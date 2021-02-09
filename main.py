import requests
from bs4 import BeautifulSoup

import csv
import json

def getLinks():
  totalLeyes2016 = 7.057	
  paginacion = 100
  llamadas = 71
  dataFinal = []

  totalLeyes2016 = "http://www.congreso.gob.pe/pley-2016-2021"

  pages = [1,101, 201, 301, 401, 501, 601, 701, 801, 901, 1001, 1101, 1201, 1301, 1401, 1501, 1601, 1701, 1801, 1901, 2001, 2101, 2201, 2301, 2401, 2501, 2601, 2701, 2801, 2901, 3001, 3101, 3201, 3301, 3401, 3501, 3601, 3701, 3801, 3901, 4001, 4101, 4201, 4301, 4401, 4501, 4601, 4701, 4801, 4901, 5001, 5101, 5201, 5301, 5401, 5501, 5601, 5701, 5801, 5901, 6001, 6101, 6201, 6301, 6401, 6501, 6601, 6701, 6801, 6901, 7001, 7101]

  counter = 0
  counterVacio = 0 

  for iter in range(llamadas):
      url = f"http://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey2016.nsf/Local%20Por%20Numero%20Inverso?OpenView&Start={pages[iter]}"
      p12 = requests.get(url)
      s = BeautifulSoup(p12.text, 'lxml')
      secciones = s.findAll('tr', attrs={'valign':'top'})

      for seccion in secciones:
          arrayObjDetalle = []
          arrayOfData = seccion.findAll('font', attrs={'face':'Verdana'})
          if arrayOfData == []:
              counterVacio= counterVacio+1
              print(f'Vacios count:{counterVacio}')
          else:

              tr = seccion.findAll('td')
              # tr = seccion.findAll('font')
              link = tr[0].font.a.get('href')
              numero = tr[0].getText()
              fecha_ultima = tr[1].getText()
              fecha_presente = tr[2].getText()
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
  with open('dataFinal2.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)


def getCompleteData():
  baseUrl = "http://www2.congreso.gob.pe"

  with open(f'dataFinal2.json', 'r', encoding='utf-8') as outFile:
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
        valueLinkDetalle = f'http://www2.congreso.gob.pe/sicr/tradocestproc/Expvirt_2011.nsf/visbusqptramdoc1621/{valueNumeroSimple}?opendocument'
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
  with open('dataTotal2.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)




# getLinks()

getCompleteData()