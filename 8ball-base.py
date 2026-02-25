# N.B.: questo è lo scheletro più basilare possibile. Il tutto può essere modificato, migliorato e/o ampliato in qualsiasi momento. 

import random #Importiamo il modulo random

risposta = "" #La risposta sarà definita in base al numero randomico

numero_randomico = random.randint(1, 9) #Generiamo numero randomico

if numero_randomico == 1: #Usiamo il numero randomico per randomizzare la nostra risposta
  risposta = "Sì, decisamente"
elif numero_randomico == 2:
  risposta = "È già stato scritto nel destino"
elif numero_randomico == 3:
  risposta = "Senza ombra di dubbio"
elif numero_randomico == 4:
  risposta = "Non riesco a decifrare le arcane scritte, ritenta"
elif numero_randomico == 5:
  risposta = "Non mi va di dirlo"
elif numero_randomico == 6:
  risposta = "È meglio che tu non venga a saperlo"
elif numero_randomico == 7:
  risposta = "Assolutamente no"
elif numero_randomico == 8:
  risposta = "Sì, in questo istante"
elif numero_randomico == 9:
  risposta = "Non potrà mai succedere"
else:
  print("Errore") #Se per qualche ambiguità dovesse generare numeri diversi dagli inseriti: "Errore"

nome = "John Doe" #Nome utente
if nome == "":
  nome = "(Anonimo)" #Se vuoto, scrivi "Anonimo"

domanda = "Dovrei andare al bar ora?" #Domanda utente
if domanda == "":
  print("Non hai posto alcuna domanda")
else:
  print(str(nome) + " chiede: " + str(domanda)) #Nome e domanda nel terminal
  print("La palla magica risponde: " + str(risposta)) #Risposta nel terminal
