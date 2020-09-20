import urllib
import urllib.request
import os
import time

# Função que cria o arquivo
def criar(nome):
	try:
		a = open(nome, 'wt+')
	except:
		print("Não foi possivel criar arquivo")
	else:
		return True

# Nome do arquivo que vai ser criado
arquivo = "dados.txt"
if not criar(arquivo):
	criar(arquivo)

os.system("clear")

# Iniciando o programa

print("""\033[1;93m
	███████╗██████╗ ██╗██████╗ ███████╗██████╗ 
	██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
	███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝
	╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗
	███████║██║     ██║██████╔╝███████╗██║  ██║
	╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝\033[m
	         	\033[1;91mVersão 1.0\033[m
""")

# Explicação

print("""
#############################################################
\033[1;33m
Explicação:

Este script se conecta a qualquer site que está
no ar e retorna se o usuário quiser, o html inteiro do site!
\033[m
-------------------------------------------------------------
\033[1;94m
Script criado por > Lucas Walker
link facebook > https://www.facebook.com/Walker.Lxrd
link GitHub > https://github.com/lucas-Dk
\033[m
------------------------------------------------------------
\033[1;96m
OBS: Necessário 'http://' ou 'https://'

Qualquer merda gerada, não tenho responsabilidade sobre!
Fiz para fins de estudos!

Exemplo:

https://www.google.com
http://www.pudim.com.br
\033[m
#############################################################
""")

# Entrada de dados

try:
	nome = str(input("Nome do site: "))
	link = str(input("Url: "))

except KeyboardInterrupt:
	print("\nUsuário decidiu sair!")
else:

	print("Conectando ao {}....\n".format(nome))
	time.sleep(2)

	try:
		site = urllib.request.urlopen(link)
	except:
		print("Ocorreu um erro ao se conectar!")
	else:
		print("Estou conectado!\n")


	try:
		ler = str(input("Deseja ler o html? S/N: ")).upper().strip()
	except KeyboardInterrupt:
		print("Usuário decidiu sair!")

	else:
		if ler in 'S':
			arm = site.read()
			try:
				a = open(arquivo, 'at')
			except:
				print("erro")
			else:
				try:
					a.write('HTML GERADO > {}\n'.format(arm))
				except:
					print("erro")
				else:
					print("\nGerando HTML...")
					time.sleep(0.9)
					print("Armazenando dentro do arquivo...")
					time.sleep(0.9)
					print("\nHtml gerado, verifique dentro do arquivo criado pelo script!")
					a.close()

		else:
			print("Saindo...")
			time.sleep(1)
			print()

print("\nPrograma encerrado, volte sempre!\n")
