import sqlite3
# from dotenv import load_dotenv

# load_dotenv()

# DB_NAME = os.getenv('DB_NAME')

DB_NAME = "db_movies.db"
# Todo: hacer una clase de esto

def connect_to_database(db):
    con = sqlite3.connect(db)
    return con, con.cursor()

con, cursor = connect_to_database(DB_NAME)



def get_all_movies():
    cursor.execute("SELECT * FROM movie")
    lista_movies = cursor.fetchall()
    return lista_movies


def get_movie(id):
    cursor.execute("""SELECT * FROM movie
            WHERE id = ?
    """, (id, ))
    one_movie = cursor.fetchall()
    return one_movie

def save_movie(movie):
    cursor.execute("""INSERT INTO movie 
                (title, year, score) VALUES 
                (?, ?, ?)
            """, (movie.title, movie.year, movie.score))
    con.commit()
    print(f"Película '{movie.title}' almacenada exitosamente ")


def delete_movie(id):
    cursor.execute("""DELETE FROM movie
            WHERE id = ?
    """, (id, ))
    con.commit()
    print(f"Película '{id}' eliminada exitosamente")


def edit_movie(id, new_title, new_year, new_score):
    cursor.execute("""UPDATE movie SET 
        title=?, 
        year=?, 
        score=? 
        WHERE id=?
        """, 
        (new_title, new_year, new_score, id)
    )
    con.commit()
    print(f"Película '{id}' editada exitosamente")



# class SQLiteStorage:
#     def __init__(self, db):
#         self.db = db
    
#     def connect_to_database(self):
#         con = sqlite3.connect(self.db)
#         self.con = con
#         self.cursor = con.cursor()
#         return con, con.cursor()

#     def select_all_registers(self, model):
#         cursor.execute(f"SELECT * FROM {model}")
#         all_register = self.cursor.fetchall()
#         return all_register
    
# storage = SQLiteStorage("")

# con, cursor = storage.connect_to_database()

# storage.select_all_registers("Movie")