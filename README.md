# 🔍 Port Scanner

Python ile geliştirilmiş **basit ve hızlı** bir **port tarama** aracıdır.  
Açık portları tespit eder ve hangi servislerin çalıştığını analiz eder.  

## 🚀 Özellikler  
✔️ Belirtilen IP veya **local ağ üzerinde port tarama**  
✔️ **Tüm portları** veya sadece **yaygın portları** tarama seçeneği  
✔️ **Banner Grabbing** ile port üzerindeki servisi tespit etme  
✔️ **Raporlama** ile tüm açık portları listeleme  
✔️ Windows & Linux & macOS uyumlu  

## ⚡ Kurulum ve Kullanım  

### 📥 1. Projeyi Klonla  
```sh
git clone https://github.com/kullaniciadi/Port-Scanner.git
cd Port-Scanner
```
### 🛠 2. Gerekli Kütüphaneleri Kur  
```sh
pip install -r requirements.txt
```
### ▶️ 3. Çalıştır  
```sh
python port_scanner.py
```

## 📌 Örnek Kullanım  
```sh
Hedef IP adresini girin: 192.168.1.1
Tüm portları taramak ister misiniz? (Evet/Hayır): evet
```
📜 **Çıktı:**  
```sh
[+] Port 80 Açık - Web sunucusu çalışıyor
[+] Port 22 Açık - SSH servisi çalışıyor
[+] Port 443 Açık - HTTPS servisi çalışıyor
[-] Port 21 Kapalı
[-] Port 3306 Kapalı
```

## 📝 Lisans  
Bu proje **MIT Lisansı** ile sunulmaktadır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakabilirsiniz.  

## ✉️ İletişim  
📌 **Geliştirici:** [Mustafa Karakolcu](https://github.com/mustafakarakolcu)  
📌 **E-Mail:** m.karakolcu@hotmail.com  
🌐 Web Sitesi: mustafakarakolcu.net

