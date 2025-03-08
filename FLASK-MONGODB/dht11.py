import network
import urequests
import time
import dht
import machine

# Konfigurasi WiFi
SSID = "PEXIST106_9"
PASSWORD = "imanilmuamal"
TOKEN = "BBUS-8hUnm03n07t4TUCweSz7Pzzl2GZV8Z"
URL = "https://industrial.api.ubidots.com/api/v1.6/devices/Demo_Machine"

# Inisialisasi sensor DHT11 di GPIO 4
sensor = dht.DHT11(machine.Pin(4))

# Inisialisasi buzzer di GPIO 5
buzzer = machine.Pin(5, machine.Pin.OUT)

# Koneksi ke WiFi dengan batas waktu (timeout)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Menghubungkan ke WiFi...")
timeout = 10  # Batas waktu koneksi 10 detik

while not wlan.isconnected() and timeout > 0:
    time.sleep(1)
    timeout -= 1

if wlan.isconnected():
    print("Terhubung ke WiFi:", wlan.ifconfig())

    # Buzzer berbunyi saat WiFi berhasil terhubung (2 beep)
    for _ in range(2):
        buzzer.on()
        time.sleep(0.2)
        buzzer.off()
        time.sleep(0.2)
else:
    print("Gagal terhubung ke WiFi, cek SSID dan Password!")

def send_to_ubidots(temperature, humidity):
    if not wlan.isconnected():
        print("Tidak terhubung ke WiFi, data tidak dikirim!")
        return  # Keluar dari fungsi jika WiFi tidak terhubung

    try:
        data = {
            "temperature": temperature,
            "humidity": humidity
        }

        headers = {
            "X-Auth-Token": TOKEN,
            "Content-Type": "application/json"
        }

        response = urequests.post(URL, json=data, headers=headers)
        
        if response.status_code == 200:
            print("Data berhasil dikirim:", response.text)
            
            # Buzzer berbunyi jika data berhasil terkirim
            buzzer.on()
            time.sleep(0.3)
            buzzer.off()
        else:
            print("Gagal mengirim data. Status code:", response.status_code)
            print("Response:", response.text)

        response.close()

    except Exception as e:
        print("Terjadi kesalahan saat mengirim data:", str(e))

while True:
    if wlan.isconnected():  # Hanya jalankan jika WiFi masih terhubung
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()

        print(f"Mengirimkan data... Suhu: {temperature}°C, Kelembapan: {humidity}%")
        send_to_ubidots(temperature, humidity)

    else:
        print("WiFi terputus, mencoba menyambungkan kembali...")
        wlan.connect(SSID, PASSWORD)
    
    # Tunggu 3 detik sebelum pengiriman berikutnya
    time.sleep(3)

 