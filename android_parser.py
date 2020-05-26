import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def remove_unicode(row):
    return row.replace(u"\u202a", "").replace(u"\u200e", "").replace(u"\u202c", "")

def parse_chat(file_name):
    alist = [remove_unicode(line.rstrip()) for line in open(file_name)]
    reg1 = re.compile(r'^(\d{2}\/\d{2}\/\d{2}),\s(\d{2}:\d{2})\s-\s([A-Za-z0-9+\s]+):')
    reg2 = re.compile(r'^(\d{2}\/\d{2}\/\d{2}),\s(\d{2}:\d{2})\s-\s(.+)')
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
                line = current_date + ', ' + current_time + ' - ' + current_sender + ': ' + line
                final_list.append(line)

    with open('output.txt', 'w') as out:
        for line in final_list:
            out.write("%s\n" % line)
        out.close()

def makeDf():
    complete = re.compile(r'^(?P<date>\d{2}\/\d{2}\/\d{2}),\s+(?P<time>\d{2}\:\d{2})\s-\s(?P<name>[^:]+):\s+(?P<message>[\s\S]+?(?=^\[|\+\d{2}|\Z))', re.M)
    datetime = []; sender = []; message = []
    with open('output.txt') as fp:
        for row in fp.readlines():
            current_word = complete.match(row)
            if current_word is not None:
                datetime.append(current_word.group(1) + ' ' + current_word.group(2))
                sender.append(current_word.group(3))
                message.append(current_word.group(4).strip().replace('~', ' '))
            else:
                continue
        fp.close()
    df = pd.DataFrame(zip(datetime, sender, message), columns=['datetime', 'sender', 'message'])
    bool_series = pd.notnull(df['message'])
    df = df[bool_series]
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

def export_to_csv(df, file_name):
    df.to_csv(file_name, index=False, sep="~")