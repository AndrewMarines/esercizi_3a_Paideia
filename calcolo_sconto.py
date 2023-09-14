#Chiedo le due variabili all'utente
n_prodotti=int(input("Inserisci quanti prodotti hai acquistato"))
costo_prodotto=int(input("Inserisci il costo del singolo prodotto"))

#faccio il calcolo per il totale
totale=costo_prodotto*n_prodotti

#guardo se devo applicare sconto
if(n_prodotti>10 or costo_prodotto>3):
  totale = totale - (totale*10)/100

print(f"Il totale è {totale} euro")