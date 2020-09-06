from __MiniProjet import data_base as db
from tkinter import *
from datetime import datetime

# ###################################################################################################
# ######################################__Programming__Part__########################################
# ###################################################################################################
num_carte = ''
code_secret = ''
montant = ''
count = 0


def press_btn(num):
    """When button clicked"""
    global num_carte, code_secret, montant
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
    if lenght_code == 4:
        code_entry.focus_displayof()
    else:
        code_secret += str(num)
        code.set(code_secret)
    code_entry.icursor(len(code_secret))

    montant += str(num)
    amount.set(montant)
    amount_entry.icursor(len(montant))


def validate(value):
    """Entry accept just numbers"""
    if str.isdigit(value) or value == "":
        return True
    else:
        return False


def enter_card():
    """verification card number"""
    global num_carte, code_secret
    ecran.configure(state=NORMAL)
    ecran.delete(3.0, END)
    num_carte = card_num.get()
    num_cartes = [i[2] for i in db.cards()]
    if not num_carte:
        ecran.insert(INSERT, '\n\n\n Tapez le numéro SVP.')
    elif num_carte not in num_cartes:
        ecran.insert(INSERT, '\n\n\n Incorrecte numéro carte.')
    elif num_carte in num_cartes:
        etat_carte = db.carte_info(num_carte)[5]
        if not etat_carte:  # Si la carte Invalide
            ecran.insert(INSERT, '\n\n\n Invalide carte')
            card_num_entry.configure(state='readonly')
            carte_pic.pack_forget()
            avale_pic.pack()
        else:  # Cas favorable
            code_secret = ''
            code.set(code_secret)
            card_info = db.carte_info(num_carte)
            enter_button.configure(command=lambda: enter_code(card_info))
            ecran.delete(0.0, END)
            ecran.insert(INSERT, '\n Entrez votre code secret :')
            carte_pic.pack_forget()
            avale_pic.pack_forget()
            card_num_entry.delete(0, END)
            card_num_entry.place_forget()
            code_pic.pack()
            code_entry.delete(0, END)
            code_entry.place(x=110, y=80)
            code_entry.focus()
            code_entry.focus_set()
    ecran.configure(state=DISABLED)


def enter_code(card_info):
    """Verification code PIN"""
    global num_carte, code_secret, montant, count
    ecran.configure(state=NORMAL)
    ecran.delete(3.0, END)
    code_card = card_info[3]
    code_secret = code.get()
    num_card = card_info[2]

    if not code_secret:
        ecran.insert(INSERT, '\n\n\n Tapez le code SVP.')

    elif int(code_secret) != code_card:
        count += 1
        while count < 3:
            ecran.insert(INSERT, f'\n\n\n Code erroné {count} fois.')
            break
        else:
            code_entry.place_forget()
            code_pic.pack_forget()
            avale_pic.pack()
            ecran.delete(0.0, END)
            ecran.insert(INSERT, '\n\n\n Code erroné 3 fois de suite.')
            db.change_etat(False, num_card)

    else:  # Cas favorable
        Nom_prenom.set(db.client_info(card_info[1])[1])
        code_clt.set(card_info[1])
        no_carte.set(num_card)
        solde.set(f'{db.compte_info(card_info[1])[2]:.2f}')
        date.set(card_info[4])
        solde_actual = float(solde.get())
        num_compte = card_info[0]
        enter_button.configure(command=lambda: enter_money(num_compte, solde_actual))
        second_frame.pack_forget()
        info_frame.pack(side='left', ipadx=20)
        ecran.delete(0.0, END)
        ecran.insert(INSERT, '\n Tapez le montant :')
        code_entry.place_forget()
        count = 0
        montant = ''
        amount.set(montant)
        amount_entry.place(x=110, y=85)
        amount_entry.focus()
        amount_entry.focus_set()
    ecran.configure(state=DISABLED)


def enter_money(num_compte, solde_actual):
    """Verification amount"""
    global num_carte, code_secret, montant
    ecran.configure(state=NORMAL)
    ecran.delete(3.0, END)
    montant = amount.get()

    if not montant:
        ecran.insert(INSERT, '\n\n\n Tapez un montant SVP.')
    else:
        try:
            money = float(montant)
        except ValueError:
            ecran.insert(INSERT, '\n\n\n Tapez un montant SVP.')
        else:
            if money <= solde_actual:
                solde.set(str(solde_actual - money))
                db.retirer(num_compte, money)
                ecran.insert(INSERT, '\n\n\n Opération réussie.')
                info_frame.pack_forget()
                second_frame.pack(side='left', ipadx=20)
                code_pic.pack_forget()
                money_pic.pack()
                main.after(2500, sleep)
            else:
                ecran.insert(INSERT, '\n\n\n Le montant est supérieur au solde.')


def sleep():
    """sleep for 2500s then show another frame"""
    amount_entry.place_forget()
    money_pic.pack_forget()
    merci_pic.pack()
    ecran.configure(state=NORMAL)
    ecran.delete(0.0, END)
    ecran.tag_configure("center", justify='center')
    ecran.insert(INSERT, '\n\nMerci \nÀ bientôt')
    ecran.tag_add("center", "1.0", "end")
    ecran.configure(state=DISABLED)


def delete():
    """Delete just one number"""
    global num_carte, code_secret, montant
    length_card = len(card_num_entry.get())
    if length_card in [5, 10, 15]:
        num_carte = num_carte[:-2]
        card_num.set(num_carte)
    else:
        num_carte = num_carte[:-1]
        card_num.set(num_carte)

    code_secret = code_secret[:-1]
    code.set(code_secret)

    montant = str(montant)[:-1]
    amount.set(montant)


def clear():
    """Clear all the entry"""
    global num_carte, code_secret, montant
    num_carte = ''
    card_num.set(num_carte)
    code_secret = ''
    code.set(code_secret)
    montant = ''
    amount.set(montant)
    ecran.configure(state=NORMAL)
    ecran.delete(5.0, END)
    ecran.configure(state=DISABLED)
    card_num_entry.delete(0, END)
    card_num_entry.focus_set()
    code_entry.delete(0, END)
    code_entry.focus_set()
    amount_entry.delete(0, END)
    amount_entry.focus_set()


def cancel():
    """Return to the initial state of GUI"""
    global count
    count = 0
    clear()
    ecran.configure(state=NORMAL)
    ecran.delete(0.0, END)
    ecran.insert(INSERT, '\n Entrer votre numéro de carte :')
    ecran.configure(state=DISABLED)
    code_pic.pack_forget()
    avale_pic.pack_forget()
    money_pic.pack_forget()
    merci_pic.pack_forget()
    carte_pic.pack()
    code_entry.place_forget()
    amount_entry.place_forget()
    card_num_entry.configure(state=NORMAL)
    card_num_entry.place(x=110, y=80)
    card_num_entry.focus_set()
    enter_button.configure(command=enter_card)
    info_frame.pack_forget()
    second_frame.pack(side='left', ipadx=20)


# #####################################################################################################
# ######################################__Designing__Part__############################################
# #####################################################################################################

# MAIN Window _________________________________________________________________
main: Tk = Tk()
main.geometry('780x520+280+115')
main.title("Distributeur Automatique de Billets")
main.configure(bg='burlywood4')
main.lift()
main.deiconify()
main.resizable(0, 0)
main.iconbitmap(r'Images\atm.ico')
main.wm_attributes("-topmost", 1)
vld_cmd = (main.register(validate))

# DAB Label ___________________________________________________________________
dab = Label(main, text='DI$TRIBUT£UR AUTOMATIQUE DE BILLETS',
            bg='burlywood4', fg='LightGoldenrod2', anchor='s',
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
date = Label(first_frame,
             text=f"{datetime.now():%d-%m-%Y}",
             fg="azure", bg="gray20",
             font=("Rockwell", 16))
date.place(x=295, y=10)

# L'ecran _____________________________________________________________________
ecran = Text(first_frame, bg='pale green', bd=2,
             fg='gray12', width=25, height=7,
             font=('times', 12),
             relief=SUNKEN, wrap=WORD)
ecran.place(x=80, y=35)
ecran.insert(INSERT, '\n Entrez votre numéro de carte :')
ecran.configure(state=DISABLED)

# Entry card number ___________________________________________________________
card_num = StringVar()
card_num_entry = Entry(first_frame, bg='pale green',
                       fg='gray20', width=18, relief=SOLID,
                       font=('times', 12, 'bold'), justify=CENTER,
                       textvariable=card_num)
card_num_entry.place(x=110, y=80)
card_num_entry.focus()
card_num_entry.focus_set()

# Entry code PIN ___________________________________________________________
code = StringVar()
code_entry = Entry(first_frame, bg='pale green',
                   fg='gray20', width=18, relief=SOLID,
                   font=('times', 12, 'bold'), justify=CENTER,
                   validate=ALL, validatecommand=(vld_cmd, '%P'),
                   show="•", textvariable=code)

# Entry amount ________________________________________________________________
amount = StringVar()
amount_entry = Entry(first_frame, bg='pale green',
                     fg='gray20', width=18, relief=SOLID,
                     font=('times', 12, 'bold'), justify=LEFT,
                     validate=ALL, validatecommand=(vld_cmd, '%P'),
                     textvariable=amount)

# Images _______________________________________________________________________
carte_png = PhotoImage(file=r'Images\carte.png')
carte_pic = Label(second_frame, bg='gray20', justify=CENTER,
                  image=carte_png, compound=CENTER)
carte_pic.pack()

avale_png = PhotoImage(file=r'Images\avalé.png')
avale_pic = Label(second_frame, bg='gray20', justify=CENTER,
                  image=avale_png, compound=CENTER)

code_png = PhotoImage(file=r'Images\code.png')
code_pic = Label(second_frame, bg='gray20', justify=CENTER,
                 image=code_png, compound=CENTER)

money_png = PhotoImage(file=r'Images\money.png')
money_pic = Label(second_frame, bg='gray20', justify=CENTER,
                  image=money_png, compound=CENTER)

merci_png = PhotoImage(file=r'Images\merci.png')
merci_pic = Label(second_frame, bg='gray20', justify=CENTER,
                  image=merci_png, compound=CENTER)


# Buttons _____________________________________________________________________
def num_btn(text, cmd, stt=NORMAL):
    return Button(first_frame, text=text,
                  command=cmd, state=stt,
                  bg='ivory3', bd=4,
                  activebackground='ivory4',
                  fg='black', cursor='hand2',
                  font=('Arial', 14, 'bold'),
                  padx=15, pady=4,
                  relief=GROOVE)


vide1 = num_btn('  ', None, DISABLED).place(x=40, y=380)
vide2 = num_btn('  ', None, DISABLED).place(x=180, y=380)
_0_ = num_btn('0', lambda: press_btn(0)).place(x=110, y=380)
_1_ = num_btn('1', lambda: press_btn(1)).place(x=40, y=200)
_2_ = num_btn('2', lambda: press_btn(2)).place(x=110, y=200)
_3_ = num_btn('3', lambda: press_btn(3)).place(x=180, y=200)
_4_ = num_btn('4', lambda: press_btn(4)).place(x=40, y=260)
_5_ = num_btn('5', lambda: press_btn(5)).place(x=110, y=260)
_6_ = num_btn('6', lambda: press_btn(6)).place(x=180, y=260)
_7_ = num_btn('7', lambda: press_btn(7)).place(x=40, y=320)
_8_ = num_btn('8', lambda: press_btn(8)).place(x=110, y=320)
_9_ = num_btn('9', lambda: press_btn(9)).place(x=180, y=320)

enter_button = Button(first_frame, text='ENTER',
                      bg='forest green', fg='black',
                      activebackground='dark green', bd=4,
                      font=('Arial', 11, 'bold'),
                      cursor='hand2', pady=7,
                      command=enter_card, relief=GROOVE)
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

# Client Info _________________________________________________________________
Label(info_frame, text='SYSTÈME BANCAIRE',
      bg='gray20', fg='old lace', anchor='s',
      font=('Rockwell', 20, 'bold', 'underline'),
      bd=3, justify='center').place(x=20, y=20)

Label(info_frame, text='Bienvenue dans votre compte:',
      bg='gray20', fg='old lace', anchor='s',
      font=('times', 16)).place(x=0, y=75)

# Nom & Prenom ----------------------------------
Label(info_frame, text='⮚ Nom & Prénom:',
      bg='gray20', fg='old lace', anchor='s',
      font=('times', 16)).place(x=0, y=120)

Nom_prenom = StringVar()
Entry(info_frame,
      fg='gray18', width=18,
      font=('times', 12, 'bold'),
      relief=SUNKEN, textvariable=Nom_prenom,
      state='readonly').place(x=180, y=122)

# Code client -----------------------------------
Label(info_frame, text='⮚ Code client:',
      bg='gray20', fg='old lace', anchor='s',
      font=('times', 16)).place(x=0, y=170)

code_clt = StringVar()
Entry(info_frame,
      fg='gray18', width=18,
      font=('times', 12, 'bold'),
      relief=SUNKEN, textvariable=code_clt,
      state='readonly').place(x=180, y=172)

# Num carte -------------------------------------
Label(info_frame, text='⮚ Numéro de carte:',
      bg='gray20', fg='old lace', anchor='s',
      font=('times', 16)).place(x=0, y=220)

no_carte = StringVar()
Entry(info_frame,
      fg='gray18', width=18,
      font=('times', 12, 'bold'),
      relief=SUNKEN, textvariable=no_carte,
      state='readonly').place(x=180, y=222)

# Solde -----------------------------------------
Label(info_frame, text="⮚ Solde: ",
      bg='gray20', fg='old lace', anchor='s',
      font=('times', 16)).place(x=0, y=270)

solde = StringVar()
Entry(info_frame,
      fg='gray18', width=18,
      font=('times', 12, 'bold'),
      relief=SUNKEN, textvariable=solde,
      state='readonly').place(x=180, y=272)

# Date d'expiration -----------------------------
Label(info_frame, text="⮚ Date d'expiration: ",
      bg='gray20', fg='old lace', anchor='s',
      font=('times', 16)).place(x=0, y=320)

date = StringVar()
Entry(info_frame,
      fg='gray18', width=18,
      font=('times', 12, 'bold'),
      relief=SUNKEN, textvariable=date,
      state='readonly').place(x=180, y=322)

main.mainloop()
