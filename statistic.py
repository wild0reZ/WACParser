import pandas as pd
import matplotlib.pyplot as plt

def open_and_sanitize_df(file_name):
    df = pd.read_csv(file_name, delimiter='~')
    df.dropna(axis=0, how='any', inplace=True)
    df['datetime'] = pd.to_datetime(df['datetime'], dayfirst=True)
    return df

def analyze_day_messages(df):
    new_df = df.copy()
    new_df = new_df.groupby(new_df['datetime'].dt.date).count()
    new_df.index.name = 'data'
    new_df.reset_index(inplace=True)
    new_df = new_df.drop(['datetime', 'sender'], axis=1)
    return new_df.apply(tuple)

def graph_day_messages(t):
    data, messaggi = t
    plt.figure(figsize=(20,10))
    plt.plot(data,messaggi)
    plt.xlabel('Data')
    plt.xticks(rotation='vertical')
    plt.ylabel('Numero Messaggi')
    plt.title('Numero messaggi al giorno')
    plt.savefig('frequenza_messaggi.png', dpi=100)
