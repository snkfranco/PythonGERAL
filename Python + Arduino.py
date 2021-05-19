from pyfirmata import Arduino, util
import time

                                #void setup(){
Uno = Arduino('COM8')
                                     # Serial.begin(9600);
print('Olá Mundo!')                  # Serial.println("Olá Mundo!");   
                                #}



while True:                     # void loop(){

    Uno.digital[13].write(1)         # digitalWrite(13, HIGH);
    print('LED ligado')              # Serial.println("LED ligado");
    time.sleep(0.5)                    # delay(1000);

    Uno.digital[13].write(0)         # digitalWrite(13, LOW);
    print('LED desligado')           # Serial.println("LED desligado");
    time.sleep(1)                    # delay(1000);

                                #}