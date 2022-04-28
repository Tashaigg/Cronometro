# Programa que cronometra o tempo e salva em arquivos cada run
# Objetivo: contar tempo de estudo e ter acesso a tempo de dias anteriores

from datetime import *
from tkinter import *
from pathlib import Path

# Defs
def show():
    global status
    global my_label
    global delta
    if status == 'playing':
        my_label.destroy()
        delta = datetime.now() - time1
        try:
            delta_s = str(delta).split('.',1)[0] + '.' + str(delta).split('.',1)[1][0:2]
        except:
            delta_s = str(delta).split('.',1)[0] + '.' + '00'
        my_label = Label(root, bg='black', border=10, width=10, fg='blue', text=delta_s, font=('Arial', 50))
        my_label.grid(row=0, column=0,columnspan=2, sticky='EWNS')
        my_label.after(12,lambda : show())

def play():
    global my_label
    global status
    global time1
    if status == 'paused':
        p = open(Path(f'{Path.home()}\\Desktop\\Python\\cronometro\\tempos.txt'),'a')
        p.write('Inicio em ' + str(datetime.now()) + '\n')
        p.close()
        status = 'playing'
        time1 = datetime.now() - delta
        show()

def pause():
    global status
    global delta
    global pausa_ant
    if status == 'playing':
        p = open(Path(f'{Path.home()}\\Desktop\\Python\\cronometro\\tempos.txt'),'a')
        p.write('Pausa em ' + str(datetime.now()) + ' SOMANDO: ' + str(delta - pausa_ant)+'\n')
        p.close()
        pausa_ant = delta
        status = 'paused'


def close():
    p = open(Path(f'{Path.home()}\\Desktop\\Python\\cronometro\\tempos.txt'),'a')
    p.write('Término em ' + str(datetime.now()) + ' TOTAL: ' + str(delta)+'\n\n')
    p.close()
    root.destroy()

# Create Object
root = Tk()
root.geometry("412x365")


status = 'paused'
time1 = datetime.now()
delta = datetime.now()-time1
delta_s = str(delta)+'.00'
pausa_ant = delta

# Create buttons
btnplay = Button(root, bg='black', border=5, width=5, fg='#15E42A', text='Play', font=('Forte', 50), command=play)
btnpause = Button(root, bg='black', border=5, width=5, fg='#FF993F', text='Pause', font=('Forte', 50), command=pause)
btnclose = Button(root, bg='black', border=5, width=10, fg='#FF0000', text='Close', font=('Forte', 50), command=close)
my_label = Label(root, bg='black', border=10, width=10, fg='blue', text=delta_s, font=('Arial', 50))

# Display buttons
my_label.grid(row=0, column=0,columnspan=2, sticky='EWNS')
btnplay.grid(row=1, column=0, columnspan=1, sticky='EWNS')
btnpause.grid(row=1, column=1, columnspan=1, sticky='EWNS')
btnclose.grid(row=2, column=0, columnspan=2, sticky='EWNS')


root.mainloop()
