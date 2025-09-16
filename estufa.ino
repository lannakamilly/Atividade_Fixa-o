#include <DHT.h>
#include <Servo.h>

// =========================
// Configuração do hardware
// =========================
#define DHTPIN 2         // Pino do sensor DHT11
#define DHTTYPE DHT11

#define LED_PIN 3        // LED indicador de alerta
#define BUZZER_PIN 13    // Buzzer
#define BUTTON_PIN 4     // Botão de emergência

DHT dht(DHTPIN, DHTTYPE);
Servo ventilacao;

// Limites de temperatura
float tempMin = 20.0;   // Limite mínimo ideal
float tempMax = 30.0;   // Limite máximo ideal
float tempCriticaMin = 18.0; // Limite crítico mínimo
float tempCriticaMax = 35.0; // Limite crítico máximo

bool controleManual = false;

void setup() {
  Serial.begin(9600);
  dht.begin();
  
  ventilacao.attach(9);   // Servo conectado ao pino 9
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP); // Botão com resistor interno
  
  ventilacao.write(0); // Começa com ventilação fechada
}

void loop() {
  // Leitura do botão de emergência
  if(digitalRead(BUTTON_PIN) == LOW){
    controleManual = !controleManual; // Alterna o controle manual
    delay(500); // Debounce
  }
  
  float temperatura = dht.readTemperature(); // Leitura da temperatura
  
  if(isnan(temperatura)){
    Serial.println("Erro ao ler sensor!");
    return;
  }
  
  Serial.print("Temperatura: ");
  Serial.println(temperatura);
  
  if(controleManual){
    ventilacao.write(90); // Abre ventilação totalmente em modo manual
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, HIGH);
  } else {
    // Controle automático proporcional
    int anguloServo = map(temperatura, tempMin, tempMax, 0, 180);
    anguloServo = constrain(anguloServo, 0, 180);
    ventilacao.write(anguloServo);

    // Verifica limites críticos
    if(temperatura < tempCriticaMin || temperatura > tempCriticaMax){
      digitalWrite(LED_PIN, HIGH);
      digitalWrite(BUZZER_PIN, HIGH);
    } else {
      digitalWrite(LED_PIN, LOW);
      digitalWrite(BUZZER_PIN, LOW);
    }
  }

  delay(2000); // Atualiza a cada 2 segundos
}