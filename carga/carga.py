import json
import requests
from bs4 import BeautifulSoup
import csv

import psycopg2
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv('../.env')

con = psycopg2.connect(database=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASS"), host=os.getenv("DB_HOST"), port="5432")
print(con)
print("Database opened successfully")

# cur = con.cursor()
# cur.execute('''
# DROP TABLE IF EXISTS de.proyectos_ley_congreso;
# CREATE TABLE IF NOT EXISTS  de.proyectos_ley_congreso (
#   periodo character varying,
#   legislatura character varying,
#   fecha_presentacion character varying,
#   numero character varying,
#   proponente character varying,
#   grupo_parlamentario character varying,
#   titulo character varying,
#   sumilla character varying,
#   autores character varying,
#   adherentes character varying,
#   seguimiento character varying,
#   iniciativa_agrupadas character varying,
#   numero_simple character varying,
#   fecha_ultima character varying,
#   estado character varying,
#   link_detalle character varying,
#   fecha_registro timestamp NOT NULL DEFAULT now(),
#   fecha_modificacion timestamp NULL
#   );
# ''')
# con.commit()

# print("Table expedientes_poder_jud created successfully")

# con.close()


# ----------------------------------------------------------------

cur = con.cursor()

with open(f'../dataTotal2.json', 'r', encoding='utf-8')as outFile:
  doc = outFile.read()
  # print(doc)
  docString = json.loads(doc)

  count = 0
  # print(docString)
  cur.execute("TRUNCATE de.proyectos_ley_congreso")

  for row in docString:
    if row:
      cur.execute("INSERT INTO de.proyectos_ley_congreso( \
        periodo, \
        legislatura, \
        fecha_presentacion, \
        numero, \
        proponente, \
        grupo_parlamentario, \
        titulo, \
        sumilla, \
        autores, \
        adherentes, \
        seguimiento, \
        iniciativa_agrupadas, \
        numero_simple, \
        fecha_ultima, \
        estado, \
        link_detalle \
        )\
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,  %s, %s, %s, %s, %s, %s)", (
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
        row[15]
        ))
      count+=1
      print(row)
      print("insert row ",count," success!")
      if count == 1000 or count == 2000 or count == 3000 or count == 4000 or count == 5000 or count == 6000:
        con.commit()

  con.commit()
print("Table proyectos_ley_congreso cargado successfully")

con.close()

