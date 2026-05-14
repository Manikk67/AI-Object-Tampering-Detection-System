char data;

void setup()
{
    pinMode(12, OUTPUT);

    pinMode(13, OUTPUT);

    pinMode(8, OUTPUT);

    Serial.begin(9600);
}

void loop()
{
    if(Serial.available())
    {
        data = Serial.read();

        //ALARM STATE
        if(data == '1')
        {
            //green LED OFF
            digitalWrite(12, LOW);

            //red LED ON
            digitalWrite(13, HIGH);

            //buzzer ON
            digitalWrite(8, HIGH);
        }

        //NORMAL STATE
        else if(data == '0')
        {
            //green LED ON
            digitalWrite(12, HIGH);

            //red LED OFF
            digitalWrite(13, LOW);

            //buzzer OFF
            digitalWrite(8, LOW);
        }
    }
}