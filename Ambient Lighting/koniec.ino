#include <FastLED.h>

#define NUM_LEDS 30
#define DATA_PIN 6
#define CLOCK_PIN 13
CRGB leds[NUM_LEDS];
String readString;
int r;
int g;
int b;
String a;
char *strings[10];
char *ptr = NULL;
char* str;
char temp[30];

const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];        // tymczasowa tablica uzywana przy dzieleniu danych

      


boolean newData = false;

void setup() {
Serial.begin(9600);
FastLED.addLeds<APA102, DATA_PIN, CLOCK_PIN, RGB>(leds, NUM_LEDS); 
    
}

//============

void loop() {
    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        for (int i = 0; i < NUM_LEDS; i++) {
        leds[i] = CRGB(b,g,r);
        }
        FastLED.show();   
        newData = false;
    }
}

//============

void recvWithStartEndMarkers() {             // funkcja okreslająca początek i koniec danych
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';      // okresla znak ktory oznacza poczatek danych
    char endMarker = '>';        // okresla znak ktory oznacza koniec danych
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

//============

void parseData() {      // rozdziela dane na oddzielne części wartosci RGB

    char * strtokIndx; // uzywane przez strtok jako wskaznik

    strtokIndx = strtok(tempChars,"-");      // czyta czesc danych do znaku -
    r = atoi(strtokIndx);  // zmienia wartosc na int iprzypisuje pierwsza wartosc do r
 
    strtokIndx = strtok(NULL, "-"); // kontynuuje czytanie danych do nastepnego znaku -
    g = atoi(strtokIndx);     // zmienia wartosc na int iprzypisuje pierwsza wartosc do g

    strtokIndx = strtok(NULL, "-"); //kontynuuje czytanie danych do nastepnego znaku -
    b = atoi(strtokIndx);     // zmienia wartosc na int iprzypisuje pierwsza wartosc do b

}

//============
