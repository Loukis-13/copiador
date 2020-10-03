from tkinter import*
import random

def leitor():
    filename = filedialog.askopenfile(filetypes=[("Text files","*.txt")])
    e1.delete('1.0',END)
    e1.insert(END, filename.read())
    l2['text']=filename.name.split('/')[-1]

def separador():
    x=e1.get("1.0",END)
    x=x.split()
    x=random.choice(x)
    janela.clipboard_clear()
    janela.clipboard_append(x)
    janela.update()
    ll['text']=x
    
janela = Tk()
janela.title("Copiador")
janela.geometry("400x250")

v0=Label(janela);v0.pack()
frame = Frame(janela);frame.pack()

l1 = Label(frame, text="Texto")
l1.grid(row=0,column=1)
e1 = Text(frame, height=6, width=43, borderwidth=2)
e1.grid(row=1,column=1)
s = Scrollbar(frame)
s.grid(row=1,column=2,sticky='ns')
s.config(command=e1.yview)
e1.config(yscrollcommand=s.set)

bt = Button(frame, text="Escolher arquivo", command=leitor)
bt.grid(row=2,column=1,sticky='w')
l2 = Label(frame, text='')
l2.grid(row=2,column=1,sticky='e')

ll=Label(janela)
ll.pack()

bt1= Button(janela, text="Ctrl+v", command=separador)
bt1.pack()

janela.mainloop()