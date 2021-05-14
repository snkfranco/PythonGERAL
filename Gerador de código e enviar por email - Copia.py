import smtplib    #Usada para enviar o e-mail
import random     #Usada para gerar número aleatório para cadastro
import os         #Usada para limpar a tela com os.system('cls')
import colorama   #Biblioteca de cor usada
import winsound   #Usada para reproduzir "beep" sounds

os.system('cls')

print('\n\n\033[36m  >>> Autenticador \033[m')
print('\n Para segurança do nosso trabalho o CPF vai ser conferido com o nome colocado abaixo ')
usuario = input('\n  >> Digite o seu Discord (com a #): ')
nome = input('\n  >> Digite seu nome: ')
cpf = input('\n  >> Digite seu CPF: ')

verificador = random.randint(0,999999999999) #Gera um número aleatório entre 0 e 999999999999

gmail_user = "EMAIL DE ORIGEM AQUI"
gmail_pwd = "SENHA DO EMAIL ACIMA"
TO = "EMAIL DE DESTINO" 
SUBJECT = verificador
TEXT = usuario
TEXT2 = nome
TEXT3 = cpf
TEXT4 = " "
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)

BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '\n', TEXT,' ','\n', TEXT2,' ','\n', TEXT3,' ','\n', TEXT4])

server.sendmail(gmail_user, [TO], BODY)

winsound.Beep(440, 100)
winsound.Beep(500, 100)

os.system('cls')
print('\n\n\033[36m  >>>  Aguarde a confirmação do e-mail e o cadastro do seu código \033[m')
print('\n\033[32m  >>>  Obrigado pela Preferência!\033[m')
input('\n  >>>  Pressione ENTER tecla pra sair...')

print('\a')