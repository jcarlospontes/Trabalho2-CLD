from random import *
from tkinter import *
from tkinter import messagebox

W = []
Z = []
var_chk = 0
tabela = []
escolha = []

#funcao que gera o traco mealy
def geramealy(entrada,saida,sequencia):
	cont = 0
	for x in range(0, 25):
		p = (len(sequencia)-1)
		if (x <= len(sequencia)-2):
			saida.append(0)
			continue
		while p >= 0:
			if(entrada[x-p] == sequencia[cont]):
				cont +=1
				p -= 1
			else:
				cont = 0
				p -= 1
		if(cont == len(sequencia)):
			saida.append(1)
			cont = 0
		else:
			saida.append(0)
			cont = 0

#funcao que gera o traco moore
def geramoore(entrada,saida,sequencia):
	cont = 0
	for x in range(0, 25):
		if (x < len(sequencia)):
			saida.append(0)
		else:
			p = len(sequencia)
			while p > 0:
				if(entrada[x-p] == sequencia[cont]):
					cont +=1
					p -= 1
				else:
					cont = 0
					p -= 1
			if(cont == len(sequencia)):
				saida.append(1)
				cont = 0
			else:
				saida.append(0)
				cont = 0

#funcao que verifica se a sequencia é binaria
def eh_binario(x):
	for t in range(len(x)):
		if(x[t] == 0 or x[t] == 1):
			continue
		else:
			return False
	return True

#funcao que verifica a sequencia e a maquina
def btentrada_click():
	escolha = var_chk.get()
	if (escolha == 0):
		lberro2.place(x=210,y=93)
		return 0
	sequencia = textsequencia.get()
	sequencia = list(map(int, sequencia))
	if ((eh_binario(sequencia) == False) or (sequencia == [])):
		print("entrada invalida")
		W = []
		Z = []
		lberro1.place(x=210,y=93)
		if(escolha != 0):
			lberro2.place(x=5000,y=93)
	else:
		lberro1.place(x=5000,y=93)
		if(escolha != 0):
			lberro2.place(x=5000,y=93)
		W = []
		Z = []
		if escolha == 1:
			for x in range(0, 25):
				W.append(randint(0,1))
				tabela.append(W[x])
			geramoore(W,Z,sequencia)
		if escolha == 2:
			for x in range(0, 25):
				W.append(randint(0,1))
				tabela.append(W[x])
			geramealy(W,Z,sequencia)
		textosaida.configure(state='normal')
		textosaida.delete('0.0', END)
		textosaida.insert(0.0, Z)
		textosaida.configure(state='disabled')
		textoentrada.configure(state='normal')
		textoentrada.delete('0.0', END)
		textoentrada.insert(0.0, W)
		textoentrada.configure(state='disabled')

#funcao que gera a tabela de estados
def bttabela_click():
	estados = []
	escolha = var_chk.get()
	escolha = int(escolha)
	sequencia = textsequencia.get()
	if escolha == 1:
		#gera estado moore
		for x in range(len(sequencia)+1):
			if x == 0:
				estados.append("A")
			else:
				estados.append(chr(65+x))
		textotabela.configure(state='normal')
		textotabela.delete('0.0', END)
		prox = "X"
		saida = 0
		texto = ""
		texto += " _________________________________________________\n| Estado Atual | Proximo Estado | Entrada | Saída |\n"
		#cria uma matriz com o historico dos estados
		historicoestados = []
		for x in range(len(estados)):
			copiasequencia = sequencia[:]
			if x == 0:
				historicoestados.append([])
			else:
				historicoestados.append([])
				for y in range(x):
					historicoestados[x].append(int(copiasequencia[y]))
		for x in range (len(estados)):
			cont = 0
			#direciona o momento de saida 1
			if x == len(estados)-1:
				saida = 1
			#direciona o proximo estado
			temnohistorico = False
			prov = historicoestados[x][:]
			prov.append(int(cont))
			while temnohistorico == False:
				for z in range(len(estados)):
					if ((temnohistorico == False) and (prov == historicoestados[z])):
						prox = estados[z][:]
						temnohistorico = True
				if prov != []:
					prov.pop(0)
			texto += ("|      {}       |        {}       |    {}    |   {}   |\n".format(estados[x], prox, cont,saida))
			cont +=1
			#direciona o proximo estado
			temnohistorico = False
			prov = historicoestados[x][:]
			prov.append(int(cont))
			while temnohistorico == False:
				for z in range(len(estados)):
					if ((temnohistorico == False) and (prov == historicoestados[z])):
						prox = estados[z][:]
						temnohistorico = True
				if prov != []:
					prov.pop(0)
			texto += ("|      {}       |        {}       |    {}    |   {}   |\n".format(estados[x], prox, cont,saida))
		texto += " ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"
		textotabela.insert(0.0, texto)
		textotabela.configure(state='disabled')
	if escolha == 2:
		#gera estado mealy
		for x in range(len(sequencia)):
			estados.append(chr(65+x))
		textotabela.configure(state='normal')
		textotabela.delete('0.0', END)
		prox = "X"
		saida = 0
		texto = ""
		texto += " _________________________________________________\n| Estado Atual | Proximo Estado | Entrada | Saída |\n"
		#faz uma matriz com o historico de cada estado
		historicoestados = []
		for x in range(len(estados)):
			copiasequencia = sequencia[:]
			if x == 0:
				historicoestados.append([])
			else:
				historicoestados.append([])
				for y in range(x):
					historicoestados[x].append(int(copiasequencia[y]))
		for x in range(len(estados)):
			#direciona o momento de saida 1
			cont = 0
			if x == len(estados)-1:
				if cont == int(sequencia[x]):
					saida = 1
				else:
					saida = 0
			#direciona o proximo estado
			temnohistorico = False
			prov = historicoestados[x][:]
			prov.append(int(cont))
			while temnohistorico == False:
				for z in range(len(estados)):
					if ((temnohistorico == False) and (prov == historicoestados[z])):
						prox = estados[z][:]
						temnohistorico = True
				if prov != []:
					prov.pop(0)
			texto += ("|      {}       |        {}       |    {}    |   {}   |\n".format(estados[x], prox, cont,saida))
			cont +=1
			#direciona o momento de saida 1
			if x == len(estados)-1:
				if cont == int(sequencia[x]):
					saida = 1
				else:
					saida = 0
			#direciona o proximo estado
			temnohistorico = False
			prov = historicoestados[x][:]
			prov.append(int(cont))
			while temnohistorico == False:
				for z in range(len(estados)):
					if ((temnohistorico == False) and (prov == historicoestados[z])):
						prox = estados[z][:]
						temnohistorico = True
				if prov != []:
					prov.pop(0)
			texto += ("|      {}       |        {}       |    {}    |   {}   |\n".format(estados[x], prox, cont,saida))
		texto += " ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"
		textotabela.insert(0.0, texto)
		textotabela.configure(state='disabled')

#funcao que cria uma janela com o conteudo do botao about
def btabout_click():
	messagebox.showinfo("Sobre", "Segundo Trabalho de Circuitos Lógicos Digitais - UECE 2019.1 \n\nO programa mostra o traço e a tabela de estados de uma máquina Moore ou Mealy a partir de uma sequência de binários fornecida pelo usuário.\n\nJoão Carlos Pontes")

#janela principal
janela = Tk()
#retira a opção de maximizar a janela principal
janela.resizable(0,0)
#titulo da janela principal
janela.title("Trabalho CLD")
#dimensao da janela principal
janela.geometry("463x500+500+300")
janela.grid_rowconfigure(0, minsize=26)
janela.grid_rowconfigure(1, minsize=20)
janela.grid_rowconfigure(2, minsize=20)
janela.grid_rowconfigure(3, minsize=25)
janela.grid_rowconfigure(4, minsize=30)
janela.grid_rowconfigure(6, minsize=35)
#escrito na janela principal(label)
lbtraco = Label(janela, text="Traço")
lbtraco.grid(row=0,column=1)

lbentrada = Label(janela, text="Entrada:")
lbentrada.grid(row=1,column=0)

lbsaida = Label(janela, text="Saída:")
lbsaida.grid(row=2,column=0)

lbsequencia = Label(janela, text="Sequencia:")
lbsequencia.grid(row=3,column=0)

lbescolha = Label(janela, text="Escolha:")
lbescolha.grid(row=4,column=0)

lberro1 = Label(janela,text ="Sequencia inválida!")
lberro1.place(x=5000,y=93)

lberro2 = Label(janela,text ="Escolha uma opção!")
lberro2.place(x=5000,y=93)

#janela de saida de dados
textoentrada = Text(janela, width=49, height=1,state="disabled")
textoentrada.grid(row=1,column=1)

textosaida = Text(janela, width=49, height=1,state="disabled")
textosaida.grid(row=2,column=1)

textotabela = Text(janela, width=51, height=18,state="disabled")
textotabela.grid(row=7, columnspan=2, sticky=W)

#entrada de sequencia
textsequencia = Entry(janela,width=20)
textsequencia.grid(row=3,column=1)

#botoes
btentrada = Button(janela, width=8, text="Gerar Traço", command=btentrada_click)
btentrada.grid(row=5,column=1)

btmoore = Button(janela, width=9, text="Gerar Tabela", command=bttabela_click)
btmoore.grid(row=6, column=1)

btabout = Button(janela, width = 4, text="Sobre", command=btabout_click)
btabout.place(x=425,y=1)

#botao de escolha
var_chk = IntVar()
escolhamoore = Radiobutton(janela, text="Moore", variable=var_chk, value=1)
escolhamoore.place(x=70,y=97)
escolhamealy = Radiobutton(janela, text="Mealy", variable=var_chk, value=2)
escolhamealy.place(x=140,y=97)

janela.mainloop()