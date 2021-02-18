
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

  with open(f'{data20062011}.json', 'r', encoding='utf-8') as outFile:
    # read as text
    doc = outFile.read()
    
    # convert to json to manipulate
    docString = json.loads(doc)
    # print(docString[0])

  with open(f'{data20062011}.csv', mode='w') as data:
    writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(["id_tmp","periodo","legislatura","fecha_presentacion","numero",
    "proponente","grupo_parlamentario","titulo","sumilla",
    "autores","adherentes","seguimiento","iniciativa_agrupadas","numero_simple",
    "fecha_ultima","estado","link_detalle","periodo_inicio","periodo_fin","fecha_registro"])
    for row in docString:
      writer.writerow([ 
            "20062011"+row[12],
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
            "2006",
            "2011",
            today
            ])




def convertAutoresToCSV():

  data20162021 = "data20162021"
  data20112016 = "data20112016"
  data20062011 = "data20062011"

  with open(f'data20062011.json', 'r', encoding='utf-8') as outFile:

    doc = outFile.read()
    docString = json.loads(doc)

  with open(f'autores20062011.csv', mode='w') as data:
    writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(["id_tmp","nombre"])
    for row in docString:
      if row:
        autores = row[8].split(",")
        if autores:
          for autor in autores:
            writer.writerow(["20062011"+row[12],autor])


  print("Table autores20162021 cargado successfully")



# ['Periodo de Gobierno 2016 - 2021.', 'Tercera Legislatura Ordinaria 2020', '02/05/2021', '07057/2020-PE ', 'Poder Ejecutivo', 'vacio', 'LEY DE SANEAMIENTO DEL LÍMITE ENTRE LOS DEPARTAMENTOS DE LAMBAYEQUE Y PIURA  ', ' Propone Ley de Saneamiento entre los departamentos de Lambayeque y Piura. ',
#  ' ', 
#  '', '  ', '', 
#  '07057', '', 'Presentado', 'http://www2.congreso.gob.pe/sicr/tradocestproc/Expvirt_2011.nsf/visbusqptramdoc1621/07057?opendocument']
# ['Periodo de Gobierno 2006- 2011.', '', '', '00001/2006-CR ', 'Congreso', 'Nacionalista Unión por el Perú', 'ELECCIONES:REGIONALES L.27683/VIGENCIA ART.14º DE LA LEY DE...', 'Propone precisar que el literal b) del artículo 14º de la Ley Nº 27683,  Ley de Elecciones Regionales, no ha sido derogado por la reforma del artículo 191º de la Constitución Política del Estado efectuada por la Ley Nº 28607, referente a que se mantiene en vigor, el impedimento de los Presidentes y Vicepresidentes Regionales de postular a la Presidencia, Vice-Presidencia ó como miembro del Consejo Regional, si no han renunciado por lo menos 120 días antes de la fecha de elección.', 
# ' Reymundo Mercado  Edgard Cornelio,Anaya Oropeza  José Oriol,León Zapata  Antonio,Gutierrez Cueva  Alvaro Gonzalo,Espinoza Ramos  Eduardo,Escudero Casquino  Francisco Alberto,Estrada Choque  Aldo Vladimiro,Cánepa la Cotera  Carlos Alberto ', 
# '', ' 07/08/2006 Dispensado del Trámite de Comisión       - Ac. N° 06-2006-2007/JUNTA PORTAVOCES-CR.-En Agenda: 8.08.06.\n10/08/2006 Orden del Día\n22/08/2006 Retirado al archivo       - Al Archivo 01-03-10 (14 folios)/A ped. Sr. Gutiérrez Cueva ', '', 
# '00001', '', 'Presentado', 'http://www2.congreso.gob.pe/sicr/tradocestproc/TraDoc_expdig_2006.nsf/5C26E09BB2A7CFDA052574AC005DA5B7/00001?opendocument']

convertToCSV()

# convertAutoresToCSV()