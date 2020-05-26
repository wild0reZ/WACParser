import android_parser as ap

ap.parse_chat('android_chat.txt')
df = ap.makeDf()
ap.export_to_csv(df, 'chat_android.csv')
