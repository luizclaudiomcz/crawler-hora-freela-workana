from bs4 import BeautifulSoup
import urllib3
import numpy as np

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
 
paginainicial = 1
paginafinal = 50
salarios = []

# Fazer requisição em cada pagina
for pagina in range (paginainicial,paginafinal + 1):
    print('\n')        
    print('Página: ' + str(pagina))
    url =  'https://www.workana.com/freelancers/brazil?category=it-programming&region=029%2C013%2C005&page=' + str(pagina)
    page = http.request('GET', url)
    soup = BeautifulSoup(page.data, 'lxml')
    
    # Pegar os metadados
    freelas = soup.find_all('div', class_ = 'js-worker listing worker-item')
    
    for freela in freelas:
        
        salario = freela.find('span','js-monetary-amount monetary-amount')
        
        if salario:
            salario = salario.text
            if ',' in salario:
                salario = salario.split(',')[0]
                salarios.insert(0,int(salario))            
                print('Salário: ' + str(salario))

mediana = np.median(salarios)
media = np.mean(salarios)
meu = np.quantile(salarios,0.7)
print('\n') 
print('######################') 
print('Mediana: ' + str(mediana))
print('Média: ' + str(media))
print('Meu salário: ' + str(meu))
