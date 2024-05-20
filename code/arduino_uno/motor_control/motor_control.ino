const int motor1_pin1 = 7;
const int motor1_pin2 = 4;
const int motor2_pin1 = 3;
const int motor2_pin2 = 2;
const int motor3_pin1 = 9;
const int motor3_pin2 = 8;
const int motor4_pin1 = 13;
const int motor4_pin2 = 12;
const int motor1_pwm_pin = 6;
const int motor2_pwm_pin = 5;
const int motor3_pwm_pin = 10;
const int motor4_pwm_pin = 11;
unsigned long previousMillis = 0;
unsigned long interval = 1;
char c = '\0';
char ceche = '\0';

class Wheel {
public:
    Wheel(int pin1, int pin2, int pwmpin) : pin1(pin1), pin2(pin2), pwmpin(pwmpin) {
        pinMode(pin1, OUTPUT);
        pinMode(pin2, OUTPUT);
        pinMode(pwmpin, OUTPUT);
    }

    void Positive() {
        digitalWrite(pin1, HIGH);
        digitalWrite(pin2, LOW);
        analogWrite(pwmpin, pwm);
    }

    void Reverse() {
        digitalWrite(pin1, LOW);
        digitalWrite(pin2, HIGH);
        analogWrite(pwmpin, pwm);
    }

    void Stop() {
        digitalWrite(pin1, HIGH);
        digitalWrite(pin2, HIGH);
    }

    void setPWM(int speed) {
        pwm = speed;
    }

private:
    int pin1;
    int pin2;
    int pwmpin;
    int pwm = 165;
};

class MyCar {
public:
    MyCar(int m1_pin1, int m1_pin2, int m1_pwmpin,
        int m2_pin1, int m2_pin2, int m2_pwmpin,
        int m3_pin1, int m3_pin2, int m3_pwmpin,
        int m4_pin1, int m4_pin2, int m4_pwmpin)
        : wheel1(m1_pin1, m1_pin2, m1_pwmpin),
        wheel2(m2_pin1, m2_pin2, m2_pwmpin),
        wheel3(m3_pin1, m3_pin2, m3_pwmpin),
        wheel4(m4_pin1, m4_pin2, m4_pwmpin) {}

    void SetAllWheelsPWM(int speed) {
        wheel1.setPWM(speed);
        wheel2.setPWM(speed);
        wheel3.setPWM(speed);
        wheel4.setPWM(speed);
    }

    void Move(char command) {
        switch (command) {
        case 'w': Forward(); break;
        case 's': Backward(); break;
        case 'a': Left(); break;
        case 'd': Right(); break;
        case 'z': LeftForward(); break;
        case 'x': RightForward(); break;
        case 'c': LeftBackward(); break;
        case 'v': RightBackward(); break;
        case 'q': TurnLeft(); break;
        case 'e': TurnRight(); break;
        default: Stop(); break;
        }
    }

    void ProcessCommand(char command, char ceche) {
        int speed;
        switch (command) {
            case 'i': speed = 75; break;
            case 'o': speed = 120; break;
            case 'p': speed = 165; break;
            case 'k': speed = 210; break;
            case 'l': speed = 255; break;
            default: speed = -1; break; // Indicates invalid speed command
        }

        if (speed != -1) {
            SetAllWheelsPWM(speed);
            Move(ceche);
        } else {
            Move(command);
        }
    }

private:
    void Forward() {
        wheel1.Positive();
        wheel2.Positive();
        wheel3.Positive();
        wheel4.Positive();
    }

    void Backward() {
        wheel1.Reverse();
        wheel2.Reverse();
        wheel3.Reverse();
        wheel4.Reverse();
    }

    void Left() {
        wheel1.Positive();
        wheel2.Reverse();
        wheel3.Reverse();
        wheel4.Positive();
    }

    void Right() {
        wheel1.Reverse();
        wheel2.Positive();
        wheel3.Positive();
        wheel4.Reverse();
    }

    void LeftForward() {
        wheel1.Stop();
        wheel2.Positive();
        wheel3.Positive();
        wheel4.Stop();
    }

    void RightForward() {
        wheel1.Positive();
        wheel2.Stop();
        wheel3.Stop();
        wheel4.Positive();
    }

    void LeftBackward() {
        wheel1.Stop();
        wheel2.Reverse();
        wheel3.Reverse();
        wheel4.Stop();
    }

    void RightBackward() {
        wheel1.Reverse();
        wheel2.Stop();
        wheel3.Stop();
        wheel4.Reverse();
    }

    void TurnLeft() {
        wheel1.Reverse();
        wheel2.Positive();
        wheel3.Reverse();
        wheel4.Positive();
    }

    void TurnRight() {
        wheel1.Positive();
        wheel2.Reverse();
        wheel3.Positive();
        wheel4.Reverse();
    }

    void Stop() {
        wheel1.Stop();
        wheel2.Stop();
        wheel3.Stop();
        wheel4.Stop();
    }

private:
    Wheel wheel1;
    Wheel wheel2;
    Wheel wheel3;
    Wheel wheel4;
};

MyCar car(motor1_pin1, motor1_pin2, motor1_pwm_pin,
    motor2_pin1, motor2_pin2, motor2_pwm_pin,
    motor3_pin1, motor3_pin2, motor3_pwm_pin,
    motor4_pin1, motor4_pin2, motor4_pwm_pin);

void setup() {
    Serial.begin(9600);
}

void loop() {
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;

        if (Serial.available() > 0) {
            c = Serial.read();
        } else {
            c = '\0';
        }

        car.ProcessCommand(c, ceche);

        if (c != 'i' && c != 'o' && c != 'p' && c != 'k' && c != 'l' && c != '\0') {
            ceche = c;
        }
        Serial.flush();
    }
}
