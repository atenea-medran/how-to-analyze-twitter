import pandas as pd
import glob
import questionary
import os
import unidecode as ud
import re

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None

# crea lista de archivos del directorio donde está
files = os.listdir(".")

# extrae los archivos que termina en .txt
txts = [file for file in files if ".txt" in file]
if len(txts) == 0:
    print("No hay archivos txt en este directorio")
    exit()

# toma el archivo principal entre los txt
main_file = questionary.rawselect(
    "Cuál es el archivo principal?",
    choices=txts,
).ask()

print('Cargando archivo...')
ht = pd.read_csv(main_file,sep='\t',on_bad_lines='skip')
print('Número de tweets:',len(ht))

print('Creando archivo de grafo...')


ht['hashtags'] = ht['text'].apply(lambda x: re.findall(r"#(\w+)", x))
hashtag_list = ht['hashtags'].tolist()
ht_con_tildes = []
for listed in hashtag_list:
    for ht2 in listed:
        ht_con_tildes.append(ht2)
hashtag_list_separated = []
for ht2 in ht_con_tildes:
    ht2 = ud.unidecode(ht2)
    hashtag_list_separated.append(ht2)


ht_list_df = pd.DataFrame (hashtag_list_separated, columns = ['Label']) 
ht_list_df['Label'] = ht_list_df['Label'].str.lower()

nodes_gdf = ht_list_df.value_counts().to_frame().reset_index().reset_index()

filter_question = input('¿Filtrar hashtags por número de apariciones? y/n: ')
if filter_question == 'y':
    number = input('Mantener hashtags con más de __ apariciones. Inserte número: ')
    nodes_gdf = nodes_gdf[nodes_gdf[0] >= int(number)]
    filtered_list = nodes_gdf['Label'].tolist()

nodes_gdf.columns = [0,1,2]
nodes_gdf_first_row = {0: ['nodedef>name VARCHAR'],
        1: ['label VARCHAR'],
        2: ['Links INT']}
nodes_gdf_first_row_df = pd.DataFrame(nodes_gdf_first_row)
nodes_gdf = pd.concat([nodes_gdf_first_row_df,nodes_gdf],axis=0)

def build_edges(row):
    source = row['first HT']
    Labels = row['hashtags']
    for Label in Labels:
        edges_list.append([source,Label])

edges_list = []
ht.apply(build_edges, axis=1)
edges_df = pd.DataFrame (edges_list, columns = ['Source','Label'])

edges_df['Source'] = edges_df['Source'].apply(lambda x:ud.unidecode(x))
edges_df['Source'] = edges_df['Source'].str.lower()
edges_df['Label'] = edges_df['Label'].apply(lambda x:ud.unidecode(x))
edges_df['Label'] = edges_df['Label'].str.lower()

edges_df = edges_df[edges_df['Source'] != edges_df['Label']]

if filter_question == 'y':
    edges_df = edges_df[edges_df['Source'].isin(filtered_list)]
    edges_df = edges_df[edges_df['Label'].isin(filtered_list)]

ids = ht_list_df.value_counts().to_frame().reset_index().reset_index()
ids = ids[['Label','index']]


edges_df = edges_df.merge(ids,how='left',on='Label')

edges_df = edges_df.rename(columns={'index':'Target'})
edges_df = edges_df.drop('Label',axis=1)

ids.columns = ['Source','index']

edges_df = edges_df.merge(ids,how='left',on='Source')
edges_df = edges_df.drop('Source',axis=1)
edges_df = edges_df.rename(columns={'index':'Source'})

edges_df = edges_df[['Source','Target']]
edges_df['Type'] = 'false'

edges_gdf = edges_df
edges_gdf.columns = [0,1,2]

data = {0: ['edgedef>node1 VARCHAR'],
        1: ['node2 VARCHAR'],
        2: ['directed BOOLEAN']}
columns = pd.DataFrame(data)
edges_gdf = pd.concat([columns,edges_df],axis=0)

gdf = pd.concat([nodes_gdf,edges_gdf],axis=0)

gdf.to_csv('grafo.gdf',sep=',',index=False,header=False)

print('Archivo de grafo creado con éxito')
