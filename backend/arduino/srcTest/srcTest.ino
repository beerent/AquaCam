#include <SPI.h>
#include <Ethernet.h>
#include <LiquidCrystal.h>
#include <OneWire.h>

/*
 * --ARC--

 * circuit:
 * LCD RS (4) | digital pin 30
 * LCD Enable pin (6) | digital pin 31
 * LCD D4 pin to digital pin 32
 * LCD D5 pin to digital pin 33
 * LCD D6 pin to digital pin 34
 * LCD D7 pin to digital pin 35
 * LCD R/W (5) | ground
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)
 */
 
 /*pins:
  * 0: light1
  * 1: light2
  * 2: LCD RS 
  * 3: LCD EN
  * 4: LCD D4
  * 5: LCD D5
  * 6: LCD D6
  * 7: LCD D7
  */

int pin[2];
String UUID[2];

byte mac[] = {0x90, 0xA2, 0xDA, 0x0E, 0x40, 0x9F};
byte ip[] = {192, 168, 2, 172};
IPAddress server(192,168,2,6);
int port = 5678;
EthernetClient client;
int connected;

int relayCount = 2;
int relay[2];

// on and off times for lights
int lightOn[2];
int lightOff[2];

LiquidCrystal lcd(30, 31, 32, 33, 34, 35);

OneWire  ds(5);

// function called when Arduino needs to communicate with server
void connect2server() {
  Serial.println("connecting to server...");
  if (client.connect(server, port)) {
    connected = 1;
    Serial.println("connected.");
  } 
  else {
    Serial.println("connection failed");
  }
}

void serverDisconnect(){
  client.stop();
  connected = 0;  
}


void sendOut(String str){
  client.println(str); 
}

// accepts a String pointer, simply reads input from the Server,
// and modifies the String input (essentially returning a String).
void readIn(String &input) {
  delay(1000); //FIX: delay to allow for server to send all of the bytes
  
  // if the client has bytes to read from the server
  if (client.available()) { 
    while(client.available()!= 0){
      input += (char)client.read(); 
    }
  }
}

// accepts the current time in military time as two parameters
// turns on/off any devices that use a relay, if they need
// to be turned on/off. 
void relayTimer(int currentTime){
  
  int max = 2500;
  for(int i = 0; i < relayCount; i++){
    if(((max + currentTime - lightOn[i]) % max) < ((max + lightOff[i] - lightOn[i]) % max)){
      digitalWrite(pin[i], LOW);
      relay[i] = 1;
      Serial.println("pin " + String(i) + " launched");
    }else{
      digitalWrite(pin[i], HIGH);
      relay[i] = 0;
      Serial.println("pin " + String(i) + " blogged off");
    }
  }
  
}

void lightManager(){
  //get time from server
  connect2server();
  if (connected == 1) sendOut("0"); //request for time
  String t = ""; 
  readIn(t); //receive time
  //disconnect, we have the data.
  serverDisconnect();

  t.trim();
  Serial.println("current time = " + t);
    
  //convert Strings to ints
  int time[2];
    for(int i = 0; i  < 2; i++){
      if(t.charAt(1) == ' '){
      time[i] = (int) t.charAt(0); 
      t = t.substring(2);
    }else{
      time[i] = t.substring(0, 2).toInt();
      t = t.substring(3);
    } 
  }
  int currentTime = 0;
  
  if(time[0] == 00){
    currentTime = 0;
  } else if(String(time[0]).charAt(0) == '0'){
    currentTime = ((int) String(time[0]).charAt(1) * 100);
  } else {
    currentTime = 100 * time[0];
  }
  
  if(String(time[1]).charAt(0) == '0'){
      currentTime += (int) String(time[1]).charAt(1);
  } else {
      currentTime += time[1]; 
  }
  
  //int currentTime = (String(time[0]) + String(time[1])).toInt().trim();
  Serial.println("sending " + String(currentTime));
  //check relay timer for lights (op code 'L')
  relayTimer(currentTime);
}

void setLightTimes(){
  lightOn[0] = 1330; lightOff[0] = 2330;
  lightOn[1] = 1430; lightOff[1] = 2230;
}

// ID number, Pin number, OUTPUT/INPUT, LOW/HIGH, Device name
void addPin(int num, int p, int type, int pos, String name){
  pin[num] = p;
  if(type == 0) pinMode(pin[num], OUTPUT);
  else pinMode(pin[num], INPUT);
  if(pos == 0) digitalWrite(pin[num], LOW);
  else digitalWrite(pin[0], HIGH);  
  UUID[num] = name;
}

void statusReport(){
  // FORMAT: NAME PIN POWER(1 or 0)
  String status;
  for(int i = 0; i < relayCount; i++){
    status += UUID[i] + " " + String(pin[i]) + " " + relay[i]; 
  }
  
  connect2server();
  if(connected == 1){
    sendOut("1"); //alert for status report
    sendOut(status);
  }
  serverDisconnect();
}

//temperature layout:
//
void reportLCD(){ 
  lcd.setCursor(0, 0); 
  
  for(int i = 0; i < 2; i++){
    if(relay[i] == 0){
      lcd.print("Light " + String(i+1) + ": OFF"); 
    }else{
      lcd.print("Light " + String(i+1) + ": ON"); 
    }
    lcd.setCursor(0, 1);
  }
  displayTemperatures();
}

void setup() {
  // set light pins
  addPin(0, 22, 0, 1, "Light 1");
  relay[0] = 0; 
  addPin(1, 23, 0, 1, "Light 2");
  relay[1] = 0;
  
  //set lights
  relayCount = 2;
  setLightTimes();
  
  //initialize LCD
  lcd.begin(20, 4);
  lcd.setCursor(1, 1);
  lcd.print("welcome to the ARC");
  //five second swag delay
  for(int i = 0; i < 5; i++){
    lcd.setCursor(i, 2);
    lcd.print(".");
    delay(1000); 
  }
  lcd.clear();
  
  //initialize Serial
  Serial.begin(9600);
  
  
  //initialize ethernet connection
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    Ethernet.begin(mac, ip);
  }
  connected = 0;
}

void displayTemperatures() {
  byte i;
  byte present = 0;
  byte type_s;
  byte data[12];
  byte addr[8];
  float celsius, fahrenheit;
  
  if ( !ds.search(addr)) {
    Serial.println("No more addresses.");
    Serial.println();
    ds.reset_search();
    delay(250);
    return;
  }
  
  Serial.print("ROM =");
  for( i = 0; i < 8; i++) {
    Serial.write(' ');
    Serial.print(addr[i], HEX);
  }

  if (OneWire::crc8(addr, 7) != addr[7]) {
      Serial.println("CRC is not valid!");
      return;
  }
  Serial.println();
 
  // the first ROM byte indicates which chip
  switch (addr[0]) {
    case 0x10:
      Serial.println("  Chip = DS18S20");  // or old DS1820
      type_s = 1;
      break;
    case 0x28:
      Serial.println("  Chip = DS18B20");
      type_s = 0;
      break;
    case 0x22:
      Serial.println("  Chip = DS1822");
      type_s = 0;
      break;
    default:
      Serial.println("Device is not a DS18x20 family device.");
      return;
  } 

  ds.reset();
  ds.select(addr);
  ds.write(0x44,1);         // start conversion, with parasite power on at the end
  
  delay(1000);     // maybe 750ms is enough, maybe not
  // we might do a ds.depower() here, but the reset will take care of it.
  
  present = ds.reset();
  ds.select(addr);    
  ds.write(0xBE);         // Read Scratchpad

  Serial.print("  Data = ");
  Serial.print(present,HEX);
  Serial.print(" ");
  for ( i = 0; i < 9; i++) {           // we need 9 bytes
    data[i] = ds.read();
    Serial.print(data[i], HEX);
    Serial.print(" ");
  }
  Serial.print(" CRC=");
  Serial.print(OneWire::crc8(data, 8), HEX);
  Serial.println();

  // convert the data to actual temperature

  unsigned int raw = (data[1] << 8) | data[0];
  if (type_s) {
    raw = raw << 3; // 9 bit resolution default
    if (data[7] == 0x10) {
      // count remain gives full 12 bit resolution
      raw = (raw & 0xFFF0) + 12 - data[6];
    }
  } else {
    byte cfg = (data[4] & 0x60);
    if (cfg == 0x00) raw = raw << 3;  // 9 bit resolution, 93.75 ms
    else if (cfg == 0x20) raw = raw << 2; // 10 bit res, 187.5 ms
    else if (cfg == 0x40) raw = raw << 1; // 11 bit res, 375 ms
    // default is 12 bit resolution, 750 ms conversion time
  }
  celsius = (float)raw / 16.0;
  fahrenheit = celsius * 1.8 + 32.0;
  int f = (int) fahrenheit;
  
  lcd.setCursor(0, 2);
  lcd.print("Temperature = " + String(f));
  Serial.print("  Temperature = ");
  Serial.print(celsius);
  Serial.print(" Celsius, ");
  Serial.print(fahrenheit);
  Serial.println(" Fahrenheit");
}

void loop() {
  
  //check time with lights function, requires connection
  //lightManager();

  //refresh lcd display
  reportLCD();
  
  //submit status of hardware to server
  //statusReport();
  
  //one second 
  delay(1000);
}

// GOALS:
// temperature
// lcd function
// dpad

