import re
import pandas as pd


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

date = []; time = []; sender = []; message = []
with open('output.txt') as fp:
    for row in fp.readlines():
        current_word = complete.match(row)
        if current_word is not None:
            date.append(current_word.group(1))
            time.append(current_word.group(2))
            sender.append(current_word.group(3))
            message.append(current_word.group(4).strip().replace('~', ' '))
        else:
            continue
        #print('Still processing the chat. Wait!')
    datetime = [dt[0] + ' ' + dt[1] for dt in zip(date, time)]
    datetime = pd.to_datetime(datetime)
    df = pd.DataFrame(zip(datetime, sender, message), columns=[
                            'datetime', 'sender', 'message'])
    df.to_csv('chat.csv', index=False, sep="~")
    fp.close()
