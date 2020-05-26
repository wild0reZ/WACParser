import test_parsing as tp

tp.parse_chat('real_chat.txt')
df = tp.makeDf()
tp.export_to_csv(df, 'chat.csv')