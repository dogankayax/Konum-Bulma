# Konum-Bulma (app.py)

Bu dosya, `src/Konum-Bulma/app.py` içindeki Flask uygulaması için Türkçe bir kullanım kılavuzudur. Araç ngrok tüneli ile birlikte çalışarak lokal Flask uygulamanızı internete açar ve ziyaretçilerin IP / başlık bilgilerini HTML sayfası ve terminale yazdırır.

---

## Özellikler
- Flask tabanlı basit web arayüzü (Instagram takibi temalı gösterim sayfası)
- pyngrok ile otomatik ngrok tüneli oluşturma
- Gelen ziyaretçi bilgilerini (IP, User-Agent, X-Forwarded-For) terminale yazdırma
- Mobil/masaüstü uyumlu basit HTML ön yüz

---

## Gereksinimler
- Python 3.8+
- Flask
- pyngrok

requirements örneği (manuel yükleme):

```bash
pip install flask pyngrok
```

Not: Projeye özel ortam bağımlılıkları varsa proje kökünde `requirements.txt` dosyası kullanabilirsiniz.

---

## Kurulum & Çalıştırma
1. Gerekli paketleri yükleyin:

```bash
pip install flask pyngrok
```

2. `app.py` dosyasını çalıştırın:

```bash
python src/Konum-Bulma/app.py
```

3. Eğer sisteminizde ngrok kurulu değilse, `app.py` pyngrok ile otomatik olarak deneyecektir veya kurulum hakkında uyarı verip yönlendirme yapacaktır. README içindeki uyarılar ve `install_ngrok_warning()` fonksiyonu kullanıcılara nasıl kuracaklarını gösterir.

---

## Nasıl Çalışıyor (Kısa Açıklama)
- Program başta `check_ngrok_installed()` ile yerel sistemde `ngrok` komutunun veya pyngrok kitaplığının varlığını kontrol eder.
- Ngrok yoksa kullanıcıya kurulum talimatı gösterir ve GitHub üzerindeki `Ngrok-kurulum` reposuna yönlendirme teklif eder.
- Ngrok varsa `setup_ngrok_tunnel()` fonksiyonu ile 5000 portuna TLS ile bir public URL açar.
- Web tarayıcısı üzerinden açılan her istek `index()` fonksiyonunda yakalanır, terminale ziyaretçi bilgileri yazılır ve aynı zamanda kullanıcıya gösteren bir HTML sayfa döndürülür.

---

## README için Örnek Terminal "Screenshot" (Türkçe, ASCII ön izleme)
Aşağıda `app.py` çalıştırıldığında terminalde görülebilecek tipik çıktının bir örneği bulunmaktadır.

```
🔍 Sistem kontrolü yapılıyor...
✅ Pyngrok üzerinden ngrok kurulu: 3.4.0

🌐==================================================
✅ NGROK TÜNELİ BAŞARIYLA AÇILDI!
==================================================
📱 Public URL: https://abcd-1234-5678-ngrok-free.app
🔗 Local URL: http://localhost:5000
📡 Tunnel: https://abcd-1234-5678-ngrok-free.app -> 5000
==================================================

🚀 Flask sunucusu başlatılıyor...
📡 Ngrok URL: https://abcd-1234-5678-ngrok-free.app
🔗 Yerel URL: http://localhost:5000
⏳ Ziyaretçileri bekliyorum...

🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
🆕 YENİ ZİYARETÇİ!
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
📅 Tarih: 2025-10-17 14:23:12
🌐 Public URL: https://abcd-1234-5678-ngrok-free.app
📱 Gerçek IP: 85.34.12.100
🖥️ User Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)...
🔗 X-Forwarded-For: 85.34.12.100
```

Bu ASCII ön izleme gerçek çalıştırma sırasında farklı değerlere sahip olacaktır (ngrok token, public URL, IP adresleri vb.).

---

## Güvenlik & Etik Uyarı
- Bu proje eğitim amaçlıdır. Kötü niyetli (izinsiz) takip, veri toplama veya saldırı amaçlı kullanmayın.
- Ngrok üzerinden açılan public URL'ler herkese erişilebilir hale gelir; hassas servisleri direkt olarak açmayın.

---
---

## Lisans
Bu proje MIT lisansı altında dağıtılmaktadır. Ayrıntılar proje kökündeki `LICENSE` dosyasında bulunur.
