import requests
from bs4 import BeautifulSoup

import csv
import json


from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry



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




def getLinks20002001():

#   totalLeyes2001 = 01968
  paginacion = 30
  llamadas = 66
  dataFinal = []

  totalLeyes2001 = "http://www.congreso.gob.pe/pley-2000-2001"
  pages = [1,31, 61, 91, 121, 151, 181, 211, 241, 271, 301, 331, 361, 391, 
  421, 451, 481, 511, 541, 571, 601, 631, 661, 691, 721, 751, 781, 811, 
  841, 871, 901, 931, 961, 991, 1021, 1051, 1081, 1111, 1141, 1171, 1201, 
  1231, 1261, 1291, 1321, 1351, 1381, 1411, 1441, 1471, 1501, 1531, 1561, 
  1591, 1621, 1651, 1681, 1711, 1741, 1771, 1801, 1831, 1861, 1891, 1921, 
  1951, 1981]

  counter = 0
  counterVacio = 0 
  print("here we goo")
  for iter in range(llamadas):
      url = f"http://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey2000.nsf/Por%20Numero?OpenView&Start={pages[iter]}"
              
      p12 = requests.get(url)
      s = BeautifulSoup(p12.text, 'lxml')
      secciones = s.findAll('tr', attrs={'valign':'top'})
      print(len(secciones))
      for seccion in secciones:
          arrayObjDetalle = []
          arrayOfData = seccion.findAll('font', attrs={'size':'1','face':'Verdana'})
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
  with open('links20002001.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)




def getLinks19952000():

#   totalLeyes2001 = 05807	
  paginacion = 30
  llamadas = 194
  dataFinal = []

  totalLeyes2001 = "http://www.congreso.gob.pe/pley-1995-2000"
  pages = [1, 31, 61, 91, 121, 151, 181, 211, 241, 271, 301, 331, 361, 391, 421, 
  451, 481, 511, 541, 571, 601, 631, 661, 691, 721, 751, 781, 811, 841, 871, 901,
   931, 961, 991, 1021, 1051, 1081, 1111, 1141, 1171, 1201, 1231, 1261, 1291, 1321,
    1351, 1381, 1411, 1441, 1471, 1501, 1531, 1561, 1591, 1621, 1651, 1681, 1711,
     1741, 1771, 1801, 1831, 1861, 1891, 1921, 1951, 1981, 2011, 2041, 2071, 2101,
      2131, 2161, 2191, 2221, 2251, 2281, 2311, 2341, 2371, 2401, 2431, 2461, 2491,
       2521, 2551, 2581, 2611, 2641, 2671, 2701, 2731, 2761, 2791, 2821, 2851, 2881,
        2911, 2941, 2971, 3001, 3031, 3061, 3091, 3121, 3151, 3181, 3211, 3241, 3271,
         3301, 3331, 3361, 3391, 3421, 3451, 3481, 3511, 3541, 3571, 3601, 3631, 3661,
          3691, 3721, 3751, 3781, 3811, 3841, 3871, 3901, 3931, 3961, 3991, 4021, 4051,
           4081, 4111, 4141, 4171, 4201, 4231, 4261, 4291, 4321, 4351, 4381, 4411, 4441,
            4471, 4501, 4531, 4561, 4591, 4621, 4651, 4681, 4711, 4741, 4771, 4801, 4831,
             4861, 4891, 4921, 4951, 4981, 5011, 5041, 5071, 5101, 5131, 5161, 5191, 5221,
              5251, 5281, 5311, 5341, 5371, 5401, 5431, 5461, 5491, 5521, 5551, 5581, 5611,
               5641, 5671, 5701, 5731, 5761, 5791, 5821]

  counter = 0
  counterVacio = 0 
  print("here we goo")
  for iter in range(llamadas):
      url = f"http://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey1995.nsf/Por%20Numero?OpenView&Start={pages[iter]}"

      p12 = requests.get(url)
      s = BeautifulSoup(p12.text, 'lxml')
      secciones = s.findAll('tr', attrs={'valign':'top'})
      print(len(secciones))
      for seccion in secciones:
          arrayObjDetalle = []
          arrayOfData = seccion.findAll('font', attrs={'size':'1','face':'Verdana'})
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
  with open('links19952000.json', 'w') as file:  # Use file to refer to the file object
    file.write(dataFinalJson)

# getLinks20112016()
# getLinks20062011()
# getLinks20012006()
# getLinks20002001()
getLinks19952000()
