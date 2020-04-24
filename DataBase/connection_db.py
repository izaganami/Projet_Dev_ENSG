
import psycopg2
from psycopg2 import Error

connection=0


def faire_requete(requete):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "mdp",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "carto_etudiant")

        cursor = connection.cursor()


        #POUR EXECUTER UNE REQUÊTE
        cursor.execute(requete)
        connection.commit()
        print("Ajout des lignes")


    except (Exception, psycopg2.DatabaseError) as error :
        print ("Erreur", error)

    finally:
        # FERMETURE DE LA BDD
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == "__main__":

    count_query = '''INSERT INTO "etudiants" (id, domicile_courant, lieu_etude)
VALUES (1, '{1.32,10.23}', '{1.44,23.77}');'''
    faire_requete(count_query)