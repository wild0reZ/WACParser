# WACParser

WhatsApp Chat Parser.

# Formato della Chat
Il formato iOS dei messaggi è il seguente:
**[data, ora] nome: messaggio**

Il formato android dei messaggi è il seguente:
**data, ora - nome: messaggio**

# Librerie
Ci sono due dipendenze da soddisfare: **pandas** e **matplotlib**
> pip3 install pandas matplotlib

Per una guida più dettagliata su come installare pandas clicca [qui](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html).

Per una guida più dettagliata su come installare matplotlib clicca [qui](https://matplotlib.org/users/installing.html).

# Utilizzo
> python3 main.py -h **Help message**
Il parser può essere utilizzato in due modi:
1. Generare un file in formato .csv;
2. Oltre alla generazione del file in formato .csv anche la creazione di immagini che rappresentano le statistiche della chat.
  - Al momento le statistiche generate comprondono:
    1. Numero di messaggi della singola persona;
    2. Frequenza di messaggi giornaliera;
    3. Top 10 delle parole più utilizzate. (Nella cartella c'è un file di testo contenente le stopwords più utilizzate. Dato che è difficile rimuoverle tutte, c'è la possibilità che nelle parole utilizzate più di frequente compaia una stopword. In questo caso basta aggiungere la parola al file di testo.)

Per generare solamente il file csv bisogna utilizzare:
> python3 main.py --create-csv nome_file.txt [ios|android]

Per generare il file csv e le statistiche bisogna utilizzare:
> python3 main.py --stats nome_file.txt [ios|android]

In entrambi i casi il file .csv generato avrà lo stesso nome del file originale.

La chat (per ora) deve essere messa all'interno della cartella del parser.

Il file .csv generato conterrà tre colonne:
- **datetime**, contenente data e ora nel formato dd/MM/YYYY HH:mm:(ss se estratta da iOS);
- **sender**, persona che ha inviato il messaggio;
- **message**, il messaggio.

# Avvertenza
Il codice è ottimizzato male.
Questa versione è (probabilmente) un'alpha. Manca la gestione degli errori e devo ridurre il codice.

Inoltre c'è la possibilità che alcune linee, data la sanitizzazione della chat di partenza, non contengano dei messaggi.
