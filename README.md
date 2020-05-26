# WACParser

WhatsApp Chat Parser.

# Formato della Chat
Il formato iOS dei messaggi è il seguente:
**[data, ora] nome: messaggio**

Il formato android dei messaggi è il seguente:
**data, ora - nome: messaggio**

# Librerie
L'unica dipendenza da soddisfare è **pandas**
> pip3 install pandas

Per una guida più dettagliata clicca [qui](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html).

# Uso
> python3 main.py -h **Help message**
Ci sono tre argomenti obligatori:
- -f/--file per specificare il file della chat
- -c/--config specificare se la chat è stata esportata da android o ios
- -o/--output serve per specificare il nome del file in formato csv

> python3 main.py -f nome_chat.txt -c [android|ios] -o nome_file_output

La chat (per ora) deve essere messa all'interno della cartella del parser.

Il file .csv contiene tre colonne:
- datetime, contenente data e ora nel formato YYYY/MM/dd HH:mm;
- sender, persona che ha inviato il messaggio;
- message, il messaggio.

# Avvertenza
Il codice è ottimizzato male.
Questa versione è (probabilmente) un'alpha. Manca la gestione degli errori e devo ridurre il codice.

Inoltre c'è la possibilità che alcune linee, data la sanitizzazione della chat di partenza, non contengano dei messaggi.
