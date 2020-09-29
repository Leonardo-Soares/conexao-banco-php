import requests
import os

#https://servicodados.ibge.gov.br/api/docs/agregados?versao=3#api-acervo

Url = 'https://servicodados.ibge.gov.br/api/v3/agregados/5939/periodos/2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017/variaveis/529|531|532|6568|534?localidades=N3[15]'

#Requisisção dos dados
Data = requests.get(Url).json()

#Funçao Cabeçario
def header():
  os.system('clear') or None
  print('ÍNDICE DE GINI NO PARÁ NOS ANOS DE 2002 ATÉ 2017')
  print('===========================================================')
  print('Obs: A medição do índice de Gini obedece a seguinte escala:\n0 (quando não há desigualdade)\n1 (com desigualdade máxima)')
  print('===========================================================')

#Função Lista de 2002 a 2017
def verificar(resposta):
    if resposta == 2002:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2002']
      print(dado1)

    if resposta == 2003:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2003']
      print(dado1)

    if resposta == 2004:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2004']
      print(dado1)

    if resposta == 2005:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2005']
      print(dado1)

    if resposta == 2006:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2006']
      print(dado1)

    if resposta == 2007:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2007']
      print(dado1)

    if resposta == 2008:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2008']
      print(dado1)

    if resposta == 2009:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2009']
      print(dado1)

    if resposta == 2010:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2010']
      print(dado1)

    if resposta == 2011:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2011']
      print(dado1)

    if resposta == 2012:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2012']
      print(dado1)

    if resposta == 2013:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2013']
      print(dado1)

    if resposta == 2014:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2014']
      print(dado1)

    if resposta == 2015:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2015']
      print(dado1)

    if resposta == 2016:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2016']
      print(dado1)

    if resposta == 2017:
      dado1 = Data[0]['resultados'][0]['series'][0]['serie']['2017']
      print(dado1)

#Função Principal 
def main ():
  header()
  resp = float(input("\nDigite um ano entre 2002 a 2017 (o valor deve ser do tipo inteiro)\n"))

  #Verifica Resposta
  if resp >= 2002 and resp <= 2017:
    #Titulo
    titulo = Data[0]['variavel']
    print('\n',titulo , 'no ano de', resp, 'é:')
    #Resultado
    verificar(resp)
    
    #Repetir ciclo
    print('===========================================================')
    repetir = int(input("Deseja realizar um nova consulta ? \n[Digite 1 para sim ou 2 para não]\n"))

    if repetir == 1:
      os.system('clear') or None
      main()
    else:
      os.system('clear') or None
      print('Finalizando...')
  else:
    print('\nNão tenho dados desse ano!\n')
    repetir = int(input("Deseja realizar um nova consulta ?\n[Digite 1 para sim ou 2 para não]\n"))
    if repetir == 1:
      os.system('clear') or None
      main()
      
    else:
      os.system('clear') or None
      print('Finalizando...')

#Primeira Pergunta 
header()
resp = float(input("\nDigite um ano entre 2002 a 2017 (o valor deve ser do tipo inteiro)\n"))

#Verifica a resposta
if resp >= 2002 and resp <= 2017:
  #Titulo
  titulo = Data[0]['variavel']
  print('\n',titulo, 'no ano de', resp, 'é:')
  verificar(resp)
  #Repetir Ciclo
  print('===========================================================')
  repetir = int(input("\nDeseja realizar um nova consulta ? \n[Digite 1 para sim ou 2 para não]\n"))

  if repetir == 1:
    os.system('clear') or None
    main()
  else:
    os.system('clear') or None
    print('Finalizando...')
else:
  print('\nNão tenho dados desse ano!\n')
  repetir = int(input("Deseja realizar um nova consulta ?\n[Digite 1 para sim ou 2 para não]\n"))
  if repetir == 1:
    main()
  else:
    os.system('clear') or None
    print('Finalizando...')