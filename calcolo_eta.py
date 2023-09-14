#Creiamo una variabile
#nome = valore
#anno_attuale = 2023
#far inserire all'utente l'anno attuale
anno_attuale = int(input("Inserisci l'anno attuale"))
#anno_prossimo = anno_attuale + 1
#secondo metodo per incrementare
#anno_prossimo+=1
#dire ad utente la variabile anno_attuale
anno_nascita = int(input("inserisci il tuo anno di nascita"))
  
#controllo se son inseriti correttamente gli anni
if(anno_attuale > annno_nascita):
  #calcolo e stampaggio età utente
  eta=anno_attuale-anno_nascita
  print("La tua età è ", eta)

else:
  print("Hai sbagliato ad inserire gli anni")
