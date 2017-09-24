import psycopg2

def create_table():
    conn = psycopg2.connect("dbname = 'Database1' user='postgres' password = 'postgres123' host ='localhost' port='5432'")
    curr = conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quatity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity,price):
    conn = psycopg2.connect("dbname = 'Database1' user='postgres' password = 'postgres123' host ='localhost' port='5432'")
    curr = conn.cursor()

    curr.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))

    conn.commit()
    conn.close()


def view():

    conn = psycopg2.connect("dbname = 'Database1' user='postgres' password = 'postgres123' host ='localhost' port='5432'")
    curr = conn.cursor()

    curr.execute("SELECT * FROM store")
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(item_stored):
    conn = psycopg2.connect("dbname = 'Database1' user='postgres' password = 'postgres123' host ='localhost' port='5432'")
    curr = conn.cursor()

    curr.execute("DELETE FROM store WHERE item =%s",(item_stored,))

    conn.commit()
    conn.close()

def update(quantity,item_stored):
    conn = psycopg2.connect("dbname = 'Database1' user='postgres' password = 'postgres123' host ='localhost' port='5432'")
    curr = conn.cursor()

    curr.execute("UPDATE store SET quantity=%s price =%s WHERE item =%s",(quantity,price,item_stored))

    conn.commit()
    conn.close()


create_table()
insert("apple",10,15)
insert("Orange",15,20)
print(view())
#insert("Coffee",10,5)
#print(view())
