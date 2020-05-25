import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def remove_unicode(row):
    return row.replace(u"\u202a", "").replace(u"\u200e", "").replace(u"\u202c", "")


alist = [remove_unicode(line.rstrip()) for line in open('real_chat.txt')]
reg1 = re.compile(
    r'^\[(\d{2}\/\d{2}\/\d{2}),\s(\d{2}:\d{2}:\d{2})\]\s+([A-Za-z0-9+]+):')
reg2 = re.compile(r'^\[(\d{2}\/\d{2}\/\d{2}),\s(\d{2}:\d{2}:\d{2})\]\s+(.+)')
complete = re.compile(
    r'^\[(?P<date>\d{2}\/\d{2}\/\d{2}),\s+(?P<time>\d{2}\:\d{2}\:\d{2})\]\s+(?P<name>[^:]+):\s+(?P<message>[\s\S]+?(?=^\[|\+\d{2}|\Z))', re.M)
final_list = []
for line in alist:
    if reg1.match(line):
        current_date = reg1.match(line).group(1)
        current_time = reg1.match(line).group(2)
        current_sender = reg1.match(line).group(3)
        final_list.append(line)
    else:
        if reg2.match(line):
            final_list.append(line)
        else:
            line = '[' + current_date + ', ' + current_time + ']' + \
                ' ' + current_sender + ': ' + line
            final_list.append(line)

with open('output.txt', 'w') as out:
    for line in final_list:
        out.write("%s\n" % line)
    out.close()

def makeDf():
    datetime = []
    sender = []
    message = []
    with open('output.txt') as fp:
        for row in fp.readlines():
            current_word = complete.match(row)
            if current_word is not None:
                datetime.append(current_word.group(
                    1) + ' ' + current_word.group(2))
                sender.append(current_word.group(3))
                message.append(current_word.group(4).strip().replace('~', ' '))
            else:
                continue
            #print('Still processing the chat. Wait!')
        datetime = pd.to_datetime(datetime)
        df = pd.DataFrame(zip(datetime, sender, message), columns=[
            'datetime', 'sender', 'message'])
        df.to_csv('chat.csv', index=False, sep="~")
        fp.close()
        return df


def generateGraph(csv_file):
    data = pd.read_csv(csv_file, delimiter="~")
    bool_series = pd.notnull(data['message'])
    data = data[bool_series]
    data['datetime'] = pd.to_datetime(data['datetime'])
    new_df = data.groupby('sender')['message'].count().to_frame()
    new_df = new_df.rename(columns={'message': 'number_of_messages'})
    new_df = new_df.reset_index()
    tuples = new_df[['sender', 'number_of_messages']].apply(tuple)
    a, b = tuples
    c = []
    for elem in a:
        c.append(elem.replace(u'\xa0', ''))
    fig, ax = plt.subplots()
    ax.barh(c,b)
    for index, value in enumerate(b):
        ax.text(value, index, str(value))
    ax.set_xlabel('Numero di Messaggi')
    ax.set_ylabel('Amici')
    plt.show()
    
generateGraph('chat.csv')