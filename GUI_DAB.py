from tkinter import *
from __MiniProjet import dab_db as db

# ###################################################################################################
# ######################################__Programming__Part__########################################
# ###################################################################################################
press = ''


def numbut(num):
    global press
    length = len(entr.get())
    if length in [3, 8, 13]:
        press += (str(num) + '-')
        entry.set(press)
    elif length > 18:
        entr.focus_displayof()
    else:
        press += str(num)
        entry.set(press)
    entr.icursor(len(press))


def enter1():
    ecran.configure(state='normal')
    ecran.delete(3.0, 'end')
    num_carte = entry.get()
    num_cartes = [i[2] for i in db.cards()]
    if not num_carte:
        ecran.insert(INSERT, '\n\n\n Tapez le numéro SVP.')
    elif len(num_carte) < 18 or num_carte not in num_cartes:
        ecran.insert(INSERT, '\n\n\n Incorrecte numéro carte.')
    elif num_carte in num_cartes:
        etat_carte = db.carte_info(num_carte)[5]
        if not etat_carte:
            ecran.insert(INSERT, '\n\n\n Invalide carte')
            card_label.pack_forget()
            avale_label.pack()

        # TODO: reni hna nkamel la partie hadi... w la partie code
        # TODO: le problème fi command nte3 ENTER button !!???
    ecran.configure(state='disable')


def enter2():
    global press
    pass


def cancel():
    clear()


def clear():
    global press
    ecran.configure(state='normal')
    entr.delete(0, 'end')
    ecran.delete(3.0, 'end')
    press = ''
    entr.focus_set()
    ecran.configure(state='disable')


# #####################################################################################################
# ######################################__Designing__Part__############################################
# #####################################################################################################

# MAIN Window__________________________________________________________________
main: Tk = Tk()
main.geometry('780x520+265+75')
main.title("Distributeur Automatique de Billets")
main.configure(bg='NavajoWhite1')
main.lift()
main.resizable(0, 0)
main.iconbitmap(r'Images\atm.ico')
main.wm_attributes("-topmost", 1)

# DAB Label ___________________________________________________________________
dab = Label(main, text='DI$TRIBUT£UR AUTOMATIQUE DE BILL£T$',
            bg='NavajoWhite1', fg='DarkGoldenrod3', anchor='s',
            font=('Perpetua', 20, 'bold'), bd=3, justify='center')
dab.pack(ipady=4)

# Operations Frames ___________________________________________________________
first_frame = Frame(main, height=450, width=360,
                    bg='gray20',
                    relief=SUNKEN)
first_frame.pack(side='left', ipadx=20)

second_frame = Frame(main, height=450, width=360,
                     bg='gray20',
                     relief=SUNKEN)
second_frame.pack(side='left', ipadx=20)

# Client_Information Frame ____________________________________________________
info_frame = Frame(main, height=450, width=360,
                   bg='gray20',
                   relief=SUNKEN)

# L'ecran _____________________________________________________________________
ecran = Text(first_frame, bg='PaleGreen1', bd=2,
             fg='gray15', width=25, height=7,
             font=('times', 12),
             relief=SUNKEN, wrap=WORD)
ecran.place(x=70, y=45)
ecran.insert(0.0, '\n Entrer votre numéro de carte:')
ecran.configure(state='disable')

# Entry card number ___________________________________________________________
entry = StringVar()
entr = Entry(first_frame, bg='PaleGreen1',
             fg='gray20', width=18, relief=SOLID,
             font=('times', 12, 'bold'), justify='center',
             textvariable=entry)
entr.place(x=100, y=90)
entr.focus_set()

# Image _______________________________________________________________________
card_pic = PhotoImage(file=r'Images\carte.png')
card_label = Label(second_frame, bg='gray20', justify=CENTER,
                   image=card_pic, compound=CENTER)
card_label.pack()
# card_label.place(x=10, y=10)

carte_avale = PhotoImage(file=r'Images\avalé.png')
avale_label = Label(second_frame, bg='gray20', justify=CENTER,
                    image=carte_avale, compound=CENTER)


# Buttons _____________________________________________________________________
def btn(text, cmd, bg='ivory3', abg='ivory4'):
    return Button(first_frame, text=text, bg=bg, fg='black',
                  activebackground=abg, bd=4,
                  font=('Arial', 14, 'bold'),
                  cursor='hand2', padx=15, pady=4,
                  command=cmd, relief=GROOVE)


def empty_button():
    vide = btn('  ', None)
    vide.configure(state='disabled')
    return vide


vide1 = empty_button().place(x=40, y=380)
vide2 = empty_button().place(x=180, y=380)
_0_ = btn('0', lambda: numbut(0)).place(x=110, y=380)
_1_ = btn('1', lambda: numbut(1)).place(x=40, y=200)
_2_ = btn('2', lambda: numbut(2)).place(x=110, y=200)
_3_ = btn('3', lambda: numbut(3)).place(x=180, y=200)
_4_ = btn('4', lambda: numbut(4)).place(x=40, y=260)
_5_ = btn('5', lambda: numbut(5)).place(x=110, y=260)
_6_ = btn('6', lambda: numbut(6)).place(x=180, y=260)
_7_ = btn('7', lambda: numbut(7)).place(x=40, y=320)
_8_ = btn('8', lambda: numbut(8)).place(x=110, y=320)
_9_ = btn('9', lambda: numbut(9)).place(x=180, y=320)

ent = Button(first_frame, text='ENTER',
             bg='forest green', fg='black',
             activebackground='dark green', bd=4,
             font=('Arial', 11, 'bold'),
             cursor='hand2', pady=7,
             command=lambda: [enter1(), enter2()], relief=GROOVE).place(x=270, y=320)

clr = Button(first_frame, text='CLEAR',
             bg='orange', fg='black',
             activebackground='dark orange', bd=4,
             font=('Arial', 11, 'bold'),
             cursor='hand2', padx=2, pady=7,
             command=clear, relief=GROOVE).place(x=270, y=260)

cncl = Button(first_frame, text='CANCEL',
              bg='red', fg='black',
              activebackground='red2', bd=4,
              font=('Arial', 10, 'bold'),
              cursor='hand2', padx=2, pady=9,
              command=cancel, relief=GROOVE).place(x=270, y=200)

main.mainloop()
