import os
from datetime import datetime
import random
import schedule
import time

categories = ["health", "love", "history", "psychology", "space", "quotes"]

# Gelişmiş içerik şablonları
example_contents = {
    "health": [
        "---\ntitle: 'Günün Sağlık İpucu: {topic}'\ndate: {date}\nsummary: 'Sağlıklı yaşam için {topic} hakkında bilmeniz gerekenler.'\ntags: ['sağlık', 'yaşam', '{tag}']\nviews: {views}\n---\n\n{content}",
        "---\ntitle: 'Sağlık Rehberi: {topic}'\ndate: {date}\nsummary: '{topic} ile ilgili uzman tavsiyeleri.'\ntags: ['sağlık', 'rehber', '{tag}']\nviews: {views}\n---\n\n{content}"
    ],
    "love": [
        "---\ntitle: 'İlişki Tavsiyeleri: {topic}'\ndate: {date}\nsummary: '{topic} hakkında uzman görüşleri.'\ntags: ['aşk', 'ilişkiler', '{tag}']\nviews: {views}\n---\n\n{content}",
        "---\ntitle: 'Aşkın Psikolojisi: {topic}'\ndate: {date}\nsummary: '{topic} ile ilgili psikolojik yaklaşımlar.'\ntags: ['aşk', 'psikoloji', '{tag}']\nviews: {views}\n---\n\n{content}"
    ],
    "history": [
        "---\ntitle: 'Tarihte Bugün: {topic}'\ndate: {date}\nsummary: '{topic} ile ilgili tarihi olaylar.'\ntags: ['tarih', 'günlük', '{tag}']\nviews: {views}\n---\n\n{content}",
        "---\ntitle: 'Tarihi Kişilikler: {topic}'\ndate: {date}\nsummary: '{topic} hakkında bilinmeyenler.'\ntags: ['tarih', 'kişilik', '{tag}']\nviews: {views}\n---\n\n{content}"
    ],
    "psychology": [
        "---\ntitle: 'Psikoloji Rehberi: {topic}'\ndate: {date}\nsummary: '{topic} ile ilgili psikolojik yaklaşımlar.'\ntags: ['psikoloji', 'zihin', '{tag}']\nviews: {views}\n---\n\n{content}",
        "---\ntitle: 'Zihin Sağlığı: {topic}'\ndate: {date}\nsummary: '{topic} hakkında bilinmesi gerekenler.'\ntags: ['psikoloji', 'sağlık', '{tag}']\nviews: {views}\n---\n\n{content}"
    ],
    "space": [
        "---\ntitle: 'Uzay Keşfi: {topic}'\ndate: {date}\nsummary: '{topic} hakkında son gelişmeler.'\ntags: ['uzay', 'bilim', '{tag}']\nviews: {views}\n---\n\n{content}",
        "---\ntitle: 'Astronomi: {topic}'\ndate: {date}\nsummary: '{topic} ile ilgili bilimsel yaklaşımlar.'\ntags: ['uzay', 'astronomi', '{tag}']\nviews: {views}\n---\n\n{content}"
    ],
    "quotes": [
        "---\ntitle: 'Günün Sözü: {topic}'\ndate: {date}\nsummary: '{topic} hakkında ilham verici alıntı.'\ntags: ['alıntı', 'motivasyon', '{tag}']\nviews: {views}\n---\n\n{content}",
        "---\ntitle: 'Ünlü Sözler: {topic}'\ndate: {date}\nsummary: '{topic} ile ilgili ünlü alıntılar.'\ntags: ['alıntı', 'ünlü', '{tag}']\nviews: {views}\n---\n\n{content}"
    ]
}

# Kategori bazlı konu önerileri
topics = {
    "health": ["Beslenme", "Egzersiz", "Uyku", "Stres Yönetimi", "Vitamin", "Su İçmek"],
    "love": ["İletişim", "Güven", "Romantizm", "Uzak İlişki", "Evlilik", "Flört"],
    "history": ["Antik Çağ", "Savaşlar", "Keşifler", "İmparatorluklar", "Devrimler", "Kültür"],
    "psychology": ["Motivasyon", "Hafıza", "Duygular", "Davranış", "Kişilik", "Öğrenme"],
    "space": ["Gezegenler", "Yıldızlar", "Galaksiler", "Uzay Seyahati", "NASA", "Kepler"],
    "quotes": ["Başarı", "Hayat", "Aşk", "Bilgelik", "Cesaret", "Mutluluk"]
}

def generate_article(category):
    today = datetime.now().strftime("%Y-%m-%d")
    template = random.choice(example_contents[category])
    topic = random.choice(topics[category])
    tag = topic.lower().replace(" ", "-")
    views = random.randint(100, 2000)

    # Basit içerik örnekleri
    content_examples = {
        "health": f"{topic} sağlığınız için çok önemlidir. Uzmanlar bu konuda şu tavsiyelerde bulunuyor:\n\n1. Düzenli olarak {topic.lower()} konusuna dikkat edin\n2. Günlük rutininize dahil edin\n3. Uzman kontrolü yaptırın\n\nBu adımları takip ederek daha sağlıklı bir yaşam sürebilirsiniz.",
        "love": f"{topic} ilişkilerde kritik bir faktördür. İşte {topic.lower()} hakkında bilmeniz gerekenler:\n\n- Açık iletişim kurun\n- Karşılıklı anlayış gösterin\n- Sabırlı olun\n- Birbirinize destek olun\n\nBu prensipler güçlü ilişkiler kurmanın temelidir.",
        "history": f"{topic} tarihinde önemli bir yer tutar. Bu dönemde:\n\n• Büyük değişimler yaşandı\n• Toplumsal dönüşümler gerçekleşti\n• Kültürel gelişmeler oldu\n\nBu olaylar günümüzü de etkilemeye devam ediyor.",
        "psychology": f"{topic} psikolojisinde araştırmalar şunu gösteriyor:\n\nİnsan {topic.lower()}'i karmaşık bir süreçtir. Bilim insanları bu alanda:\n- Yeni teoriler geliştiriyor\n- Pratik çözümler sunuyor\n- Tedavi yöntemleri araştırıyor\n\nBu bilgiler günlük yaşamda faydalı olabilir.",
        "space": f"{topic} uzay bilimlerinde heyecan verici bir alan. Son araştırmalar:\n\n🚀 Yeni keşifler yapılıyor\n🌌 Teknoloji gelişiyor\n⭐ Gizli sırlar çözülüyor\n\nBu gelişmeler insanlığın geleceğini şekillendirecek.",
        "quotes": f'"{topic} hayatın en değerli hediyesidir." - Bilinmeyen\n\nBu söz bize şunu hatırlatıyor:\n- Hayatın değerini bil\n- Anı yaşa\n- Umutla ilerle\n\nİlham verici sözler ruhumuza dokunur.'
    }

    content = content_examples.get(category, "Bu konu hakkında daha fazla araştırma yapılması gerekiyor.")

    return template.format(
        date=today,
        topic=topic,
        tag=tag,
        views=views,
        content=content
    )

def save_article(category, content):
    folder = f"src/content/{category}"
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{datetime.now().strftime('%Y-%m-%d')}-{random.randint(10000,99999)}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ {category} kategorisine yeni içerik eklendi: {filename}")

def generate_daily_content():
    """Her kategoriye günlük içerik ekler"""
    print(f"\n🤖 Otomatik içerik üretimi başladı - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    for category in categories:
        content = generate_article(category)
        save_article(category, content)
    print("✨ Tüm kategorilere günlük içerikler eklendi!\n")

def generate_batch_content(count=3):
    """Her kategoriye toplu içerik ekler"""
    print(f"\n📦 Toplu içerik üretimi başladı - {count} adet/kategori")
    for category in categories:
        for i in range(count):
            content = generate_article(category)
            save_article(category, content)
    print(f"✨ Her kategoriye {count} adet içerik eklendi!\n")

# Zamanlayıcı ayarları
def setup_scheduler():
    """Otomatik içerik üretimi için zamanlayıcı kurar"""
    schedule.every().day.at("09:00").do(generate_daily_content)
    schedule.every().day.at("15:00").do(generate_daily_content)

    print("⏰ Zamanlayıcı ayarlandı:")
    print("  - Her gün 09:00'da otomatik içerik")
    print("  - Her gün 15:00'da otomatik içerik")
    print("  - Çıkmak için Ctrl+C")

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "batch":
            count = int(sys.argv[2]) if len(sys.argv) > 2 else 3
            generate_batch_content(count)
        elif sys.argv[1] == "scheduler":
            setup_scheduler()
        elif sys.argv[1] == "single":
            generate_daily_content()
    else:
        # Varsayılan: tek seferlik içerik üretimi
        generate_daily_content()
