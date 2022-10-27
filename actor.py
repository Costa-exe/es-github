from connection_utility import MySql

class Actor:

    def getAllActors(self):
        a = MySql()
        a.execute("select * from actor")
        all_actors = a.fetchall()
        a.close_connection()

        return all_actors

    def getAllActorsByFilm(self, filmTitle):
        b = MySql()
        b.execute(f"select a.first_name, a.last_name from actor a, film_actor fa, film f where a.actor_id = fa.actor_id and fa.film_id = f.film_id and f.title = '{filmTitle}'")
        all_actors_by_film = b.fetchall()
        b.close_connection()

        return all_actors_by_film


actors = Actor()

print(actors.getAllActors())
print(actors.getAllActorsByFilm('ACADEMY DINOSAUR'))