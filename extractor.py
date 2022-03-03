
from bs4 import BeautifulSoup
import urllib.request

n = 1
while n<31:

    if n < 10:
        lot = "0" + str(n) + "%AA"
    else:
        lot = str(n) + "%AA"
    
    req = urllib.request.Request('https://pae.sc.gov.br/direto/Direto/CatalogoBusiness?direto_tarefa=search&option=catalogo/geral&nome=&mail=&empresa=ou=policiacivil&setor='+lot+'&telefone=&ramal=&cargo=&matricula=&cidade=&estado=')
    req.add_header('Cookie', 'JSESSIONID=1oo1brjix7ws0')
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    for x in soup.select('input[name*=nome_]'):
        nome = x['value']
        
        with open("regionais.txt", "a") as a_file:
            a_file.write(nome)
            a_file.write(";")
            a_file.write(str(n))
            a_file.write("\n")

    n = n + 1