import socket
import threading

# Açık portları kaydedeceğimiz liste
open_ports = {}

# Hangi servisin çalıştığını bulmaya çalışan fonksiyon
def get_service_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # Timeout süresi
        s.connect((ip, port))
        
        # Banner grabbing için veri gönderme
        s.send(b'HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n')
        response = s.recv(1024)  # Servisten gelen yanıtı al
        s.close()
        
        return response.decode("utf-8", "ignore").strip()
    except:
        return "Bilinmeyen Servis"

# Tek bir portu tarayan fonksiyon
def scan_port(ip, port):
    global open_ports
    try:
        with socket.create_connection((ip, port), timeout=1):
            service_info = get_service_banner(ip, port)  # Servis bilgisi al
            print(f"[+] Port {port} Açık - {service_info}")
            open_ports[port] = service_info  # Açık portu kaydet
    except:
        pass  # Port kapalıysa hata mesajı göstermiyoruz

# Kullanıcıdan hedef IP adresini al
ip = input("Hedef IP adresini girin: ")

# Kullanıcıya tüm portları mı yoksa belirli aralığı mı taramak istediğini sor
full_scan = input("Tüm portları taramak ister misiniz? (Evet/Hayır): ").strip().lower()

if full_scan == "evet":
    ports = range(1, 65536)  # Tüm portları tara
else:
    ports = [21, 22, 25, 53, 80, 135, 139, 443, 445, 3306, 3389, 8080]  # Sık kullanılan portlar

# Thread'ler ile tarama başlat
threads = []
for port in ports:
    thread = threading.Thread(target=scan_port, args=(ip, port))
    threads.append(thread)
    thread.start()

# Thread'lerin tamamlanmasını bekle
for thread in threads:
    thread.join()

# Açık portları rapor olarak göster
if open_ports:
    print("\n📌 **TARAMA RAPORU** 📌")
    for port, service in open_ports.items():
        print(f"✅ {port} Açık - {service}")
else:
    print("⚠️ Açık port bulunamadı.")
