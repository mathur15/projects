import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quatity INTEGER, price REAL)")
    curr.execute("INSERT INTO store VALUES ('Wine Glass',8,10.5)")
    conn.commit()
    conn.close()

def insert(item, quantity,price):
    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()

    curr.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))

    conn.commit()
    conn.close()


def view():

    conn = sqlite3.connect("lite.db")
    curr = conn.cursor()

    curr.execute("SELECT * FROM store")
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(item_stored):
    conn = sqlit3.connect("lite.db")
    curr = conn.cursor()

    curr.execute("DELETE FROM store WHERE item =?",(item_stored,))

    conn.commit()
    conn.close()

def update(quantity,item_stored):
    conn = sqlite3.connect("lit.db")
    curr = conn.cursor()

    curr.execute("UPDATE store SET quantity=? WHERE item =?",(quantity,item_stored,))

    conn.commit()
    conn.close()



insert("Coffee",10,5)
print(view())
