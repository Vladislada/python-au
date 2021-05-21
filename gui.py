from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

def add():

    books.append(message.get())
    print(books)
    messagebox.showinfo('Done', 'Добавлена книга: '+message.get())
    variable = StringVar(root)
    variable.set(books[0])
    w = OptionMenu(root, variable, *books)
    w.place(relx=.3, rely=.3, anchor='c')
def delete():
    messagebox.showinfo('Done', 'Вы добавили книгу '+message.get()+' в список прочитанных')
    print("It is "+message.get())
    f = open('Книга с follentass.txt', 'w+')
    f.write(''+message.get()+' ')
    try:
        books.remove(message.get())
    except:
        pass
    f.close()
    variable = StringVar(root)
    variable.set(books[0])
    w = OptionMenu(root, variable, *books)
    w.place(relx=.3, rely=.3, anchor='c')

root = Tk()
root.title('Книга с follentass')
root.geometry('800x300')
message = StringVar()

message_entry = Entry(textvariable=message,width=52)
message_entry.place(relx=.3, rely=.1, anchor='c')

message_button = ttk.Button(text='Добавить',width=30, command=add)
message_button.place(relx=.7, rely=.1, anchor='c')

books = ['Выберите прочитанную книгу из списка ниже',
       'Бремя страстей человеческих',
       'Собор Парижской Богоматери',
       'Остриё бритвы',
       'Бойцовский клуб',
       'Война и мир',
       'Анна Каренина',
       'Джейн Эйр',
       'Грозовой перевал']

variable = StringVar(root)
variable.set(books[0])

w = OptionMenu(root, variable, *books)
w.place(relx=.3, rely=.3, anchor='c')

message_button = ttk.Button(text='Добавить в прочитанные',width=30, command=delete)
message_button.place(relx=.7, rely=.3, anchor='c')

root.mainloop()
