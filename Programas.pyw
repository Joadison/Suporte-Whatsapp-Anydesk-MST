import os
import time
import re
import datetime, random
from tkinter import ttk
from tkinter import *

def whatss():
    numero = numero1.get()
    chamado = chamado1.get()
    nome = nome1.get()

    numero = re.sub("\+|\(|\)|\.|\-","", numero)
    numero = numero.replace(" ","")

    telefone = '55'+numero
    #def saudacao():
    mensagem = '\n'
    hora = datetime.datetime.now().hour
    if hora < 12:
        mensagem = 'Bom dia, '
    elif 12 <= hora < 18:
        mensagem = 'Boa tarde, '
    else:
        mesnagem = 'Boa noite, '

    mensagem += '''%s! Meu nome é Joadison! Sou do CATI, estou entrando em contato referente ao chamado.:%s ''' %(nome, chamado)
    os.system('start chrome "https://web.whatsapp.com/send?phone=%s&text=%s"' %(telefone, mensagem))
    #os.system('start chrome "https://wa.me/send?phone=%s&text=%s"' %(telefone, mensagem))


def remot():
    anydes = anydesk.get()
    re.sub("\+|\(|\)|\.|\-","", anydes)
    anydes.replace(" ","")
    print(anydes)
    os.system('start AnyDesk.exe "%s"' %(anydes))
    
def remotmicrosoft():
    remotmts = remotmic.get()
    os.system('start cmdkey /generic:"%s" /user:"tjce-dom-01\\" /pass:"" ' %(remotmts))
    time.sleep(2)
    os.system('start mstsc /v:%s' %(remotmts))
    time.sleep(2)
    os.system('start cmdkey /delete:%s' %(remotmts))

root = Tk()
root.title('Programas')
root.geometry('500x280')
root.configure(background='#71a6ff')

tela = ttk.Notebook(root)
tela.pack()

frame1 = ttk.Frame(tela)
frame1.pack(fill='both', expand=True)
frame2 = ttk.Frame(tela)
frame2.pack(fill='both', expand=True)
frame3 = ttk.Frame(tela)
frame3.pack(fill='both', expand=True)


#######################################################
tela.add(frame1, text='Suporte Whatsapp')
label1 = Label(frame1,text = "Número").pack()
numero1 = Entry(frame1)
numero1.pack()

label2 = Label(frame1,text = "Chamado").pack()
chamado1 = Entry(frame1)
chamado1.pack()

label3 = Label(frame1,text = "Nome").pack()
nome1 = Entry(frame1)
nome1.pack()

buton = Button(frame1, text="Iniciar", command= whatss)
buton.pack()

#######################################################
tela.add(frame2, text='Acesso Remoto')
label1 = Label(frame2,text = "Anydesk").pack()
anydesk = Entry(frame2)
anydesk.pack()
buton1 = Button(frame2, text="OK", command= remot)
buton1.pack()

label2 = Label(frame2,text = "Conexão de Área de Trabalho Remota").pack()
remotmic = Entry(frame2)
remotmic.pack()
buton2 = Button(frame2, text="OK", command= remotmicrosoft)
buton2.pack()



#######################################################
tela.add(frame3, text='Info')
label1 = Label(frame3,text = "Sistema").pack()
textt = Label(frame3, text = "Sistema feito para agilizar o Atendimento!").pack()


root.mainloop()

