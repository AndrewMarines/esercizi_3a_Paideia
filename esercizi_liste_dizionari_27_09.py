#Esercizi liste, dizionari
#1. Creare lista da 3 elementi. Chiedere all'utente infinite volte se vuole inserire un elemento nella lista. Se risponde sì, chiedergli che valore inserire, se risponde no mostrargli tutta la lista completa.
"""
tip usare il ciclo while con una variabile che può essere True o False.
variabile = True
while variabile:


Nel momento in cui voglio fermare il ciclo variabile = False
"""
#2. Creare una lista di 10 elementi. Stampare a schermo indice(Il numero civico della casetta...) e elemento
"""
ES: [56,3,2,1]
Indice: 0, Elemento: 56
Indice: 1, Elemento: 3
Indice: 2, Elemento: 2
Indice: 3, Elemento: 1
"""

#3. Crea un dizionario con i nomi e voti della classe e stampali a schermo

#4. Crea una lista di 3 valori e scambia il primo e l'ultimo elemento
"""
ES: [8,15,1] -> [1,15,8]
"""

#5. ALGORITMO BUBBLE-SORT 
"""
Questo esercizio dovrete spiegarmi bene le istruzioni e cosa fanno
https://www.youtube.com/watch?v=xli_FI7CuzA
"""

#6. Crea una lista di molti numeri che possono essere positivi e negativi. Contare i numeri positivi e i negativi
"""
[8,-7,10,-5,5]
N. Positivi: 3
N.negativi 2
"""

#1

lista = [1,2,3]
ciclo = True
while ciclo:
  richiesta =int(input("1 se vuoi inserire numero, 0 se vuoi stampare la lista"))
  if richiesta == 1:
    inserimento = input("Inserire valore")
    lista.append(inserimento)
  else:
    for index, elemento in enumerate(lista):
      print(f"Indice: {index} Elemento: {elemento}")
      ciclo = False

lista_2=[1,5,7,2,6]

for index, elemento in enumerate(lista_2):
  print(f"Indice: {index} Elemento: {elemento}")

dict={
  "Andrea":5,
  "Fena":8,
  "Azzola":7
}
l=[1,5,3,7,2,5]
i = 0
while i<len(l):
    j = 0
    while j<len(l)-1:
        if l[j+1] < l[j]:
            l[j], l[j+1] = l[j+1], l[j]
        j += 1
    i += 1
print(l)

lista_3=[1,15,8]
temp=lista_3[0]
lista_3[0]=lista_3[-1]
lista_3[-1]=temp
print(lista_3)

lista_4=[5,-8,7,-9,5,5]
print(lista_4)
positivi=0
negativi=0
for elemento in lista_4:
  if elemento >=0:
    positivi+=1
  else:
    negativi+=1

print(f"Positivi: {positivi} Negativi: {negativi}")
