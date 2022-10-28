from connection_utility import MySql

class Film:

    def getAllFilm(self):
        a = MySql()
        a.execute("select * from film")
        all_film = a.fetchall()

        return all_film

film = Film()

print(film.getAllFilm())