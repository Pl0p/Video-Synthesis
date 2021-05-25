const int a1 = A7;
const int a2 = A6;
const int a3 = A5;

int val1 = 0;
int val2 = 0;
int val3 = 0;


void setup() {

  Serial.begin(115200);
}

void loop() {

  val1 = analogRead(a1);
  val2 = analogRead(a2);
  val3 = analogRead(a3);

  Serial.println(val1);
  Serial.println(val2);
  Serial.println(val3);

  delay(100);
}
