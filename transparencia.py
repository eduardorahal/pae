
from bs4 import BeautifulSoup
import urllib.request
import json
    
req = urllib.request.Request('http://www.transparencia.sc.gov.br/data/remuneracao-servidores-detalhe/27851301')
page = urllib.request.urlopen(req)

print(page.name)


# data = json.loads(page)
# # soup = BeautifulSoup(page, 'html.parser')
# # for x in soup.select('input[name*=nome_]'):
# #     nome = x['value']
    
# #     with open("regionais.txt", "a") as a_file:
# #         a_file.write(nome)
# #         a_file.write(";")
# #         a_file.write(str(n))
# #         a_file.write("\n")

# file = data[0]
# print(file)