#include <SPI.h>
#include <Ethernet.h>

byte MAC[] = {0x90, 0xA2, 0xDA, 0x0E, 0x40, 0x9F};
byte ip[] = {192, 168, 2, 172};
byte server[] = {192, 169, 1, 149};
int port = 5678;

EthernetClient client;

void setup(){
  Serial.begin(9600);
  Ethernet.begin(MAC, ip);
  delay(1000);
  Serial.println("connecting...");
  if(client.connect(server,port)){
    Serial.println("connected.");  
  }
  client.println("0 \n");
  
}

void loop(){
  if(client.available()){
     char c = client.read();
     Serial.println("received: " + c);
  } 
}
