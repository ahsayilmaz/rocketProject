#include <Wire.h>
#include <Adafruit_BMP085.h>
#include <TinyGPS++.h>
#include <RH_RF95.h>

// BMP180
Adafruit_BMP085 bmp;

// GY-NEO6MV2
TinyGPSPlus gps;
HardwareSerial &gpsSerial = Serial1;

// RFM98W
RH_RF95 rf95;

void setup() {
  // BMP180
  if (!bmp.begin()) {
    // Handle error
  }

  // GY-NEO6MV2
  gpsSerial.begin(9600);

  // RFM98W
  if (!rf95.init()) {
    // Handle error
  }
}

void loop() {
  // BMP180
  float temperature = bmp.readTemperature();
  float pressure = bmp.readPressure();

  // GY-NEO6MV2
  while (gpsSerial.available() > 0) {
    gps.encode(gpsSerial.read());
  }
  double latitude = gps.location.lat();
  double longitude = gps.location.lng();

  // RFM98W
  String message = String(temperature) + "," + String(pressure) + "," + String(altitude) + "," + String(longitude);
  rf95.send((uint8_t *)message.c_str(), message.length());
  rf95.waitPacketSent();
}
