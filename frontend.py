from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple   
    index = box.curselection()[0]
    selected_tuple = box.get(index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[1])
    author_entry.delete(0,END)
    author_entry.insert(END, selected_tuple[2])
    year_entry.delete(0,END)
    year_entry.insert(END, selected_tuple[3])
    isbn_entry.delete(0,END)
    isbn_entry.insert(END,selected_tuple[4])

def view_command():
    box.delete(0, END)
    for row in backend.view():
        box.insert(END, row)

def search_command():
    box.delete(0, END)  
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        box.insert(END, row)

def add_command():
    backend.insert(title = title_text.get(), author = author_text.get(), year = year_text.get(), isbn = isbn_text.get())
    box.delete(0, END)
    box.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get()  )

window = Tk()

title = Label(window, text= "Title")
title.grid(row = 0, column = 0)

title_text = StringVar()
title_entry = Entry(window, textvariable = title_text)
title_entry.grid(row = 0, column = 1)

author = Label(window, text = "Author")
author.grid(row = 0, column = 2)

author_text = StringVar()
author_entry = Entry(window, textvariable = author_text)
author_entry.grid(row = 0, column = 3)

year = Label(window, text = "Year")
year.grid(row = 1, column = 0)

year_text = StringVar()
year_entry = Entry(window, textvariable = year_text)
year_entry.grid(row = 1, column = 1)

isbn = Label(window, text = "ISBN")
isbn.grid(row =1, column = 2)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable = isbn_text)
isbn_entry.grid(row = 1, column = 3)

box = Listbox(window, height = 6, width = 35)
box.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb = Scrollbar(window)
sb.grid(row  =2, column = 2, rowspan = 6)
box.configure(yscrollcommand = sb.set)
sb.configure(command = box.yview)

box.bind("<<ListboxSelect>>", get_selected_row)

view = Button(window,text = "View All", width = 12, command = view_command)
view.grid(row = 2, column  =3)

search = Button(window, text = "Search Entry", width = 12, command = search_command)
search.grid(row = 3, column = 3)

add = Button(window, text = "Add Entry", width = 12, command = add_command)
add.grid(row = 4, column = 3)

update = Button(window, text = "Update Selected", width = 12, command = update_command)
update.grid(row = 5, column = 3)

delt = Button(window, text = "Delete Selected", width = 12, command = delete_command)
delt.grid(row = 6, column = 3)

close = Button(window, text = "Close", width = 12, command = window.destroy)
close.grid(row = 7, column = 3)

window.mainloop()

