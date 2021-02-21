
import csv
import json
import datetime
import time
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(today)

def convertToCSV():
  data20162021 = "data20162021"
  data20112016 = "data20112016"
  data20062011 = "data20062011"
  data20012006 = "data20012006"
  data20002001 = "data20002001"
  data19952000 = "data19952000"

  with open(f'{data19952000}.json', 'r', encoding='utf-8') as outFile:
    doc = outFile.read()
    
    docString = json.loads(doc)

  with open(f'{data19952000}.csv', mode='w') as data:
    writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(["id_tmp","periodo","legislatura","fecha_presentacion","numero",
    "proponente","grupo_parlamentario","titulo","sumilla",
    "autores","adherentes","seguimiento","iniciativa_agrupadas","numero_simple",
    "fecha_ultima","estado","link_detalle","periodo_inicio","periodo_fin","fecha_registro"])
    for row in docString:
      writer.writerow([ 
            "19952000"+row[12],
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            row[8],
            row[9],
            row[10],
            row[11],
            row[12],
            row[13],
            row[14],
            row[15],
            "1995",
            "2000",
            today
            ])




def convertAutoresToCSV():

  data20162021 = "data20162021"
  data20112016 = "data20112016"
  data20062011 = "data20062011"
  data20012006 = "data20012006"
  data20002001 = "data20002001"
  data19952000 = "data19952000"

  with open(f'data19952000.json', 'r', encoding='utf-8') as outFile:

    doc = outFile.read()
    docString = json.loads(doc)

  with open(f'autores19952000.csv', mode='w') as data:
    writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(["id_tmp","nombre"])
    for row in docString:
      if row:
        autores = row[8].split(",")
        if autores:
          for autor in autores:
            writer.writerow(["19952000"+row[12],autor])


  print("Table autores 19952000 cargado successfully")



convertToCSV()

convertAutoresToCSV()