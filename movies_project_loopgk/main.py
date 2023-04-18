import os
from storage import get_all_movies, get_movie, save_movie, delete_movie, edit_movie
from models import Movie


ejecutar_programa = True

def ask_continuar(continuar):
    option = input("¿Desea salir del programa? [y: yes | any: no] ")
    if option == 'y':
        # continuar = not continuar    
        continuar = False    
        print(f"Saliendo del programa")
     
    return continuar
    
menu_opciones = (
    "Salir del programa",
    "Traer todas las películas",
    "Crear una nueva pelicula",
    "Eliminar un registro de la base de datos",
    "Traer una pelicula",
    "Editar una pelicula",
    "pruebas"
)


while ejecutar_programa:
    print("Selecciona una opción... ")
    for opcion, elemento in enumerate(menu_opciones):
        print(f"{opcion} - {elemento}")
    option = int(input(">>> "))
    
    # get all movies
    if option == 1:
        all_movies = get_all_movies() 
        print(all_movies)

    # Save new movie
    elif option == 2:
        movie_title = input("Ingresa el nombre de la pelicula: ")
        movie_year = int(input("Ingresa el año en el que salió la pelicula: "))
        movie_score = float(input("Ingresa la calificación del 1 al 10 que le das a la pelicula: "))
        movie = Movie(title = movie_title, year = movie_year, score = movie_score)
        save_movie(movie)

    # Delete movie by Id
    elif option == 3:
        all_movies = get_all_movies()
        print("Estas son las peliculas almacenadas")
        print("Id  ---  Titulo")
        for movie in all_movies:
            print(f"{movie[0]} --- {movie[1]}")
        movie_id = input("Ingresa el id de la pelicula a eliminar: ")
        delete_movie(movie_id)
    
    # Get 1 movie by Id
    elif option == 4:
        all_movies = get_all_movies()
        print("Estas son las peliculas almacenadas")
        print("Id   |  Titulo")
        for movie in all_movies:
            print(f"{movie[0]} --- {movie[1]}")
        movie_id = input("Ingresa el id de la pelicula: ")
        movie = get_movie(movie_id)
        print(f"Película obtenida exitosamente: {movie} ")

    # Edit a movie by Id
    elif option == 5:
        movie_id        = input("Ingresa el id de la pelicula: ")
        movie_new_title = input("Ingresa el nuevo titulo de la pelicula: ")
        movie_new_year  = input("Ingresa el nuevo año de la pelicula: ")
        movie_new_score = input("Ingresa el nuevo score de la pelicula: ")
        edit_movie(movie_id, movie_new_title,movie_new_year, movie_new_score)
        print("movie Editada ")

    elif option == 6:
        # ask_continuar(ejecutar_programa)
        pass

    else:
        ejecutar_programa = False
        print("Saliendo del programa")
        break

    ejecutar_programa = ask_continuar(ejecutar_programa)
