#define EN 8

#define OE 7
#define OUT 2

#define S0 5
#define S1 6
#define S2 3
#define S3 4

int r, g, b;

void setup()
{
  pinMode(EN, OUTPUT);
  pinMode(OE, OUTPUT);

  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);

  pinMode(OUT, INPUT);

  // Configure the sensor to 2% scaling
  digitalWrite(S0, HIGH);
  digitalWrite(S1, LOW);
  digitalWrite(OE, LOW);

  Serial.begin(9600);
}

void loop()
{
  // Configure the sensor to read red
  digitalWrite(S2, LOW);
  digitalWrite(S3, LOW);
  delay(10);

  r = pulseIn(OUT, HIGH);

  // Configure it to read green
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  delay(10);

  g = pulseIn(OUT, HIGH);

  // Configure it to read blue
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  delay(10);

  b = pulseIn(OUT, HIGH);

  Serial.print("r = ");
  Serial.println(r);
  Serial.print("g = ");
  Serial.println(g);
  Serial.print("b = ");
  Serial.println(b);
  Serial.println("----");

  delay(1000);
}
