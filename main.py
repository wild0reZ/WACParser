import parser as prs
import statistic as st
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--create-csv', nargs='+')
arg_parser.add_argument("-s", "--stats", action='store_true', help="Genera le statistiche della chat")
args = vars(arg_parser.parse_args())

original_file, config = args['create_csv']
output_file_name = original_file.split('.')[0]

if '.txt' in original_file and args['stats']:
    if config == 'android' or config == 'ios':
        if prs.parse_chat(original_file, config):
            prs.make_csv(output_file_name, config)
            df = st.open_and_sanitize_df(output_file_name+'.csv')
            t = st.analyze_day_messages(df)
            st.graph_day_messages(t)
            t1 = st.analyze_sender_message(df)
            st.graph_sender_message(t1)
    else:
        print('Sistema operativo non riconosciuto.')
elif '.txt' in original_file:
    if config == 'android' or config == 'ios':
        if prs.parse_chat(original_file, config):
            prs.make_csv(output_file_name, config)
    else:
        print('Sistema operativo non riconosciuto.')
else:
    print('Formato del file non riconosciuto. Assicurati che sia .txt')
