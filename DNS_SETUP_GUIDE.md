# MindVerse Daily - DNS Ayar Rehberi

## GitHub Pages için DNS Konfigürasyonu

### CNAME Kaydı (Ana Kayıt)
```
Type: CNAME
Name: www
Value: ykperdgn.github.io
TTL: 3600 (veya otomatik)
```

### A Kayıtları (GitHub Pages IP'leri)
```
Type: A
Name: @ (veya boş)
Value: 185.199.108.153
TTL: 3600

Type: A
Name: @ (veya boş)
Value: 185.199.109.153
TTL: 3600

Type: A
Name: @ (veya boş)
Value: 185.199.110.153
TTL: 3600

Type: A
Name: @ (veya boş)
Value: 185.199.111.153
TTL: 3600
```

### AAAA Kayıtları (IPv6 - İsteğe Bağlı)
```
Type: AAAA
Name: @ (veya boş)
Value: 2606:50c0:8000::153
TTL: 3600

Type: AAAA
Name: @ (veya boş)
Value: 2606:50c0:8001::153
TTL: 3600

Type: AAAA
Name: @ (veya boş)
Value: 2606:50c0:8002::153
TTL: 3600

Type: AAAA
Name: @ (veya boş)
Value: 2606:50c0:8003::153
TTL: 3600
```

## DNS Propagation Süresi

- DNS değişiklikleri 15 dakika - 48 saat arasında yayılabilir
- Genellikle 1-2 saat içinde çalışmaya başlar
- `nslookup www.mindversedaily.com` komutu ile kontrol edebilirsiniz

## Doğrulama

1. DNS ayarlarını yaptıktan sonra 15-30 dakika bekleyin
2. GitHub Pages settings sayfasında "DNS check was successful" mesajını bekleyin
3. Site `https://www.mindversedaily.com` adresinde erişilebilir olacak

## Sorun Giderme

- Eğer DNS check hâlâ başarısız oluyorsa, CNAME kaydında `ykperdgn.github.io` olduğundan emin olun
- TTL değerini 300 (5 dakika) yaparak daha hızlı propagation sağlayabilirsiniz
- Bazı DNS sağlayıcılarında "@" yerine domain adınızı yazmanız gerekebilir
