from tkinter import*

print('Привіт, тут тобі потрібно буде відповідати на запитання які я буду запитання')

answer1 = input("Чим чистив зуби Адольф Гітлер")

root = Tk()
tk=Tk()


def geometry(param):
    pass


tk:geometry("1000x500")
def btn1_click(ent=None):
    b12=Label(text="Неправильно, "+ent.get()+"!")
    b12.place(x=120,y=150)
def btn2_click(ent=None):
    b12=Label(text="Неправильно, "+ent.get()+"!")
    b12.place(x=120,y=150)
def btn3_click(ent=None):
    b12 = Label(text="Неправильно, " + ent.get() + "!")
    b12.place(x=120, y=150)
def btn4_click(ent=None):
    b12=Label(text="Правильно, "+ent.get()+"!")
    b12.place(x=120,y=150)
btn1=Button(text="Лимонний сік",command=btn1_click)
btn1.place(x=75,y=75,width=100,height=50)
btn2=Button(text="Зубна паста",command=btn2_click)
btn2.place(x=225,y=75,width=100,height=50)
btn3=Button(text="Вода з сіллю",command=btn3_click)
btn3.place(x=75,y=25,width=100,height=50)
btn4=Button(text="Какаін",command=btn4_click)
btn4.place(x=225,y=25,width=100,height=50)

root.mainloop()