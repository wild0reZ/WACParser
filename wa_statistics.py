import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

with open('stopwords.txt') as sw:
    stopwords = sw.read().replace('\n', ' ').split(' ')

def open_and_sanitize_df(file_name):
    df = pd.read_csv(file_name, delimiter='~')
    df.dropna(axis=0, how='any', inplace=True)
    df['datetime'] = pd.to_datetime(df['datetime'], dayfirst=True)
    return df

#========= Numero di Messaggi al Giorno
def analyze_day_messages(df):
    new_df = df.copy()
    new_df = new_df.groupby(new_df['datetime'].dt.date).count()
    new_df.index.name = 'data'
    new_df.reset_index(inplace=True)
    new_df = new_df.drop(['datetime', 'sender'], axis=1)
    t = new_df.apply(tuple)
    data, messaggi = t
    plt.figure(figsize=(20,10))
    plt.plot(data,messaggi)
    plt.xlabel('Data')
    if len(data) <= 100:
        data_list = [data[x] for x in range(0, len(data))]
    else:
        data_list = [data[x] for x in range(0, len(data), 10)]
    plt.xticks(data_list, rotation='vertical')
    plt.ylabel('Numero Messaggi')
    plt.title('Numero messaggi al giorno')
    plt.savefig('frequenza_messaggi_giorno.png', dpi=100)

#========= Numero di Messaggi per Persona 
def analyze_sender_message(df):
    new_df = df.copy()
    new_df = df.groupby('sender')['message'].count().to_frame()
    new_df = new_df.rename(columns={'message':'number_of_messages'})
    new_df = new_df.reset_index()
    t = new_df[['sender', 'number_of_messages']].apply(tuple)
    sender, n_message = t
    plt.figure(figsize=(20,10))
    plt.barh(sender, n_message)
    for index, value in enumerate(n_message):
        plt.text(value, index, str(value))
    plt.xlabel('Numero di Messaggi')
    plt.ylabel('Persona')
    plt.title('Numero di Messaggi per Persona')
    plt.savefig('frequenza_messaggi_persona.png', dpi=100)

#============= Top 10 parole più utilizzate
def analyze_most_used_words(df):
    a = df.copy() # Copio il DataFrame
    l = list(" ".join(a['message']).lower().strip().split()) # Joino tutti i messaggi in un'unica lista
    l = [word for word in l if not word in stopwords]
    top_10 = Counter(l).most_common(10) # conto le parole
    word = []; counter = []
    for t in top_10:
        word.append(t[0])
        counter.append(t[1])
    word.reverse()
    counter.reverse()
    plt.figure(figsize=(20,10))
    plt.barh(word, counter)
    for index, value in enumerate(counter):
        plt.text(value, index, str(value))
    plt.xlabel('Numero di Occorrenze', fontsize=15)
    plt.ylabel('Parola', fontsize=15)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.title('Occorrenze per Parola')
    plt.savefig('Occorrenze_parola.png', transparent=False)

sw.close()
