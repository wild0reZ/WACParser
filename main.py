import parser as prs
import statistic as st
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-f", "--file", required=True, help="Nome del file chat")
arg_parser.add_argument("-c", "--config",   required=True, help="Specificare se la chat è stata esportata da WhatsApp per Android o iOS")
arg_parser.add_argument("-o", "--output", required=True, help="Nome dell'output")
arg_parser.add_argument("-s", "--stats", action='store_true', help="Genera le statistiche della chat")
args = vars(arg_parser.parse_args())


if args['file']:
    if args['config'] == 'android' or args['config'] == 'ios':
        if prs.parse_chat(args['file'], args['config']):
            prs.make_csv(args['output'], args['config'])
    else:
        print('Inserisci un SO tra android e ios')
else:
    print('Controlla che il nome del file sia giusto')

if args['stats']:
    df = st.open_and_sanitize_df(args['output']+'.csv')
    t = st.analyze_day_messages(df)
    st.graph_day_messages(t)