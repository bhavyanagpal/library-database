import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(Id integer PRIMARY KEY, Title text, Author Text, Year integer,Isbn integer)")
    conn.commit() 
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books") 
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title = "", author = "", year = "", isbn = ""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(ide):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE Id = ?", (ide, ))
    conn.commit() 
    conn.close()

def update(ide, title , author , year , isbn ):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, ide))
    conn.commit()
    conn.close()
    

connect()    
#insert("The Sun", "John Smith", 1918, 745123)
#print(view())
#update(id= 1, title = "Chain of Gold", isbn = 123456, author = "Cassandra Clare", year = 2020)
#print(view())

 