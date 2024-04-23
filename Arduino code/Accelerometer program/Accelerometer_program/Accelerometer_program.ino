#include <LiquidCrystal.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
      
      
      Adafruit_MPU6050 mpu;
      
/*  LiquidCrystal lcd(12, 11, 10, 9, 8, 7);
 class Lc{
public:
 void LCD_Start();
 void acc_components(float x,float y,float z ); 
 void gyro_angles(float i,float p,float u );
};*/ 



/*void Lc::LCD_Start(){
   lcd.begin(16, 2);
    lcd.setCursor(15,0);
    lcd.print("Earthquake meter");
    
  int i=1;
  for(i=1;i<=34;i++){
      
      lcd.scrollDisplayLeft();
      delay(250); 
     
  }
    delay(900);
    lcd.clear();
}
void Lc::acc_components(float x,float y,float z){
    lcd.setCursor(0,0);
    lcd.print(x);
    lcd.setCursor(10,0);
    lcd.print(y);
    lcd.setCursor(6,1);
    lcd.print(z)
;
}

void Lc::gyro_angles(float i,float p,float u ){
    lcd.setCursor(0,1);
    lcd.print(i);
    lcd.setCursor(5,1);
    lcd.print(p);
    lcd.setCursor(10,1);
    lcd.print(u);

}*/
void setup() {
    //Lc someshit;
    Serial.begin(9600);
    //someshit.LCD_Start();
    while (!mpu.begin()) {
    Serial.println("MPU6050 not connected!");
    delay(10000);
  }
    //someshit.acc_components(1.0,1.0,1.0);

}
     
sensors_event_t event;

void loop() {
  
mpu.getAccelerometerSensor()->getEvent(&event);
   mpu.getAccelerometerSensor()->getEvent(&event);
            Serial.println(event.acceleration.x);
            Serial.println(event.acceleration.y);
            Serial.println(event.acceleration.z);
            delay(1);

    
  

}

