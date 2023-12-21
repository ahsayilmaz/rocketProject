# Roket Veri Görselleştirme

Bu depo, roketin farklı verilerini görselleştirmek ve izlemek için kullanılan bir dizi arayüz ve Arduino uygulamasını içerir.

## Dummy Arayüzü

Bu kısım, roket verilerini simüle eden bir arayüz sağlar. Tkinter kullanılarak oluşturulan bu arayüz, matplotlib kütüphanesi ile gerçek zamanlı veri görselleştirmesi yapar. Dummy verilerle çalışır ve bir roketin zamanla değişen yükseklik, hız, basınç, sıcaklık ve ivmesini taklit eder.

## Prototype Arayüzü
Bu kısım, gerçek donanım cihazlarından gelen roket verilerini görselleştirmek için kullanılır. Tkinter ve matplotlib kullanılarak oluşturulan arayüz, bir Raspberry Pi ve LoRa modülü aracılığıyla gerçek zamanlı olarak roket verilerini alır.

## Başlatma
Arduino IDE kullanarak Arduino kartınıza yüklenmiş kodu çalıştırın.

## Main Arduino Prototipi
Bu kısım, roket verilerini toplamak ve LoRa modülü aracılığıyla göndermek için kullanılan Arduino prototipinin ana kodunu içerir. BMP180 ve GY-NEO6MV2 sensörleri ile roket verilerini toplar ve RFM98W modülü ile verileri gönderir.

## Gereksinimler
Adafruit_BMP085 kütüphanesi
TinyGPS++ kütüphanesi
RH_RF95 kütüphanesi


## Lisans

Bu proje GNU Genel Kamu Lisansı (GPL) sürüm 3 altında lisanslanmıştır - [LICENSE.md](LICENSE.md) dosyasına bakın.
