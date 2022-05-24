import pandas as pd
import os



#Odczytywanie wszystkich plików txt w folderze'

def file_reader():
    kolumny =['Nazwa', 'GR', 'Szt', 'Ciec.','NAN']
    for filename in os.listdir():
        if filename.endswith('.txt'):
            df = pd.read_csv(filename,names=kolumny)
    
            setNazwa = set(df['Nazwa'])
            sN = setNazwa
            diki = {i:0 for i in sN}
    
            for i in df['Nazwa']:
                diki[i]+=1
            print(filename)      
            for i in diki:
                print(i,diki[i],sep='>')
            print('RAZEM: ',sum(diki.values()))
    

file_reader()
