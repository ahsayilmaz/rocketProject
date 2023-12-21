# Roket Veri Görselleştirme

Bu proje, bir roketin sensörlerinden alınan verileri kablosuz olarak iletmek ve bir bilgisayar arayüzünde gerçek zamanlı olarak görselleştirmek için tasarlanmıştır.

## Kurulum

1. **Bilgisayar Arayüzü (dummyInterface):**
   - Bu klasördeki `dummyInterface.py` dosyasını çalıştırarak Tkinter tabanlı bir arayüzü başlatın.
   - Arayüz, roketin anlık verilerini gösterir ve kullanıcıya veri akışını durdurma veya devam ettirme olanağı tanır.

2. **Prototip Arduino (mainArduinoPrototype):**
   - Bu klasördeki Arduino kodunu roket prototipinizdeki bir Arduino kartına yükleyin.
   - BMP180 sensörü ile sıcaklık ve basınç ölçümlerini alın.
   - GY-NEO6MV2 GPS modülü ile roketin konumunu belirleyin.
   - RFM98W LoRa modülü ile alınan verileri kablosuz olarak bilgisayar arayüzüne iletim yapın.

## Kullanım

1. Arayüzü başlatın (`dummyInterface.py`).
2. Prototip Arduino'yu çalıştırın ve roket sensörlerinden alınan verilerin arayüze aktarıldığını gözlemleyin.
3. Arayüzdeki "Pause" düğmesini kullanarak veri akışını durdurabilir veya devam ettirebilirsiniz.

## Bağımlılıklar

- Tkinter
- Matplotlib
- Adafruit BMP085 Kütüphanesi
- TinyGPS++ Kütüphanesi
- RadioHead RF95 Kütüphanesi

## Lisans

Bu proje GNU Genel Kamu Lisansı (GPL) sürüm 3 altında lisanslanmıştır - [LICENSE.md](LICENSE.md) dosyasına bakın.
