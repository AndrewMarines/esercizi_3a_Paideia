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