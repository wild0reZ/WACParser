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

Per generare solamente il file csv bisogna utilizzare:
> python3 main.py --create-csv nome_file.txt [ios|android]

Per generare anche le statistiche bisogna aggiungere il flag **-s**
> python3 main.py --create-csv nome_file.txt [ios|android] -s nome_csv

In entrambi i casi il file .csv generato avrà lo stesso nome del file originale.

Altrimenti è possibile generare le statistiche
> python3 main.py -s nome_csv (senza specificare l'estensione)

La chat (per ora) deve essere messa all'interno della cartella del parser.

Il file .csv contiene tre colonne:
- datetime, contenente data e ora nel formato dd/MM/YYYY HH:mm:(ss se estratta da iOS);
- sender, persona che ha inviato il messaggio;
- message, il messaggio.

# Avvertenza
Il codice è ottimizzato male.
Questa versione è (probabilmente) un'alpha. Manca la gestione degli errori e devo ridurre il codice.

Inoltre c'è la possibilità che alcune linee, data la sanitizzazione della chat di partenza, non contengano dei messaggi.
