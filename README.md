# WACParser

WhatsApp Chat Analyzer.

# Preprocessing della Chat
Il formato (Italiano) dei messaggi è il seguente:
**[data, ora] nome: messaggio**

Potrebbero verificarsi diverse situazioni:
1. La chat contiene immagine/audio/video omessi. In questo caso la riga va saltata;
2. Un messaggio può contenere dei tag definiti attraverso '@'. I tag vanno eliminati;
3. La chat può contenere caratteri unicode che vanno rimossi.
  - \u202a \u200e \u202c
4. Un messaggio può essere diviso su più righe, ad esempio:
  - **[data, ora] nome: messaggio**
    **resto del messaggio**
    in questo caso devo rimuovere '\n' dalla riga che contiene il timestamp
    cosicché il messaggio prenda una sola riga. Altrimenti inserire il timestamp
    a tutte le righe che non lo hanno prendendo come riferimento l'ultimo salvato.

# Librerie
Per ora la divisione della riga del messaggio in 3 o 4 sottotipi viene fatta 
attraverso l'utilizzo del modulo **re** di python. Questo consente l'uso delle
espressioni regolari.

La creazione del file in formato csv è delegata al modulo **pandas**. Questo 
consente la creazione di un **Dataframe** che poi può essere salvato come file
in formato .csv.

# TODO
- [ ] Leggere la documentazione del modulo **re**
- [ ] Vedere se sono presenti altri caratteri unicode da rimuovere
- [ ] Come strutturo il parser? Classi?
- [ ] Capire come posso eliminare lo '\n' dai messaggi su più righe
- [ ] Capire come usare le regex per dividere il messaggio
- [ ] Capire che analisi voglio fare
