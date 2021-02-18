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

def createProyectosDeLey():
  cur = con.cursor()
  cur.execute('''
  DROP TABLE IF EXISTS de.proyectos_ley_congreso;
  CREATE TABLE IF NOT EXISTS  de.proyectos_ley_congreso (
    id_tmp character varying,
    periodo character varying,
    legislatura character varying,
    fecha_presentacion character varying,
    numero character varying,
    proponente character varying,
    grupo_parlamentario character varying,
    titulo character varying,
    sumilla character varying,
    autores character varying,
    adherentes character varying,
    seguimiento character varying,
    iniciativa_agrupadas character varying,
    numero_simple character varying,
    fecha_ultima character varying,
    estado character varying,
    link_detalle character varying,
    periodo_inicio character varying,
    periodo_fin character varying,
    fecha_registro TIMESTAMP DEFAULT now() NOT NULL
  );
  ''')
  con.commit()

  print("Table expedientes_poder_jud created successfully")



# ----------------------------------------------------------------

def createProyectosDeLeyAutores():
  cur = con.cursor()
  cur.execute('''
  DROP TABLE IF EXISTS de.proyectos_ley_autores;
  CREATE TABLE IF NOT EXISTS de.proyectos_ley_autores (
    id_tmp character varying,
    nombre character varying
    );
  ''')
  con.commit()
  con.close()
  print("Table expedientes_poder_jud created successfully")

# ----------------------------------------------------------------



def cargaCsvToDB():
  cur = con.cursor()

  copy_sql = """
            COPY de.proyectos_ley_congreso FROM stdin WITH CSV HEADER
            DELIMITER as ','
            """
  # with open('../data20162021.csv', 'r') as f:
  # with open('../data20112016.csv', 'r') as f:
  with open('../data20062011.csv', 'r') as f:
      cur.copy_expert(sql=copy_sql, file=f)
      con.commit()
      con.close()
  print("Table proyectos_ley_congreso cargado successfully")

  con.close()


def cargaAutoresToDB():
  cur = con.cursor()

  copy_sql = """
            COPY de.proyectos_ley_autores FROM stdin WITH CSV HEADER
            DELIMITER as ','
            """
  # with open('../autores20162021.csv', 'r') as f:
  # with open('../autores20112016.csv', 'r') as f:
  with open('../autores20062011.csv', 'r') as f:
      cur.copy_expert(sql=copy_sql, file=f)
      con.commit()
      con.close()
  print("Table proyectos_ley_autores cargado successfully")

  con.close()

# createProyectosDeLey()
# createProyectosDeLeyAutores()

# cargaCsvToDB()
cargaAutoresToDB()