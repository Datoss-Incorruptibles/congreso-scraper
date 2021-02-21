import requests
from bs4 import BeautifulSoup

import csv
import json


from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry





def getCompleteData20112016():
  baseUrl = "http://www2.congreso.gob.pe"
  linkDetalleBase = "http://www2.congreso.gob.pe/sicr/tradocestproc/Expvirt_2011.nsf/visbusqptramdoc"

  with open(f'links20112016.json', 'r', encoding='utf-8') as outFile:
    doc = outFile.read()
    # print(doc)
    docString = json.loads(doc)
    totalData = []
    counter = 0
    for detalle in docString:
      urlEndpoint = detalle[0]
      # print(baseUrl + urlEndpoint) 
      p12 = requests.get(f'{baseUrl}{urlEndpoint}')

      s = BeautifulSoup(p12.text, 'lxml')

      table = s.find('table', attrs={'bordercolor':'#6583A0'})  
      rows = table.findAll('tr', attrs={'valign':'top'})
      valPeriodo = ""
      valLegislatura = ""
      valPresentacion = ""
      valNumero = ""
      valProponente = ""
      valPalamentario = ""
      valTitulo = ""
      valSumilla = ""
      valAutores = ""
      valAdherentes = ""
      valSeguimiento = ""
      valIniciativa = ""



      tmpArray = []

      for row in rows:
          title =  row.find('td', attrs={'width':'112'}).getText()

          if "Período" in title:
              valPeriodo =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valPeriodo}')

          elif "Legislatura" in title:
              valLegislatura =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valLegislatura}')
          
          elif "Presentación" in title:
              valPresentacion =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valPresentacion}')
          
          elif "Número" in title:
              valNumero =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valNumero}')
          
          elif "Proponente" in title:
              valProponente =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valProponente}')
          
          elif "Parlamentario" in title:
              valPalamentario =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valPalamentario}')

          elif "Título" in title:
              valTitulo =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valTitulo}')
          
          elif "Sumilla" in title:
              valSumilla =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valSumilla}')
          
          elif "Autores" in title:
              valAutores =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valAutores}')
        
          elif "Adherentes" in title:
              valAdherentes =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valAdherentes}')
        
          elif "Seguimiento" in title:
              valSeguimiento =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valSeguimiento}')

          elif "Iniciativas" in title:
              valIniciativa =  row.find('td', attrs={'width':'472'}).getText() if row.find('td', attrs={'width':'472'}).getText() else "vacio"
              # print(f'{title}:{valIniciativa}')
          else:
              print(f'no se encontro el title:{title}')


      tmpArray.append(valPeriodo)
      tmpArray.append(valLegislatura)
      tmpArray.append(valPresentacion)
      tmpArray.append(valNumero)
      tmpArray.append(valProponente)
      tmpArray.append(valPalamentario)
      tmpArray.append(valTitulo)
      tmpArray.append(valSumilla)
      tmpArray.append(valAutores)
      tmpArray.append(valAdherentes)
      tmpArray.append(valSeguimiento)
      tmpArray.append(valIniciativa)


      arrayOfNumero = detalle[1].split("/")
      # arrayOfNumero = valNumero.split("/")
      valueNumeroSimple = arrayOfNumero[0]
      valueFechaUltima = detalle[2]
      valueEstado = detalle[4]
      print(f'arrayOfNumero {arrayOfNumero}---- "estado:{valueEstado} ')

      if valueNumeroSimple.isnumeric():
        print(f' eres numero: {valueNumeroSimple}')
        valueLinkDetalle = f'{linkDetalleBase}/{valueNumeroSimple}?opendocument'
      else:
        print(f'NO eres numero: {valueNumeroSimple}')
        valueLinkDetalle = ""

      tmpArray.append(valueNumeroSimple)
      tmpArray.append(valueFechaUltima)
      tmpArray.append(valueEstado)
      tmpArray.append(valueLinkDetalle)
      counter = counter +1 
      print(f'{counter}')
      # print(tmpArray)
      totalData.append(tmpArray)

      # print(totalData)

      # print(f'{valPeriodo}--WW-{valLegislatura}-WW--{valPresentacion}--WW-{valNumero}--WW-{valProponente}-WW--{valPalamentario}-WW--{valTitulo}--WW-{valSumilla}--WW-{valAutores}---{valAdherentes}-WW--{valSeguimiento}--WW-{valIniciativa}')
  dataFinalJson = json.dumps(totalData)
  with open('data20112016.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)






def getCompleteData20062011():
  baseUrl = "http://www2.congreso.gob.pe"
  linkDetalleBase = "http://www2.congreso.gob.pe/sicr/tradocestproc/TraDoc_expdig_2006.nsf/5C26E09BB2A7CFDA052574AC005DA5B7"

  with open(f'links20062011.json', 'r', encoding='utf-8') as outFile:
    doc = outFile.read()
    # print(doc)
    docString = json.loads(doc)
    totalData = []
    counter = 0
    for detalle in docString:
      urlEndpoint = detalle[0]
      # print(baseUrl + urlEndpoint) 
      p12 = requests.get(f'{baseUrl}{urlEndpoint}')

      s = BeautifulSoup(p12.text, 'lxml')

      table = s.find('table', attrs={'bordercolor':'#6583A0'})  
      rows = table.findAll('tr', attrs={'valign':'top'})
      valPeriodo = ""
      valLegislatura = ""
      valPresentacion = ""
      valNumero = ""
      valProponente = ""
      valPalamentario = ""
      valTitulo = ""
      valSumilla = ""
      valAutores = ""
      valAdherentes = ""
      valSeguimiento = ""
      valIniciativa = ""



      tmpArray = []

      for row in rows:
          title =  row.find('td', attrs={'width':'20%'}).getText()

          if "Período" in title:
              valPeriodo =  row.find('td', attrs={'width':'27%'}).getText() if row.find('td', attrs={'width':'27%'}).getText() else "vacio"
              # print(f'{title}:{valPeriodo}')

          elif "Legislatura" in title:
              valLegislatura =  row.find('td', attrs={'width':'33%'}).getText() if row.find('td', attrs={'width':'33%'}).getText() else "vacio"
              # print(f'{title}:{valLegislatura}')
          
          elif "Presentación" in title:
              valPresentacion =  row.find('td', attrs={'width':'33%'}).getText() if row.find('td', attrs={'width':'33%'}).getText() else "vacio"
              # print(f'{title}:{valPresentacion}')
          
          elif "Número" in title:
              valNumero =  row.find('td', attrs={'width':'27%'}).getText() if row.find('td', attrs={'width':'27%'}).getText() else "vacio"
              # print(f'{title}:{valNumero}')
          
          elif "Proponente" in title:
              valProponente =  row.find('td', attrs={'width':'80%'}).getText() if row.find('td', attrs={'width':'80%'}).getText() else "vacio"
              # print(f'{title}:{valProponente}')
          
          elif "Parlamentario" in title:
              valPalamentario =  row.find('td', attrs={'width':'80%'}).getText() if row.find('td', attrs={'width':'80%'}).getText() else "vacio"
              # print(f'{title}:{valPalamentario}')

          elif "Título" in title:
              valTitulo =  row.find('td', attrs={'width':'80%'}).getText() if row.find('td', attrs={'width':'80%'}).getText() else "vacio"
              # print(f'{title}:{valTitulo}')
          
          elif "Sumilla" in title:
              valSumilla =  row.find('td', attrs={'width':'80%'}).getText() if row.find('td', attrs={'width':'80%'}).getText() else "vacio"
              # print(f'{title}:{valSumilla}')
          
          elif "Autores" in title:
              valAutores =  row.find('td', attrs={'width':'80%'}).getText() if row.find('td', attrs={'width':'80%'}).getText() else "vacio"
              # print(f'{title}:{valAutores}')
        
          elif "Adherentes" in title:
              valAdherentes =  ""
              # print(f'{title}:{valAdherentes}')
        
          elif "Seguimiento" in title:
              valSeguimiento =  row.find('td', attrs={'width':'80%'}).getText() if row.find('td', attrs={'width':'80%'}).getText() else "vacio"
              # print(f'{title}:{valSeguimiento}')

          elif "Iniciativas" in title:
              valIniciativa =  row.find('td', attrs={'width':'80%'}).getText() if row.find('td', attrs={'width':'80%'}).getText() else "vacio"
              # print(f'{title}:{valIniciativa}')
          else:
              print(f'no se encontro el title:{title}')


      tmpArray.append(valPeriodo)
      tmpArray.append(valLegislatura)
      tmpArray.append(valPresentacion)
      tmpArray.append(valNumero)
      tmpArray.append(valProponente)
      tmpArray.append(valPalamentario)
      tmpArray.append(valTitulo)
      tmpArray.append(valSumilla)
      tmpArray.append(valAutores)
      tmpArray.append(valAdherentes)
      tmpArray.append(valSeguimiento)
      tmpArray.append(valIniciativa)


      arrayOfNumero = detalle[1].split("/")
      # arrayOfNumero = valNumero.split("/")
      valueNumeroSimple = arrayOfNumero[0]
      valueFechaUltima = ""
      valueEstado = detalle[2]
      print(f'arrayOfNumero {arrayOfNumero}---- "estado:{valueEstado} ')

      if valueNumeroSimple.isnumeric():
        print(f' eres numero: {valueNumeroSimple}')
        valueLinkDetalle = f'{linkDetalleBase}/{valueNumeroSimple}?opendocument'
      else:
        print(f'NO eres numero: {valueNumeroSimple}')
        valueLinkDetalle = ""

      tmpArray.append(valueNumeroSimple)
      tmpArray.append(valueFechaUltima)
      tmpArray.append(valueEstado)
      tmpArray.append(valueLinkDetalle)
      counter = counter +1 
      print(f'{counter}')
      print(tmpArray)
      totalData.append(tmpArray)

      # print(f'{valPeriodo}--WW-{valLegislatura}-WW--{valPresentacion}--WW-{valNumero}--WW-{valProponente}-WW--{valPalamentario}-WW--{valTitulo}--WW-{valSumilla}--WW-{valAutores}---{valAdherentes}-WW--{valSeguimiento}--WW-{valIniciativa}')
  dataFinalJson = json.dumps(totalData)
  with open('data20062011.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)




def getCompleteData20012006():
  baseUrl = "http://www2.congreso.gob.pe"
  linkDetalleBase = "http://www2.congreso.gob.pe/sicr/tradocestproc/TraDoc_expdig_2001.nsf/ProyectosExpDigital"
                     
  with open(f'links20012006.json', 'r', encoding='utf-8') as outFile:
    doc = outFile.read()
    # print(doc)
    docString = json.loads(doc)
    totalData = []
    counter = 0
    for detalle in docString:
      try:
        urlEndpoint = detalle[0]
        agent = {"User-Agent":"Mozilla/5.0"}
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)   
        p12 = session.get(f'{baseUrl}{urlEndpoint}', headers=agent)
        # p12 = requests.get(f'{baseUrl}{urlEndpoint}')
      except:
        print("CRASH OBTENIENDO La url detallle ley")


      s = BeautifulSoup(p12.text, 'lxml')
      table = s.find('table', attrs={'bordercolor':'#6583A0'})  
      rows = table.findAll('tr', attrs={'valign':'top'})
      valPeriodo = ""
      valLegislatura = ""
      valPresentacion = ""
      valNumero = ""
      valProponente = ""
      valPalamentario = ""
      valTitulo = ""
      valSumilla = ""
      valAutores = ""
      valAdherentes = ""
      valSeguimiento = ""
      valIniciativa = ""



      tmpArray = []

      for row in rows:
          title =  row.find('td', attrs={'width':'112'}).getText()
          if not title:
            title =  row.find('td', attrs={'width':'113'}).getText()

          if "Período" in title:
              valPeriodo =  row.find('td', attrs={'width':'151'}).getText() if row.find('td', attrs={'width':'151'}).getText() else "vacio"
              # print(f'{title}:{valPeriodo}')

          elif "Legislatura" in title:
              valLegislatura =  row.find('td', attrs={'width':'181'}).getText() if row.find('td', attrs={'width':'181'}).getText() else "vacio"
              # print(f'{title}:{valLegislatura}')
          
          elif "Presentación" in title: 
              valPresentacion =  row.find('td', attrs={'width':'181'}).getText() if row.find('td', attrs={'width':'181'}).getText() else "vacio"
              # print(f'{title}:{valPresentacion}')
          
          elif "Número" in title:
              valNumero =  row.find('td', attrs={'width':'151'}).getText() if row.find('td', attrs={'width':'151'}).getText() else "vacio"
              # print(f'{title}:{valNumero}')
          
          elif "Proponente" in title:
              valProponente =  row.find('td', attrs={'width':'446'}).getText() if row.find('td', attrs={'width':'446'}).getText() else "vacio"
              # print(f'{title}:{valProponente}')
          
          elif "Parlamentario" in title:
              valPalamentario =  row.find('td', attrs={'width':'446'}).getText() if row.find('td', attrs={'width':'446'}).getText() else "vacio"
              # print(f'{title}:{valPalamentario}')

          elif "Título" in title:
              valTitulo =  row.find('td', attrs={'width':'446'}).getText() if row.find('td', attrs={'width':'446'}).getText() else "vacio"
              # print(f'{title}:{valTitulo}')
          
          elif "Sumilla" in title:
              valSumilla =  row.find('td', attrs={'width':'446'}).getText() if row.find('td', attrs={'width':'446'}).getText() else "vacio"
              # print(f'{title}:{valSumilla}')
          
          elif "Autores" in title:
              valAutores =  row.find('td', attrs={'width':'446'}).getText() if row.find('td', attrs={'width':'446'}).getText() else "vacio"
              # print(f'{title}:{valAutores}')
        
          elif "Adherentes" in title:
              valAdherentes =  row.find('td', attrs={'width':'446'}).getText() if row.find('td', attrs={'width':'446'}).getText() else "vacio"
              # print(f'{title}:{valAdherentes}')
        
          elif "Seguimiento" in title:
              valSeguimiento =  row.find('td', attrs={'width':'446'}).getText() if row.find('td', attrs={'width':'446'}).getText() else "vacio"
              # print(f'{title}:{valSeguimiento}')

          elif "Iniciativas" in title:
              valIniciativa =  row.find('td', attrs={'width':'446'}).getText() if row.find('td', attrs={'width':'446'}).getText() else "vacio"
              # print(f'{title}:{valIniciativa}')
          else:
              print(f'no se encontro el title:{title}')


      tmpArray.append(valPeriodo)
      tmpArray.append(valLegislatura)
      tmpArray.append(valPresentacion)
      tmpArray.append(valNumero)
      tmpArray.append(valProponente)
      tmpArray.append(valPalamentario)
      tmpArray.append(valTitulo)
      tmpArray.append(valSumilla)
      tmpArray.append(valAutores)
      tmpArray.append(valAdherentes)
      tmpArray.append(valSeguimiento)
      tmpArray.append(valIniciativa)


      arrayOfNumero = detalle[1].split("/")
      # arrayOfNumero = valNumero.split("/")
      valueNumeroSimple = arrayOfNumero[0]
      valueFechaUltima = detalle[2]
      valueEstado = detalle[4]
    #   print(f'arrayOfNumero {arrayOfNumero}---- "estado:{valueEstado} ')

      if valueNumeroSimple.isnumeric():
        print(f' eres numero: {valueNumeroSimple}')
        valueLinkDetalle = f'{linkDetalleBase}/{valueNumeroSimple}?opendocument'
      else:
        print(f'NO eres numero: {valueNumeroSimple}')
        valueLinkDetalle = ""

      tmpArray.append(valueNumeroSimple)
      tmpArray.append(valueFechaUltima)
      tmpArray.append(valueEstado)
      tmpArray.append(valueLinkDetalle)
      counter = counter +1 
      print(f'{counter}')
    #   print(tmpArray)
      totalData.append(tmpArray)

      # print(totalData)
      # print(f'{valPeriodo}--WW-{valLegislatura}-WW--{valPresentacion}--WW-{valNumero}--WW-{valProponente}-WW--{valPalamentario}-WW--{valTitulo}--WW-{valSumilla}--WW-{valAutores}---{valAdherentes}-WW--{valSeguimiento}--WW-{valIniciativa}')
      if counter == 1000 or counter == 5000 or counter == 10000 or counter == 15000:
        dataFinalJson = json.dumps(totalData)
        with open('data20012006.json', 'w') as file:  # Use file to refer to the file object
            file.write(dataFinalJson)

  dataFinalJson = json.dumps(totalData)
  with open('data20012006.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)



def getCompleteData20002001():
  baseUrl = "http://www2.congreso.gob.pe"
  linkDetalleBase = ""

  with open(f'links20002001.json', 'r', encoding='utf-8') as outFile:
    doc = outFile.read()
    # print(doc)
    docString = json.loads(doc)
    totalData = []
    counter = 0
    for detalle in docString:
      try:
        urlEndpoint = detalle[0]
        agent = {"User-Agent":"Mozilla/5.0"}
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)   
        p12 = session.get(f'{baseUrl}{urlEndpoint}', headers=agent)
        # p12 = requests.get(f'{baseUrl}{urlEndpoint}')
      except:
        print("CRASH OBTENIENDO La url detallle ley")


      s = BeautifulSoup(p12.text, 'lxml')
      table = s.find('table', attrs={'bordercolor':'#6583A0'})  
      rows = table.findAll('tr', attrs={'valign':'top'})
      valPeriodo = ""
      valLegislatura = ""
      valPresentacion = ""
      valNumero = ""
      valProponente = ""
      valPalamentario = ""
      valTitulo = ""
      valSumilla = ""
      valAutores = ""
      valAdherentes = ""
      valSeguimiento = ""
      valIniciativa = ""



      tmpArray = []

      for row in rows:
          title =  row.find('td', attrs={'width':'35%'}).getText()
          # if not title:
          #   title =  row.find('td', attrs={'width':'113'}).getText()

          if "Periodo" in title:
              valPeriodo =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valPeriodo}')

          elif "Legislatura" in title:
              valLegislatura =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valLegislatura}')
          
          elif "Presentación" in title: 
              valPresentacion =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valPresentacion}')
          
          elif "Número" in title:
              valNumero =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valNumero}')
          
          elif "Proponente" in title:
              valProponente =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valProponente}')
          
          elif "Parlamentario" in title:
              valPalamentario =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valPalamentario}')

          elif "Titulo" in title:
              valTitulo =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valTitulo}')
          
          elif "Sumilla" in title:
              valSumilla =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valSumilla}')
          
          elif "Autores" in title:
              valAutores =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valAutores}')
        
          elif "Adherentes" in title:
              valAdherentes =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valAdherentes}')
        
          elif "Seguimiento" in title:
              valSeguimiento =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valSeguimiento}')

          elif "Iniciativas" in title:
              valIniciativa =  row.find('td', attrs={'width':'65%'}).getText() if row.find('td', attrs={'width':'65%'}).getText() else "vacio"
              # print(f'{title}:{valIniciativa}')
          else:
              print(f'no se encontro el title:{title}')


      tmpArray.append(valPeriodo)
      tmpArray.append(valLegislatura)
      tmpArray.append(valPresentacion)
      tmpArray.append(valNumero)
      tmpArray.append(valProponente)
      tmpArray.append(valPalamentario)
      tmpArray.append(valTitulo)
      tmpArray.append(valSumilla)
      tmpArray.append(valAutores)
      tmpArray.append(valAdherentes)
      tmpArray.append(valSeguimiento)
      tmpArray.append(valIniciativa)


      arrayOfNumero = detalle[1].split("/")
      # arrayOfNumero = valNumero.split("/")
      valueNumeroSimple = arrayOfNumero[0]
      valueFechaUltima = detalle[2]
      valueEstado = detalle[4]
    #   print(f'arrayOfNumero {arrayOfNumero}---- "estado:{valueEstado} ')

      if valueNumeroSimple.isnumeric():
        print(f' eres numero: {valueNumeroSimple}')
        valueLinkDetalle = ''
      else:
        print(f'NO eres numero: {valueNumeroSimple}')
        valueLinkDetalle = ""

      tmpArray.append(valueNumeroSimple)
      tmpArray.append(valueFechaUltima)
      tmpArray.append(valueEstado)
      tmpArray.append(valueLinkDetalle)
      counter = counter +1 
      print(f'{counter}')
    #   print(tmpArray)
      totalData.append(tmpArray)

      # print(totalData)
      # print(f'{valPeriodo}--WW-{valLegislatura}-WW--{valPresentacion}--WW-{valNumero}--WW-{valProponente}-WW--{valPalamentario}-WW--{valTitulo}--WW-{valSumilla}--WW-{valAutores}---{valAdherentes}-WW--{valSeguimiento}--WW-{valIniciativa}')
      # if counter == 1000 or counter == 5000 or counter == 10000 or counter == 15000:
      #   dataFinalJson = json.dumps(totalData)
      #   with open('data20002001.json', 'w') as file:  # Use file to refer to the file object
      #       file.write(dataFinalJson)

  dataFinalJson = json.dumps(totalData)
  with open('data20002001.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)





def getCompleteData19952000():
  baseUrl = "http://www2.congreso.gob.pe"
  linkDetalleBase = ""

  with open(f'links19952000.json', 'r', encoding='utf-8') as outFile:
    doc = outFile.read()
    # print(doc)
    docString = json.loads(doc)
    totalData = []
    counter = 0
    for detalle in docString:
      try:
        urlEndpoint = detalle[0]
        agent = {"User-Agent":"Mozilla/5.0"}
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)   
        p12 = session.get(f'{baseUrl}{urlEndpoint}', headers=agent)
        # p12 = requests.get(f'{baseUrl}{urlEndpoint}')
      except:
        print("CRASH OBTENIENDO La url detallle ley")


      s = BeautifulSoup(p12.text, 'lxml')
      table = s.find('table', attrs={'width':'630'})  
      rows = table.findAll('tr', attrs={'valign':'top'})
      valPeriodo = ""
      valLegislatura = ""
      valPresentacion = ""
      valNumero = ""
      valProponente = ""
      valPalamentario = ""
      valTitulo = ""
      valSumilla = ""
      valAutores = ""
      valAdherentes = ""
      valSeguimiento = ""
      valIniciativa = ""

      tmpArray = []

      for row in rows:
          title =  row.find('td', attrs={'width':'23%'}).getText()
          # if not title:
          #   title =  row.find('td', attrs={'width':'113'}).getText()

          if "Periodo" in title:
              valPeriodo =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valPeriodo}')

          elif "Legislatura" in title:
              valLegislatura =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valLegislatura}')
          
          elif "Presentación" in title: 
              valPresentacion =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valPresentacion}')
          
          elif "Número" in title:
              valNumero =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valNumero}')
          
          elif "Proponente" in title:
              valProponente =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valProponente}')
          
          elif "Parlamentario" in title:
              valPalamentario =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valPalamentario}')

          elif "Titulo" in title:
              valTitulo =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valTitulo}')
          
          elif "Sumilla" in title:
              valSumilla =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valSumilla}')
          
          elif "Autores" in title:
              valAutores =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valAutores}')
        
          elif "Adherentes" in title:
              valAdherentes =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valAdherentes}')
        
          elif "Seguimiento" in title:
              valSeguimiento =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valSeguimiento}')

          elif "Iniciativas" in title:
              valIniciativa =  row.find('td', attrs={'width':'77%'}).getText() if row.find('td', attrs={'width':'77%'}).getText() else "vacio"
              # print(f'{title}:{valIniciativa}')
          else:
              print(f'no se encontro el title:{title}')


      tmpArray.append(valPeriodo)
      tmpArray.append(valLegislatura)
      tmpArray.append(valPresentacion)
      tmpArray.append(valNumero)
      tmpArray.append(valProponente)
      tmpArray.append(valPalamentario)
      tmpArray.append(valTitulo)
      tmpArray.append(valSumilla)
      tmpArray.append(valAutores)
      tmpArray.append(valAdherentes)
      tmpArray.append(valSeguimiento)
      tmpArray.append(valIniciativa)


      arrayOfNumero = detalle[1].split("/")
      # arrayOfNumero = valNumero.split("/")
      valueNumeroSimple = arrayOfNumero[0]
      valueFechaUltima = detalle[2]
      valueEstado = detalle[4]
    #   print(f'arrayOfNumero {arrayOfNumero}---- "estado:{valueEstado} ')

      if valueNumeroSimple.isnumeric():
        print(f'eres numero: {valueNumeroSimple}')
        valueLinkDetalle = ''
      else:
        print(f'NO eres numero: {valueNumeroSimple}')
        valueLinkDetalle = ""

      tmpArray.append(valueNumeroSimple)
      tmpArray.append(valueFechaUltima)
      tmpArray.append(valueEstado)
      tmpArray.append(valueLinkDetalle)
      counter = counter +1 
      print(f'{counter}')
    #   print(tmpArray)
      totalData.append(tmpArray)

      # print(totalData)
      # print(f'{valPeriodo}--WW-{valLegislatura}-WW--{valPresentacion}--WW-{valNumero}--WW-{valProponente}-WW--{valPalamentario}-WW--{valTitulo}--WW-{valSumilla}--WW-{valAutores}---{valAdherentes}-WW--{valSeguimiento}--WW-{valIniciativa}')
      # if counter == 1000 or counter == 5000 or counter == 10000 or counter == 15000:
      #   dataFinalJson = json.dumps(totalData)
      #   with open('data20002001.json', 'w') as file:  # Use file to refer to the file object
      #       file.write(dataFinalJson)

  dataFinalJson = json.dumps(totalData)
  with open('data19952000.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)






# getCompleteData20112016()
# getCompleteData20062011()
# getCompleteData20012006()
# getCompleteData20002001()
getCompleteData19952000()