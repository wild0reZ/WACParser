import re
import pandas as pd

sanitized_file_list = []

regex_dict = {
    "ios": {
        "complete": re.compile(r'^\[(?P<date>\d{2}\/\d{2}\/\d{2}),\s+(?P<time>\d{2}\:\d{2}\:\d{2})\]\s+(?P<name>[^:]+):\s+(?P<messa_ge>[\s\S]+?(?=^\[|\+\d{2}|\Z))', re.M),
        "reg1": re.compile(r'^\[(\d{2}\/\d{2}\/\d{2}),\s(\d{2}:\d{2}:\d{2})\]\s+([A-Za-z0-9+]+):'),
        "reg2": re.compile(r'^\[(\d{2}\/\d{2}\/\d{2}),\s(\d{2}:\d{2}:\d{2})\]\s+(.+)')
    },
    "android": {
        "complete": re.compile(r'^(?P<date>\d{2}\/\d{2}\/\d{2}),\s+(?P<time>\d{2}\:\d{2})\s-\s(?P<name>[^:]+):\s+(?P<message>[\s\S]+?(?=^\[|\+\d{2}|\Z))', re.M),
        "reg1":  re.compile(r'^(\d{2}\/\d{2}\/\d{2}),\s(\d{2}:\d{2})\s-\s([A-Za-z0-9+\s]+):') ,
        "reg2": re.compile(r'^(\d{2}\/\d{2}\/\d{2}),\s(\d{2}:\d{2})\s-\s(.+)')
    }
}

def remove_unicode(row):
    return row.replace(u"\u202a", "").replace(u"\u200e", "").replace(u"\u202c", "").replace(u"\u202d", "")

def parse_chat(file_name, os):
    file_as_list = []
    r1 = regex_dict[os]["reg1"]
    r2 = regex_dict[os]["reg2"]
    try: 
        file_as_list = [remove_unicode(line.rstrip()) for line in open(file_name, encoding='utf8')]
    except:
        print('Impossibile aprire o tovare il file')

    try:
        for line in file_as_list:
            if r1.match(line):
                current_date = r1.match(line).group(1)
                current_time = r1.match(line).group(2)
                current_sender = r1.match(line).group(3)
                sanitized_file_list.append(line)
            else:
                if r2.match(line):
                    sanitized_file_list.append(line)
                else:
                    line = '[' + current_date + ', ' + current_time + ']' + ' ' + current_sender + ': ' + line
                    sanitized_file_list.append(line)
    except:
        if os == 'android':
            print('Attenzione! La chat è stata esportata da iOS. Riavvia lo script utilizzando la giusta configurazione')
        else:
            print('Attenzione! La chat è stata esportata da Android. Riavvia lo script utilizzando la giusta configurazione')
    return sanitized_file_list

def make_csv(nome_file_output, os):
    datetime = []; sender = []; message = []
    complete = regex_dict[os]["complete"]
    for row in sanitized_file_list[2:]:
        current_word = complete.match(row)
        if current_word is not None:
            datetime.append(current_word.group(1) + ' ' + current_word.group(2))
            sender.append(current_word.group(3))
            message.append(current_word.group(4).strip().replace('~', ' '))
        else:
            continue
    df = pd.DataFrame(zip(datetime, sender, message), columns=['datetime', 'sender', 'message'])
    df.to_csv(nome_file_output+'.csv', index=False, sep="~")