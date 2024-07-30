from tkinter import*
from PIL import Image, ImageTk

tk = Tk()
tk.title('\t\t;)')
tk.config(bg='Lightyellow')
tk.geometry('1000x780+200+20')

#frames
icon_frame = LabelFrame(tk, bg='white', bd=6, relief=GROOVE)
icon_frame.place(x=470, y=75, width=500, height=170)

global photoicon, icon
icon = Image.open('pictures/icon.tif')
icon = icon.resize((485,155), Image.BILINEAR) #, Image.ANTIALIAS
photoicon = ImageTk.PhotoImage(icon)

lbl_img_mini = Label(icon_frame, image=photoicon, bd=4, relief=RIDGE)
lbl_img_mini.place(x=0, y=0, width=485, height=155)

pic_frame = LabelFrame(tk, text='Suraty we bahasy:', font=('Times', 20),  fg='green', bg='Lightyellow', bd=6, relief=GROOVE)
pic_frame.place(x=470, y=250, width=500, height=500)
menu_frame = LabelFrame(tk, text='Menu:', font=('Times', 20),  fg='black', bg='orange')
menu_frame.place(x=10, y=75, width=440, height=400)
bill_frame = LabelFrame(tk, text='Bill:', font=('Times', 20),  fg='black', bg='orange')
bill_frame.place(x=10, y=500, width=440, height=250)

global photoimg_mini, img_mini
img_mini = Image.open('pictures/obed.jpg')
img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
photoimg_mini = ImageTk.PhotoImage(img_mini)

lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
lbl_img_mini.place(x=15, y=1, width=450, height=305)
    
#picture doner
def pic_doner():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/doner1.jpeg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Etli doner mini: Price = 20 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Etli Doner Mini: {doner.get()}pcs')
    bill_text.insert(END, f'\n Etli Doner Mini Total Price: {int(doner.get())*20} TMT\n')


def pic_doner2():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/doner2.jpeg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Etli doner normal: Price = 30 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Etli Doner Normal: {doner.get()}pcs')
    bill_text.insert(END, f'\n Etli Doner Normal Total Price: {int(doner.get())*30} TMT\n')

def pic_doner3():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/doner_big.webp')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Etli doner large: Price = 40 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Etli Doner Large: {doner.get()}pcs')
    bill_text.insert(END, f'\n Etli Doner Large Total Price: {int(doner.get())*40} TMT\n')

#picture burger
def pic_burger():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/burger1.jpg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Burger mini: Price = 50 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Burger Mini: {burg.get()}pcs')
    bill_text.insert(END, f'\n Burger Mini Total Price: {int(burg.get())*50} TMT\n')

def pic_burger2():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/burger4.jpeg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Burger normal: Price = 70 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Burger Normal: {burg.get()}pcs')
    bill_text.insert(END, f'\n Burger Normal Total Price: {int(burg.get())*70} TMT\n')

def pic_burger3():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/burg.jpg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Burger large: Price = 90 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Burger Large: {burg.get()}pcs')
    bill_text.insert(END, f'\n Burger Large Total Price: {int(burg.get())*90} TMT\n')

#picture pizza
def pic_pizza():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/pizza1.webp')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Pizza mini: Price = 60 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Pizza Mini: {piz.get()}pcs')
    bill_text.insert(END, f'\n Pizza Mini Total Price: {int(piz.get())*60} TMT\n')

def pic_pizza2():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/pizza2.jpeg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Pizza normal: Price = 80 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Pizza Normal: {piz.get()}pcs')
    bill_text.insert(END, f'\n Pizza Normal Total Price: {int(piz.get())*80} TMT\n')

def pic_pizza3():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/pizza3.jpeg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Pizza large: Price = 100 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Pizza Large: {piz.get()}pcs')
    bill_text.insert(END, f'\n Pizza Large Total Price: {int(piz.get())*100} TMT\n')

#picture manty
def pic_manty():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/manry2.jpeg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Manty mini: Price = 20 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Manty Mini: {man.get()}pcs')
    bill_text.insert(END, f'\n Manty Mini Total Price: {int(man.get())*20} TMT\n')

def pic_manty2():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/manty3.webp')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Manty normal: Price = 30 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Manty Normal: {man.get()}pcs')
    bill_text.insert(END, f'\n Manty Normal Total Price: {int(man.get())*30} TMT\n')

def pic_manty3():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/manty1.webp')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Manty large: Price = 40 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Manty Large: {man.get()}pcs')
    bill_text.insert(END, f'\n Manty Large Total Price: {int(man.get())*40} TMT\n')

def pic_isken():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/iskender_1.jpg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Iskender mini: Price = 30 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Iskender Mini: {isken.get()}pcs')
    bill_text.insert(END, f'\n Iskender Mini Total Price: {int(isken.get())*30} TMT\n')

def pic_isken2():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/iskender_2.jpg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Iskender normal: Price = 40 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Iskender Normal: {isken.get()}pcs')
    bill_text.insert(END, f'\n Iskender Normal Total Price: {int(isken.get())*40} TMT\n')

def pic_isken3():
    global photoimg_mini, img_mini
    img_mini = Image.open('pictures/iskender_3.jpg')
    img_mini = img_mini.resize((630,305), Image.BILINEAR) #, Image.ANTIALIAS
    photoimg_mini = ImageTk.PhotoImage(img_mini)

    lbl_img_mini = Label(pic_frame, image=photoimg_mini, bd=4, relief=RIDGE)
    lbl_img_mini.place(x=10, y=1, width=450, height=305)

    lbl_price = Label(pic_frame, text='Iskender large: Price = 50 TMT', font=('Times', 14),
            fg='green', bg='white', bd=4, relief=RIDGE)
    lbl_price.place(x=100, y=330, width=300, height=100)

    bill_text.insert(END, '\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    bill_text.insert(END, '\n\n\t\t DONER HOUSE KAFE')
    bill_text.insert(END, '\n Alishir Nowayy street-22, Ashgabat')
    bill_text.insert(END, '\n Contact: +993 65123456')
    bill_text.insert(END, f'\n Iskender Large: {isken.get()}pcs')
    bill_text.insert(END, f'\n Iskender Large Total Price: {int(isken.get())*50} TMT\n')

#name restoran
res_at = Label(tk, text='DONER HOUSE', font=('Times', 30, 'bold'), fg='green', bg='gold', 
            bd=10, relief=GROOVE)
res_at.pack(side=TOP, fill=X)


# menu frame
e_doner = Label(menu_frame, text='Etli doner', bd=3, relief=GROOVE, font=('Times', 20),
        fg='white', bg='black', width=10, height=1)
doner = Entry(menu_frame, font=('Times', 20))
burger = Label(menu_frame, text='Burger', bd=3, relief=GROOVE, font=('Times', 20), 
        fg='white',bg='black', width=10, height=1)
burg = Entry(menu_frame, font=('Times', 20))
pizza = Label(menu_frame, text='Pizza', bd=3,relief=GROOVE, font=('Times', 20), 
        fg='white',bg='black', width=10, height=1)
piz = Entry(menu_frame, font=('Times', 20))
manty = Label(menu_frame, text='Manty', bd=3, relief=GROOVE, font=('Times', 20), 
        fg='white', bg='black', width=10, height=1)
man = Entry(menu_frame, font=('Times', 20))
iskender = Label(menu_frame, text='Iskender', bd=3, relief=GROOVE, font=('Times', 20), 
        fg='white', bg='black', width=10, height=1)
isken = Entry(menu_frame, font=('Times', 20))

e_doner.grid(row=0, column=0)
doner.grid(row=0, column=1, columnspan=4)
burger.grid(row=2, column=0)
burg.grid(row=2, column=1, columnspan=4)
pizza.grid(row=4, column=0)
piz.grid(row=4, column=1, columnspan=4)
manty.grid(row=6, column=0)
man.grid(row=6, column=1, columnspan=4)
iskender.grid(row=8, column=0)
isken.grid(row=8, column=1, columnspan=4)

# button in frame
btn1 = Button (menu_frame, text='small', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_doner)
btn2 = Button (menu_frame, text='small', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_burger)
btn3 = Button (menu_frame, text='small', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_pizza)
btn4 = Button (menu_frame, text='normal', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_doner2)
btn5 = Button (menu_frame, text='normal', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_burger2)
btn6 = Button (menu_frame, text='normal', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_pizza2)
btn7 = Button (menu_frame, text='large', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_doner3)
btn8 = Button (menu_frame, text='large', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_burger3)
btn9 = Button (menu_frame, text='large', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_pizza3)
btn10 = Button (menu_frame, text='small', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_manty)
btn11 = Button (menu_frame, text='normal', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_manty2)
btn12 = Button (menu_frame, text='large', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_manty3)
btn13 = Button (menu_frame, text='small', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_isken)
btn14 = Button (menu_frame, text='normal', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_isken2)
btn15 = Button (menu_frame, text='large', font=('Times', 20, 'bold'), fg='gold', bg='black', command=pic_isken3)

btn1.grid(row=1, column=1)
btn2.grid(row=3, column=1)
btn3.grid(row=5, column=1)
btn4.grid(row=1, column=2)
btn5.grid(row=3, column=2)
btn6.grid(row=5, column=2)
btn7.grid(row=1, column=3)
btn8.grid(row=3, column=3)
btn9.grid(row=5, column=3)
btn10.grid(row=7, column=1)
btn11.grid(row=7, column=2)
btn12.grid(row=7, column=3)
btn13.grid(row=9, column=1)
btn14.grid(row=9, column=2)
btn15.grid(row=9, column=3)

#Bil frame
res_at = Label(bill_frame, text='Check', font=('Times', 18, 'bold'), fg='white', bg='black', 
            bd=10, relief=GROOVE)
res_at.pack(side=TOP, fill=X)

y_scroll = Scrollbar(bill_frame, orient='vertical')
bill_text = Text (bill_frame, font=('Times', 14, 'bold'), yscrollcommand=y_scroll.set)
y_scroll.config(command=bill_text.yview)

y_scroll.pack(side=RIGHT, fill=Y)
bill_text.pack(fill=BOTH, expand= TRUE)

tk.mainloop()