import android_parser as ap
import ios_parser as ip
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True, help="Nome del file chat")
parser.add_argument("-c", "--config", required=True, help="Specificare se la chat è stata esportata da WhatsApp per Android o iOS")
args = vars(parser.parse_args())

if args['file']:
    if args['config'] == 'android':
        ap.parse_chat(args['file'])
        ap.make_csv()
        print('Done')
    elif args['config'] == 'ios':
        ip.parse_chat(args['file'])
        ip.make_csv()
        print('Done')
    else:
        print('Inserisci un SO tra android e ios')
else:
    print('Controlla che il nome del file sia giusto')