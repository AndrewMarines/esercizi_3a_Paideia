"""
Usando tre liste
Chiedere all'utente di inserire 
nome, data, e voto finale di 10 studenti.

La prima lista è solo per i nomi, la seconda solo per le date, la terza solo per il voto finale.

Alla fine stampare a schermo tutti i dati in modo decente.
Calcolare la media della classe.

"""

#creato 3 liste vuote
nomi=[]
date=[]
voti=[]

#chiediamo 10 volte nomi, date, voti
for i in range(3):
  nome=input("Inserisci il nome")
  data=input("Inserisci la data di nascita")
  voto=float(input("Inserisci il voto finale"))
  #aggiungiamo alle liste i valori inseriti dall'utente
  nomi.append(nome)
  date.append(data)
  voti.append(voto)


media=0
for i in range(3):
  #usando lista[indice] ottengo l'elemento numero indice della lista
  print(f"{nomi[i]} {date[i]} {voti[i]}")
  #calcoliamo la media(voti/n.voti)
  #Provate a mano questo calcolo
  media=media+voti[i]
media=media/3
print(media)
