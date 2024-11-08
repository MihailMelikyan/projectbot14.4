import sqlite3

connect = sqlite3.connect("database.db")
curs = connect.cursor()

curs.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price TEXT
);
''')


def get_all_products(id, title, description, price):
    check = curs.execute("SELECT FROM * Products WHERE id=?", (id,))

    if check.fetchone() is None:
        curs.execute(f'''
INSERT INTO Products VALUES('{id}','{title}','{description}','{price}')
''')
    connect.commit()


connect.commit()
connect.close()
