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

# Uso
> python3 main.py -h **Help message**
Ci sono due argomenti obligatori:
- -f/--file per specificare il file della chat
- -c/--config specificare se la chat è stata esportata da android o ios

> python3 main.py -f nome_chat.txt -c android/ios

La chat (per ora) deve essere messa all'interno della cartella del parser.

Lo script crea un file chimato out_android.txt/out_ios.txt. Qesto è necessario ad aggiungere alcune "componenti"
alla chat originale altrimenti il parser non funziona.

In fine viene creato un file .csv contenente tre campi:
- datetime, contenente data e ora nel formato YYYY/MM/dd HH:mm;
- sender, persona che ha inviato il messaggio;
- message, il messaggio.

# Avvertenza
Il codice è ottimizzato male.
Questa versione è (probabilmente) un'alpha. Manca la gestione degli errori e devo ridurre il codice.
