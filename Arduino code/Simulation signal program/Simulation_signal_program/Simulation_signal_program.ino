 void setup() {
            Serial.begin(9600);
        }
        float x =0;
        float y =0;
        float z =0;
        void loop() {
            for(float i=0; i<=1; i+=0.001){
                x= sin(2*3.14*i*10)+6*cos(2*3.14*i*30)+3*sin(2*3.14*i*20);
                z= sin(2*3.14*i*10);
                y= sin(2*3.14*i*30);
                Serial.println(x);
                Serial.println(z);
                Serial.println(y);
                delay(1); 
            }
            }
                