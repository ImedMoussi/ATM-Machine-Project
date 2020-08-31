from __MiniProjet import dab_db as db
from tkinter import *
from datetime import datetime

# ###################################################################################################
# ######################################__Programming__Part__########################################
# ###################################################################################################
num_carte = ''
code_pin = ''
count = 0


def numbut(num):
    global num_carte, code_pin
    length_card = len(card_num_entry.get())
    if length_card in [3, 8, 13]:
        num_carte += (str(num) + '-')
        card_num.set(num_carte)
    elif length_card > 18:
        card_num_entry.focus_displayof()
    else:
        num_carte += str(num)
        card_num.set(num_carte)
    card_num_entry.icursor(len(num_carte))

    lenght_code = len(code_entry.get())
    if lenght_code > 3:
        code_entry.focus_displayof()
    else:
        code_pin += str(num)
        code.set(code_pin)
    code_entry.icursor(len(code_pin))


def enter1():
    global num_carte, code_pin
    ecran.configure(state='normal')
    ecran.delete(3.0, END)
    num_carte = card_num.get()
    num_cartes = [i[2] for i in db.cards()]
    if not num_carte:
        ecran.insert(INSERT, '\n\n\n Tapez le numéro SVP.')
    elif num_carte not in num_cartes:
        ecran.insert(INSERT, '\n\n\n Incorrecte numéro carte.')
    elif num_carte in num_cartes:
        etat_carte = db.carte_info(num_carte)[5]
        if not etat_carte:
            ecran.insert(INSERT, '\n\n\n Invalide carte')
            card_num_entry.configure(state='readonly')
            card_pic.pack_forget()
            avale_pic.pack()
        else:  # Cas favorable
            code_pin = ''
            code.set(code_pin)
            info = db.carte_info(num_carte)
            enter_button.configure(command=lambda: enter2(info))
            ecran.delete(0.0, END)
            ecran.insert(INSERT, '\n Entrer votre code secret:')
            card_pic.pack_forget()
            avale_pic.pack_forget()
            card_num_entry.delete(0, END)
            card_num_entry.place_forget()
            code_pic.pack()
            code_entry.place(x=110, y=90)
            code_entry.delete(0, END)
            code_entry.focus_set()
    ecran.configure(state='disable')


def enter2(info):
    global num_carte, code_pin, count
    ecran.configure(state='normal')
    ecran.delete(3.0, END)
    code_card = info[3]
    code_pin = code.get()
    if count < 2:
        if not code_pin:
            ecran.insert(INSERT, '\n\n\n Tapez le code SVP.')
        elif int(code_pin) != code_card:
            ecran.insert(INSERT, '\n\n\n Incorrecte code PIN.')
            count += 1
        else:  # Cas favorable
            count = 0
            info0.set(db.client_info(info[1])[1])
            info1.set(info[1])
            info2.set(info[2])
            info3.set(f'{db.compte_info(info[1])[2]:.2f}')
            info4.set(info[4])
            second_frame.pack_forget()
            info_frame.pack(side='left', ipadx=20)
            ecran.delete(0.0, END)
            ecran.insert(INSERT, '\n\n\n Bienvenue dans votre compte.')
            code_entry.place_forget()
    else:
        code_pic.pack_forget()
        avale_pic.pack()
        ecran.delete(0.0, END)
        ecran.insert(INSERT, '\n\n\n Incorrecte code 3 fois.')
        code_entry.place_forget()
    ecran.configure(state='disable')


def delete():
    global num_carte, code_pin
    length_card = len(card_num_entry.get())
    if length_card in [5, 10, 15]:
        num_carte = num_carte[:-2]
        card_num.set(num_carte)
    else:
        num_carte = num_carte[:-1]
        card_num.set(num_carte)

    code_pin = code_pin[:-1]
    code.set(code_pin)


def clear():
    global num_carte, code_pin
    num_carte = ''
    code_pin = ''
    ecran.configure(state='normal')
    ecran.delete(5.0, END)
    ecran.configure(state='disable')
    card_num_entry.delete(0, END)
    card_num_entry.focus_set()
    code_entry.delete(0, END)
    code_entry.focus_set()


def cancel():
    pass


# #####################################################################################################
# ######################################__Designing__Part__############################################
# #####################################################################################################

# MAIN Window__________________________________________________________________
main: Tk = Tk()
main.geometry('780x520+265+100')
main.title("Distributeur Automatique de Billets")
main.configure(bg='NavajoWhite1')
main.lift()
main.deiconify()
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
# info_frame.pack(side='left', ipadx=20)

# Date ________________________________________________________________________
w = Label(first_frame,
          text=f"{datetime.now():%d-%m-%Y}",
          fg="azure", bg="gray20",
          font=("times", 14))
w.place(x=10, y=10)

# L'ecran _____________________________________________________________________
ecran = Text(first_frame, bg='PaleGreen1', bd=2,
             fg='gray12', width=25, height=7,
             font=('times', 12),
             relief=SUNKEN, wrap=WORD)
ecran.place(x=80, y=45)
ecran.insert(0.0, '\n Entrer votre numéro de carte:')
ecran.configure(state='disable')

# Entry card number ___________________________________________________________
card_num = StringVar()
card_num_entry = Entry(first_frame, bg='PaleGreen1',
                       fg='gray20', width=18, relief=SOLID,
                       font=('times', 12, 'bold'), justify='center',
                       textvariable=card_num)
card_num_entry.place(x=110, y=90)
card_num_entry.focus_set()

# Entry code PIN ___________________________________________________________
code = StringVar()
code_entry = Entry(first_frame, bg='PaleGreen1',
                   fg='gray20', width=18, relief=SOLID,
                   font=('times', 12, 'bold'), justify='center',
                   show="•", textvariable=code)

# Images _______________________________________________________________________
card = PhotoImage(file=r'Images\carte.png')
card_pic = Label(second_frame, bg='gray20', justify=CENTER,
                 image=card, compound=CENTER)
card_pic.pack()

avale = PhotoImage(file=r'Images\avalé.png')
avale_pic = Label(second_frame, bg='gray20', justify=CENTER,
                  image=avale, compound=CENTER)

codes = PhotoImage(file=r'Images\code.png')
code_pic = Label(second_frame, bg='gray20', justify=CENTER,
                 image=codes, compound=CENTER)

retirer = PhotoImage(file=r'Images\money.png')
money_pic = Label(second_frame, bg='gray20', justify=CENTER,
                  image=retirer, compound=CENTER)

merci = PhotoImage(file=r'Images\merci.png')
merci_pic = Label(second_frame, bg='gray20', justify=CENTER,
                  image=merci, compound=CENTER)


# Buttons _____________________________________________________________________
def btn(text, cmd, stt='normal'):
    return Button(first_frame, text=text,
                  command=cmd,
                  state=stt,
                  bg='ivory3',
                  activebackground='ivory4',
                  bd=4, fg='black',
                  font=('Arial', 14, 'bold'),
                  cursor='hand2',
                  padx=15, pady=4,
                  relief=GROOVE)


vide1 = btn('  ', None, 'disabled').place(x=40, y=380)
vide2 = btn('  ', None, 'disabled').place(x=180, y=380)
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

enter_button = Button(first_frame, text='ENTER',
                      bg='forest green', fg='black',
                      activebackground='dark green', bd=4,
                      font=('Arial', 11, 'bold'),
                      cursor='hand2', pady=7,
                      command=enter1,
                      relief=GROOVE)
enter_button.place(x=270, y=320)

clear_button = Button(first_frame, text='CLEAR',
                      bg='orange', fg='black', bd=4,
                      activebackground='dark orange',
                      font=('Arial', 11, 'bold'),
                      cursor='hand2', padx=2, pady=7,
                      command=clear, relief=GROOVE)
clear_button.place(x=270, y=260)

cancel_button = Button(first_frame, text='CANCEL',
                       bg='red', fg='black',
                       activebackground='red2', bd=4,
                       font=('Arial', 10, 'bold'),
                       cursor='hand2', padx=2, pady=9,
                       command=cancel, relief=GROOVE)
cancel_button.place(x=270, y=200)

delete_button = Button(first_frame, text='🢀',
                       bg='ivory3', fg='black',
                       activebackground='ivory4', bd=4,
                       font=('Arial', 18),
                       cursor='hand2', padx=13, pady=0,
                       command=delete, relief=GROOVE)
delete_button.place(x=270, y=380)

# Information _________________________________________________________________
sys_banq = Label(info_frame, text='SYSTÈME BANCAIRE',
                 bg='gray20', fg='old lace', anchor='s',
                 font=('Rockwell', 20, 'bold', 'underline'),
                 bd=3, justify='center')
sys_banq.place(x=20, y=20)

code_clt = Label(info_frame, text='⮚ Code client:',
                 bg='gray20', fg='azure', anchor='s',
                 font=('times', 16)).place(x=0, y=100)

info1 = StringVar()
code_clt_info = Entry(info_frame, bg='light grey',
                      fg='gray18', width=18,
                      font=('times', 12, 'bold'),
                      insertwidth=5, relief=SUNKEN,
                      textvariable=info1).place(x=180, y=100)

Nom_prenom = Label(info_frame, text='⮚ Nom & Prénom:',
                   bg='gray20', fg='azure', anchor='s',
                   font=('times', 16)).place(x=0, y=150)

info0 = StringVar()
nom_pre_info = Entry(info_frame, bg='light grey',
                     fg='gray18', width=18,
                     font=('times', 12, 'bold'),
                     insertwidth=5, relief=SUNKEN,
                     textvariable=info0).place(x=180, y=150)

cart = Label(info_frame, text='⮚ Numéro de carte:',
             bg='gray20', fg='azure', anchor='s',
             font=('times', 16)).place(x=0, y=200)

info2 = StringVar()
no_card = Entry(info_frame, bg='light grey',
                fg='gray18', width=18,
                font=('times', 12, 'bold'),
                insertwidth=5, relief=SUNKEN,
                textvariable=info2).place(x=180, y=200)

sold = Label(info_frame, text="⮚ Solde: ",
             bg='gray20', fg='azure', anchor='s',
             font=('times', 16)).place(x=0, y=250)

info3 = StringVar()
amount = Entry(info_frame, bg='light grey',
               fg='gray18', width=18,
               font=('times', 12, 'bold'),
               insertwidth=5, relief=SUNKEN,
               textvariable=info3).place(x=180, y=250)

date = Label(info_frame, text="⮚ Date d'expiration: ",
             bg='gray20', fg='azure', anchor='s',
             font=('times', 16)).place(x=0, y=300)

info4 = StringVar()
date_exp = Entry(info_frame, bg='light grey',
                 fg='gray18', width=18,
                 font=('times', 12, 'bold'),
                 insertwidth=5, relief=SUNKEN,
                 textvariable=info4).place(x=180, y=300)
# TODO: nbedel hado les info 1 2 3 4 ...
# TODO: add buttons withdarw and exit

main.mainloop()
