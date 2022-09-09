# Pedicini-s-Pizza
  L'esercizio in questione è utile a rappresentare l'impiego della logica fuzzy in un problema di vita reale.
  
# Il problema
  Si ha la necessità di calcolare la mancia da dare al cameriere basandosi sulla qualità del servizio e sulla qualità del cibo servito.
# La soluzione
  Il problema è facilmente risolvibile attraverso la logica fuzzy, in particolare la libreria Simpful: una libreria di python per l'integrazione della logica fuzzy. Aggiunge l'integrazione di Mamdani e Sugeno,  permettendo il parsing di regole fuzzy complesse che coinvolgono operatori AND, OR e NOT.
  In particolare, è stato usato Mamdani, un fuzzy inference system intuitivo, efficiente e capace di integrare parole del linguaggio comune.
  
# Il codice 
  Il programma è diviso in diverse sezioni. Sicuramente la più interessante è la prima, relativa alla libreria simpful:
  
  <p align="center">
  <img src="https://user-images.githubusercontent.com/107196231/189175379-99e02f8e-22ad-4928-b3eb-f3460124c633.png">
</p>

  In particolare, la sezione relativa alle regole che le variabili devono seguire è davvero interessante:
  <p align="center">
  <img src="https://user-images.githubusercontent.com/107196231/189176706-ff5e5677-f5b1-46f3-831e-38fea3c6dcdb.png">
</p>

È infatti proprio questo il cuore del programma: grazie a queste regole possiamo definire il valore della mancia attraverso **AND**, **OR** e **NOT**:
## Regola 1
  La regola 1 è la seguente: 
  <p align="center">
  <img src="https://user-images.githubusercontent.com/107196231/189180243-9c8597ac-bc13-43b4-88b5-375b91bd12a8.png">
</p>
  Il funzionamento è piuttosto semplice, in quanto Mamdani permette l'impiego di termini molto vicini al linguaggio umano.
  
  La regola 1 riporta: **SE** la qualità del cibo è scarsa **OPPURE** la qualità del servizio è scarsa **ALLORA** la mancia sarà bassa.

## Regola 2
  La regola 2 è la seguente: 
  <p align="center">
  <img src="https://user-images.githubusercontent.com/107196231/189180342-5ad79ac0-a5ef-46a5-9604-a8009a46f33e.png">
</p>
  La regola 2 riporta: SE la qualità del cibo è mediocre ALLORA la mancia sarà media.

## Regola 3
  La regola 3 è la seguente: 
  <p align="center">
  <img src="https://user-images.githubusercontent.com/107196231/189180417-7133190a-8e3c-4465-835c-64cc19cc48ed.png">
</p>
  La regola 3 riporta: SE la qualità del cibo è ottima OPPURE la qualità del servizio è ottima ALLORA la mancia sarà alta.

# Code Explanation

**FuzzySystem()** : creazione di un nuovo sistema fuzzy che potrà contenere variabili e regole.

**AutoTriangle(n_sets, terms,universe_of_discourse, verbose=False)** : crea una nuova variabile linguistica. Richiede almeno tre parametri:

1. n_sets - il numero di insiemi sfocati nei quali il dominio degli elementi deve essere suddiviso.
2. terms - lista di stringhe che contengono i termini da usare negli insiemi sfocati.
3. universe_of_discourse - una lista di due elementi che specificano il minimo e il massimo valore del dominio.

**add_linguistic_variable(name, LV, verbose=False)** : aggiunge una variabile linguistica al sistema fuzzy. Richiede almeno 2 parametri:

1. name - stringa che contiene il nome della variabile linguistica.
2. LV - oggetto variabile linguistica da aggiungere al sistema fuzzy. 

**TriangleFuzzySet(a, b, c, term)** : crea un insieme sfocato triangolare. Richiede almeno 4 parametri: 

1. a - coordinate del dominio del vertice superiore sinistro.
2. b - coordinate del dominio del vertice superiore.
3. c - coordinate del dominio del vertice superiore destro.
4. term - stringa che rappresenta il termine da associare all'insieme sfocato.

**add_rules(rules, verbose=False)** : aggiunge le regole fuzzy al sistema fuzzy. Richiede almeno 1 parametro:

1. rules - lista delle regole da aggiungere. Devono essere specificate come stringhe, rispettando la sintassi di Simpful.

**set_variable(name,value, verbose=False)** : Assegna il valore numerico ad una variabile linguistica. Richiede almeno 2 parametri:

1. name - nome della variabile a cui assegnare il valore.
2. value - valore numerico da assegnare.

**inference()** : esegue l'inferenza fuzzy di Mamdani.

# Diritti d'autore
  Spolaor S., Fuchs C., Cazzaniga P., Kaymak U., Besozzi D., Nobile M.S.: Simpful: a user-friendly Python library for fuzzy logic, International Journal of Computational Intelligence Systems, 13(1):1687–1698, 2020
