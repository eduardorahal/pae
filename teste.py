fileObj = open("mail_teste.txt", "r") 
emails = fileObj.read().splitlines() 
fileObj.close()
for email in emails:
    print(email)