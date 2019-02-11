/***************************************************************************
  This is a library for the Adafruit AS7262 6-Channel Visible Light Sensor

  This sketch reads the sensor

  Designed specifically to work with the Adafruit AS7262 breakout
  ----> http://www.adafruit.com/products/3779
  
  These sensors use I2C to communicate. The device's I2C address is 0x49
  Adafruit invests time and resources providing this open source code,
  please support Adafruit andopen-source hardware by purchasing products
  from Adafruit!
  
  Written by Dean Miller for Adafruit Industries.
  BSD license, all text above must be included in any redistribution
 ***************************************************************************/

#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <TimeLib.h>
#include "Adafruit_AS726x.h"

const int chipSelect = 10;

//create the object
Adafruit_AS726x ams;

//buffer to hold raw values
uint16_t sensorValues[AS726x_NUM_CHANNELS];

//buffer to hold calibrated values (not used by default in this example)
//float calibratedValues[AS726x_NUM_CHANNELS];

void setup() {
  Serial.begin(9600);
  while(!Serial);
  
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);

  //begin and make sure we can talk to the sensor
  if(!ams.begin()){
    Serial.println("could not connect to sensor! Please check your wiring.");
    while(1);
  }

  Serial.print("Initializing SD card...");

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    while (1);
  }
  Serial.println("card initialized.");
}

void loop() {
  
  //ams.drvOn(); //uncomment this if you want to use the driver LED for readings
  ams.startMeasurement(); //begin a measurement
  
  //wait till data is available
  bool rdy = false;
  while(!rdy){
    delay(5);
    rdy = ams.dataReady();
  }

  //read the values!
  ams.readRawValues(sensorValues);
  /*
  Serial.print(" Violet: "); Serial.print(sensorValues[AS726x_VIOLET]);
  Serial.print(" Blue: "); Serial.print(sensorValues[AS726x_BLUE]);
  Serial.print(" Green: "); Serial.print(sensorValues[AS726x_GREEN]);
  Serial.print(" Yellow: "); Serial.print(sensorValues[AS726x_YELLOW]);
  Serial.print(" Orange: "); Serial.print(sensorValues[AS726x_ORANGE]);
  Serial.print(" Red: "); Serial.print(sensorValues[AS726x_RED]);
  Serial.println();
  Serial.println();
*/
  time_t timeStamp = now();
  //Serial.println(now());
  String dataString = String(timeStamp) + "," + String(sensorValues[AS726x_VIOLET]) + "," + String(sensorValues[AS726x_BLUE]) + 
                      "," + String(sensorValues[AS726x_GREEN]) + + "," + String(sensorValues[AS726x_YELLOW]) + + "," + String(sensorValues[AS726x_ORANGE]) + "," + String(sensorValues[AS726x_RED]);

  Serial.println(dataString);
  delay(1000);
  /*
  File dataFile = SD.open("data.txt", FILE_WRITE);
  // if the file is available, write to it:
  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    // print to the serial port too:
    Serial.println(dataString);
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog.txt");
  
  */
}
