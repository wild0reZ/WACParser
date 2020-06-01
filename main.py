import wa_parser as prs
import wa_statistics as st
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--create-csv', nargs='+')
arg_parser.add_argument("-s", "--stats", help="Genera le statistiche della chat")
args = vars(arg_parser.parse_args())

if args['create_csv'] is not None:
    original_file, config = args['create_csv']
    output_file_name, extension = original_file.split('.')
    try:
        if 'txt' in extension and args['stats']:
            if config == 'android' or config == 'ios':
                if prs.parse_chat(original_file, config):
                    prs.make_csv(output_file_name, config)
                    df = st.open_and_sanitize_df(args['stats']+'.csv')
                    st.analyze_day_messages(df)
                    st.analyze_sender_message(df)
                    st.analyze_most_used_words(df)
                    print('Operazione completata. Ho creato il file csv e generato le statistiche.')
                else:
                    print('Sistema operativo non riconosciuto.')
        elif 'txt' in extension:
            if config == 'android' or config == 'ios':
                if prs.parse_chat(original_file, config):
                    prs.make_csv(output_file_name, config)
                    print('Operazione completata. Ho creato il file csv.')
                else:
                    print('Sistema operativo non riconosciuto.')
    except:
        print('Qualcosa è andato storto. Chat non riconosciuta.')
else:
    if args['stats']:
        df = st.open_and_sanitize_df(args['stats']+'.csv')
        st.analyze_day_messages(df)
        st.analyze_sender_message(df)
        st.analyze_most_used_words(df)
        print('Operazione completata. Ho generato le statistiche del file', args['stats']+'.csv')
    else:
        print('Formato del file non riconosciuto. Assicurati che sia .txt')
