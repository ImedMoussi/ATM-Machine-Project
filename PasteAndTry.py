# def enter_code(card_info):
#     global num_carte, code_secret, montant, count
#     ecran.configure(state=NORMAL)
#     ecran.delete(3.0, END)
#     code_card = card_info[3]
#     code_secret = code.get()
#     num_card = card_info[2]
#     if count < 3:  # TODO: reni hna nchof nte3 GHADA !!!
#         if not code_secret:
#             ecran.insert(INSERT, '\n\n\n Tapez le code SVP.')
#         elif int(code_secret) != code_card:
#             count += 1
#             ecran.insert(INSERT, f'\n\n\n Code erroné {count} fois.')
#         else:  # Cas favorable
#             count = 0
#             Nom_prenom.set(db.client_info(card_info[1])[1])
#             code_clt.set(card_info[1])
#             no_carte.set(num_card)
#             solde.set(f'{db.compte_info(card_info[1])[2]:.2f}')
#             date.set(card_info[4])
#             solde_actual = float(solde.get())
#             num_compte = card_info[0]
#             enter_button.configure(command=lambda: enter_money(num_compte, solde_actual))
#             second_frame.pack_forget()
#             info_frame.pack(side='left', ipadx=20)
#             ecran.delete(0.0, END)
#             ecran.insert(INSERT, '\n Taper le montant :')
#             code_entry.place_forget()
#             montant = ''
#             amount.set(montant)
#             amount_entry.place(x=110, y=85)
#             amount_entry.focus()
#             amount_entry.focus_set()
#     else:  # count > 3
#         code_entry.place_forget()
#         code_pic.pack_forget()
#         avale_pic.pack()
#         ecran.delete(0.0, END)
#         ecran.insert(INSERT, '\n\n\n Code erroné 3 fois de suite.')
#         db.change_etat(False, num_card)
#     ecran.configure(state=DISABLED)
