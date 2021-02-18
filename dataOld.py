import requests
from bs4 import BeautifulSoup

import csv
import json

def getLinks20112016():
  totalLeyes2011 = 5420
  paginacion = 1000
  llamadas = 6
  dataFinal = []

  totalLeyes2016 = "http://www.congreso.gob.pe/pley-2011-2016"
  pages = [1,1001,2001,3000,4000,5000]

  counter = 0
  counterVacio = 0 

  for iter in range(llamadas):
              
      url = f"http://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey2011.nsf/Local%20Por%20Numero?OpenView&Start={pages[iter]}"
      p12 = requests.get(url)
      s = BeautifulSoup(p12.text, 'lxml')
      secciones = s.findAll('tr', attrs={'valign':'top'})
      print(len(secciones))
      for seccion in secciones:
          arrayObjDetalle = []
          arrayOfData = seccion.findAll('font', attrs={'size':'2','face':'Verdana'})
          if arrayOfData == []:
              counterVacio= counterVacio+1
              print(f'Vacios count:{counterVacio}')
          else:

              tr = seccion.findAll('td')
              # print(tr)
              print(tr[0])

              link = tr[0].font.a.get('href')
              numero = tr[0].getText()
              fecha_ultima = tr[1].getText()
              fecha_presente = tr[2].getText()
              print(link)
              print(numero)
              print(fecha_ultima)
              print(fecha_presente)

              try:
                  estado = tr[3].getText()
              except IndexError:
                  estado = "vacio"

              try:
                  titulo_proyecto = tr[4].getText()
              except IndexError:
                  titulo_proyecto = "vacio"
              # print(f'{link} --- {fecha_ultima} --- {fecha_presente} --- {estado} ---{titulo_proyecto}')
              arrayObjDetalle.append(link)
              arrayObjDetalle.append(numero)
              arrayObjDetalle.append(fecha_ultima)
              arrayObjDetalle.append(fecha_presente)
              arrayObjDetalle.append(estado)
              arrayObjDetalle.append(titulo_proyecto)

              dataFinal.append(arrayObjDetalle)
              counter = counter+1
              print(f'NoVacio count:{counter}--numero:{numero}')


  dataFinalJson = json.dumps(dataFinal)
  with open('links20112016.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)

def getLinks20062011():
  totalLeyes2011 = 4908
  paginacion = 500
  llamadas = 10
  dataFinal = []

  totalLeyes2016 = "http://www.congreso.gob.pe/pley-2006-2011"
  pages = [1,501,1001,1501,2001,
          2501,3001,3501,4001,4501]

  counter = 0
  counterVacio = 0 

  for iter in range(llamadas):
      url = f"http://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey2006.nsf/Numeropa?OpenView&Start={pages[iter]}"
      p12 = requests.get(url)
      s = BeautifulSoup(p12.text, 'lxml')
      secciones = s.findAll('tr', attrs={'valign':'top'})
      print(len(secciones))
      for seccion in secciones:
          arrayObjDetalle = []
          arrayOfData = seccion.findAll('font', attrs={'size':'1','face':'Verdana'})
          if arrayOfData == []:
              counterVacio= counterVacio+1
              print(f'Vacios count:{counterVacio}')
          else:

              tr = seccion.findAll('td')
              # print(tr)
              print(tr[0])

              link = tr[0].font.a.get('href')
              numero = tr[0].getText()
              # fecha_ultima = tr[1].getText()
              fecha_presente = tr[2].getText()
              print(link)
              print(numero)
              # print(fecha_ultima)
              print(fecha_presente)

              try:
                  estado = tr[1].getText()
              except IndexError:
                  estado = "vacio"

              try:
                  titulo_proyecto = tr[4].getText()
              except IndexError:
                  titulo_proyecto = "vacio"
              # print(f'{link} --- {fecha_ultima} --- {fecha_presente} --- {estado} ---{titulo_proyecto}')
              arrayObjDetalle.append(link)
              arrayObjDetalle.append(numero)
              # arrayObjDetalle.append(fecha_ultima)
              arrayObjDetalle.append(estado)
              arrayObjDetalle.append(fecha_presente)
              arrayObjDetalle.append(titulo_proyecto)

              dataFinal.append(arrayObjDetalle)
              counter = counter+1
              print(f'NoVacio count:{counter}--numero:{numero}')


  dataFinalJson = json.dumps(dataFinal)
  with open('links20062011.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)




def getLinks20012006():
  totalLeyes2011 = 14843
  paginacion = 500
  llamadas = 30
  dataFinal = []

  totalLeyes2016 = "http://www.congreso.gob.pe/pley-2001-2006"
  pages = [1,501,1001,1501,2001,2501,3001,3501,
          4001,4501,5001,5501,6001,6501,7001,7501,
          8001,8501,9001,9501,10001,10501,11001,11501,
          12001,12501,13001,13501,14001,14501]

  counter = 0
  counterVacio = 0 

  for iter in range(llamadas):
              
      url = f"http://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey2001.nsf/Local%20Por%20Numero?OpenView&Start={pages[iter]}"
              
      p12 = requests.get(url)
      s = BeautifulSoup(p12.text, 'lxml')
      secciones = s.findAll('tr', attrs={'valign':'top'})
      print(len(secciones))
      for seccion in secciones:
          arrayObjDetalle = []
          arrayOfData = seccion.findAll('font', attrs={'size':'2','face':'Verdana'})
          print(arrayOfData,"arrayOfData")

          if arrayOfData == []:
              counterVacio= counterVacio+1
              print(f'Vacios count:{counterVacio}')
          else:
              tr = seccion.findAll('td')
              # print(tr)
              print(tr[0])
              link = tr[0].font.a.get('href')
              numero = tr[0].getText()
              fecha_ultima = tr[1].getText()
              fecha_presente = tr[2].getText()
              print(link)
              print(numero)
              print(fecha_ultima)
              print(fecha_presente)

              try:
                  estado = tr[3].getText()
              except IndexError:
                  estado = "vacio"

              try:
                  titulo_proyecto = tr[4].getText()
              except IndexError:
                  titulo_proyecto = "vacio"
              # print(f'{link} --- {fecha_ultima} --- {fecha_presente} --- {estado} ---{titulo_proyecto}')
              arrayObjDetalle.append(link)
              arrayObjDetalle.append(numero)
              arrayObjDetalle.append(fecha_ultima)
              arrayObjDetalle.append(fecha_presente)
              arrayObjDetalle.append(estado)
              arrayObjDetalle.append(titulo_proyecto)

              dataFinal.append(arrayObjDetalle)
              counter = counter+1
              print(f'NoVacio count:{counter}--numero:{numero}')


  dataFinalJson = json.dumps(dataFinal)
  with open('links20012006.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)




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

      # print(totalData)

      # print(f'{valPeriodo}--WW-{valLegislatura}-WW--{valPresentacion}--WW-{valNumero}--WW-{valProponente}-WW--{valPalamentario}-WW--{valTitulo}--WW-{valSumilla}--WW-{valAutores}---{valAdherentes}-WW--{valSeguimiento}--WW-{valIniciativa}')
  dataFinalJson = json.dumps(totalData)
  with open('data20012006.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)




# getLinks20112016()
# getLinks20062011()
# getLinks20012006()

# getCompleteData20112016()
# getCompleteData20062011()
getCompleteData20012006()