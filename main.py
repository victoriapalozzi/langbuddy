import random

greetings = ["Hola", "Buenos días", "Buenas tardes", "Buenas noches"]

responses = [
    "¿Cómo estás?",
    "¿En qué puedo ayudarte hoy?",
    "Hablemos de algo interesante",
    "Cuéntame más sobre ti",
    "Estoy aquí para practicar español contigo",
    "¿Tienes alguna pregunta?"
]

endings = ["Adiós", "Hasta luego", "Nos vemos"]

def get_response():
  return random.choice(responses)

def chat():
  print("Lang Bud: " + random.choice(greetings))
  
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["adiós", "hasta luego", "nos vemos"]:
      print("Lang Bud: " + random.choice(endings))
      break
    else:
      print("Lang Bud: " + get_response())

chat()      
      
  
