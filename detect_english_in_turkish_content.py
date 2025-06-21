import os
import re
from langdetect import detect, LangDetectException

# Klasör yolu: Türkçe içeriklerin bulunduğu ana dizin
dir_path = r"src/content"

# İngilizce tespitinde kullanılacak regex (başlık, summary, içerik)
EN_REGEX = re.compile(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}")

# Sadece Türkçe dosya adlarını filtrele (ör: _en.md, -daily-, -monthly- içermeyenler)
def is_turkish_content(filename):
    return filename.endswith('.md') and not (
        '_en.md' in filename or '-daily-' in filename or '-monthly-' in filename
    )

def detect_english_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Başlık ve summary satırlarını bul
    lines = content.splitlines()
    for line in lines[:10]:
        if EN_REGEX.search(line):
            try:
                if detect(line) == 'en':
                    return True, line.strip(), content
            except LangDetectException:
                continue
    # İçerikte İngilizce cümle var mı?
    for paragraph in content.split('\n\n'):
        if EN_REGEX.search(paragraph):
            try:
                if detect(paragraph) == 'en':
                    return True, paragraph.strip()[:80], content
            except LangDetectException:
                continue
    return False, None, content

def main():
    report = []
    deleted = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if is_turkish_content(file):
                path = os.path.join(root, file)
                found, sample, content = detect_english_in_file(path)
                if found:
                    word_count = len([w for w in content.split() if w.isalpha()])
                    if word_count > 125:
                        os.remove(path)
                        deleted.append(f"DELETED: {path} (words: {word_count})\nSample: {sample}\n")
                    else:
                        report.append(f"SHORT ENGLISH DETECTED: {path} (words: {word_count})\nSample: {sample}\n")
    if deleted:
        print("\n\n".join(deleted))
    if report:
        print("\n\n".join(report))
    if not deleted and not report:
        print("Hiç İngilizce içerik tespit edilmedi.")

if __name__ == "__main__":
    main()
