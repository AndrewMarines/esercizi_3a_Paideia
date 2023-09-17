#1. Calcolare area di un cerchio basandosi sul raggio dato dall'utente;

#Usiamo il float perchè l'utente può usare anche numeri con la virgola. Se avessimo messo int il nostro programma
#non avrebbe risolto i casi limite
raggio = float(input("Inserisci il raggio del cerchio in cm"))
pi=3.14
area=pi*(raggio ** 2)
print(f"L'area è {area} cm")
#2. Chiedere all'utente nome e cognome e riscriverli entrambi al contrario(es. Andrea Marini->iniraM aerdnA);
stringa = input("Metti il tuo nome e cognome")
#usiamo il metodo dello SLICING!
print(stringa[::-1])

#3. Chiedere all'utente un numero. Fare la sottrazione tra 17 e il numero dell'utente. Se il numero e' negativo, renderlo positivo!(e' il val. assoluto di un numero);
numero = int(input("Inserisci un numero"))
#Con abs() facciamo il valore assoluto di un nuero direttamente senza fare nessun if!
print(abs(17 - numero))

#4. Chiedere all'utente un numero. Controllare se questo e' compreso tra 1 e 100;
numero_range= int(input("Inserisci un numero"))
#Ci sono due metodi facili: range() e fare un if semplice. Facciamo l'if semplice
if(numero_range >= 1 and numero_range<=100):
  print("Il numero è compreso")
else:
  print("Numero non compreso")

#5. Chiedere all'utente un numero. Verificare se questo e' pari o dispari. Ricordate operatore modulo;
numero_pari_dispari = int(input("Inserisci un numero"))
#Ricordarsi che stiamo confrontando due valori, non lo stiamo immettendo. Dobbiamo quindi usare due uguali
if(numero_pari_dispari % 2 == 0):
  print("PARI")
else:
  print("DISPARI")
#6. x="Pallino", y="Pinco". Far diventare x="Pinco", y="Pallino";
x="Pallino"
y="Pinco"
"""
L'idea di molti potrebbe essere 
y=x
x=y
Così però è sbagliato, facciamolo assieme
y=x --> y="Pallino"
x=y --> x="Pallino"
Si trasformerebbe quindi in Pallino Pallino
Usiamo quindi una variabile in più per lo swap delle variabili
"""
temp=y
y=x
x=temp
print(f"{x} {y}")
#7. Creare una lista di 5 elementi. Aggiungere un elemento all'inizio, uno alla fine e rimuoverne uno a scelta(mostrando i passaggi);
lista=[1,2,3,4,5]
#Aggiungo 0 alla posizione 0
lista.insert(0,0)
#Aggiungo 6 all'ultima posizione
lista.append(6)
#Rimuovo ultimo elemento
lista.pop()
print(lista)

#8. Chiedere all'utente 3 numeri. Trovare il numero più alto e più basso dei 3. Dire se il numero più basso moltiplicato per 2 è lo stesso più piccolo del più grande(Più strade... p.e. ragionamento o liste con funzione max :D).
primo = int(input("Inserire primo numero"))
secondo = int(input("Inserire secondo numero"))
terzo = int(input("Inserire terzo numero"))
massimo = max(primo, secondo, terzo)
minimo = min(primo, secondo, terzo)
if(minimo*2 < massimo):
  print("è ancora più piccolo")
"""
Se trovate su internet soluzioni iper-complicate per uno di questi esercizi, state sbagliando qualcosa.
Tutti questi esercizi(tranne gli ultimi 2), si fanno in max 6 righe.
Leggete e comprendete la soluzione che state leggendo, magari serve per fare qualche richiesta particolare che a voi non serve...
"""


"""
You've stumbled upon a door where your mind is the key.
There are none who will lend you guidance;
These trials are yours to conquer alone.
Entering here will take more than mere logic and strategy,
but the criteria are just as hidden as what they reveal.
This is a mirage.
"""

