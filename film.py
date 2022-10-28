from connection_utility import MySql

class Film:

    def getAllFilm(self):
        a = MySql()
        a.execute("select * from film")
        all_film = a.fetchall()

        return all_film

    def getFilmByLength(self, length):
        b = MySql()
        b.execute("select * from film where length > 120")
        all_film_by_length = b.fetchall()

        return all_film_by_length

film = Film()

print(film.getAllFilm())
print(film.getFilmByLength("120"))