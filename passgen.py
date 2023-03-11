from random import *
from tkinter import *

num = "0123456789"
alphanum = "abcdefghjklmnopgrstuvwxyz0123456789ABCDEFGHJKLMNOPQRSTUVWXYZ"
spalphanum = "abcdefghjklmnopgrstuvwxyz0123456789ABCDEFGHJKLMNOPQRSTUVWXYZ'#@+(){}^&*%$"

# passlen = int(input("Enter password length \n"))
# randPass = []

# print('Select the type of passwords \n1. Numbers\n2.Alphanum\n3.Special alphanumeric\n')
# Selecttype = int(input())

# if Selecttype == 1:
#     for i in range(passlen):
#         randPass.append(choice(num))
# elif Selecttype == 2:
#     for i in range(passlen):
#         randPass.append(choice(alphanum))
# else:
#     for i in range(passlen):
#         randPass.append(choice(spalphanum))

# result = "".join(randPass)

# print(' Your random password is: '+result)


def Create_Pass():

        TheChoice = Tchoice.get()

        if TheChoice == "":
                resultBox.delete(0.0, END)
                resultBox.insert(END, "\n Select the type of password you'd like")

        length = int(pass_length.get())
        randPass = []
        for i in range(length):
                randPass.append(choice(TheChoice))

        result = "".join(randPass)

        TheResult = "\n *** Your Password is: "+result+" ***\n"

        resultBox.delete(0.0, END)
        resultBox.insert(END, TheResult)





window = Tk()
window.geometry('800x700')
window.title('Random Password Generator by KhoiKode with Python lol')


ProgName = Label(window, font=('Fixedsys', 14, 'bold'),text='Password Generator by KhoiKode (☞ﾟヮﾟ)☞', fg='blue')
ProgName.grid(row=1, column=3, padx=200, pady=30)

ChooseType = Label(window, font=('Fixedsys', 14, 'bold'), text='Choose a type among the 3')
ChooseType.place(relx=.03, rely=.25)

Tchoice = StringVar()
NumChoice = Radiobutton(window, font=('Terminal', 14, 'bold'), text='Numeric', variable= Tchoice, value=num)
NumChoice.place(relx=.3, rely=.35)
AlphaNumChoice = Radiobutton(window, font=('Terminal', 14, 'bold'), text='AlphaNumeric', variable= Tchoice, value=alphanum)
AlphaNumChoice.place(relx=.3, rely=.4)
SpecialChoice = Radiobutton(window, font=('Terminal', 14, 'bold'), text='Special', variable= Tchoice, value=spalphanum)
SpecialChoice.place(relx=.3, rely=.45)

size = Label(window, text='Size', font=('System', 10, 'bold'))
size.place(relx = .65, rely = .4)



pass_length = Spinbox(window, from_=8,to=100)
pass_length.place(relx = .73, rely=.4)
pass_length.config(state="readonly")

GenButton = Button(window, text='Generate',command=Create_Pass)
GenButton.place(relx = .45, rely=.57)

resultBox = Text(window, height=6, width=70)
resultBox.place(relx=.06, rely=.7)


window.mainloop()
