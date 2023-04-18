import sqlite3
import os

DB_NAME = 'db_movies.db'

# Se conecta a la DB y si no existe en el path especificado [db] la crea
def connect_to_database(db):
    con = sqlite3.connect(db)
    return con, con.cursor()


# Para hacer cualquier func siguiente debe existir una conexion (con) y un cursor en la DB
#! con, cursor = connect_to_database(DB_NAME)
# Todo: pasar create_table y delete_table a storage 
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS movie(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, year INTEGER NOT NULL, score REAL)")

def delete_table():
    cursor.execute("DROP TABLE IF EXISTS movie")

# def add_primary_key():
#     cursor.execute("ALTER TABLE movie ADD COLUMN id INTEGER PRIMARY KEY AUTOINCREMENT")
#     con.commit()

def save_movie(title, year, score):
    cursor.execute("""INSERT INTO movie 
                (title, year, score) VALUES 
                (?, ?, ?)
            """, (title, year, score))
    con.commit()
    print(f"Película '{title}' almacenada exitosamente ")

def delete_movie(id):
    cursor.execute("""DELETE FROM movie
            WHERE id = ?
    """, (id, ))
    con.commit()
    print(f"Película '{id}' eliminada exitosamente")

def get_all_movies():
    cursor.execute("SELECT * FROM movie")
    lista_movies = cursor.fetchall()
    return lista_movies


def db_exist(db):
    if os.path.exists(db):
        print("True - La base de datos existe en la ubicación especificada.")
    else:
        print("False - La base de datos no existe en la ubicación especificada.")


print("***------------------------- ------------------------- -------------------------***")
# con, cursor = connect_to_database(DB_NAME)
db_exist('D:\katar\python - Bootcamp\movies_project_loopgk\db_movies.db')
# create_table()
# delete_table()
# add_primary_key()
# save_movie('Gwr', 2013, 7.4)
# delete_movie(7)
# print( get_all_movies() )
# print("DB modificada: db_movies")
print("***------------------------- ------------------------- -------------------------***")