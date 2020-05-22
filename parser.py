import re
import pandas as pd

class Chat:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def remove_unicode(row):
        return row.replace(u"\u202a", "").replace(u"\u200e", "").replace(u"\u202c", "")

    # Ritorna un'istanza del file
    def file_magic(self):
        try:
            with open(self.path) as f:
                lines = f.read()
            with open('chat.out', 'w') as out:
                for line in lines:
                    line = self.remove_unicode(line)
                    out.write(line)
        except FileNotFoundError:
            print("Errore nell'apertura del file. Controlla se il path e/o il nome del file sono giusti.")

