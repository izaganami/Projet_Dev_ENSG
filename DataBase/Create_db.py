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
        print("Création de la table")


    except (Exception, psycopg2.DatabaseError) as error :
        print ("Erreur", error)

    finally:
        # FERMETURE DE LA BDD
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == "__main__":

    count_query = '''CREATE TABLE "etudiants" (
    id int, 
    domicile_courant integer, 
    domicile_familial integer, 
    lieu_etude integer, 
    lieu_travail integer,
    trajet_courant_familial integer,
    trajet_courant_etude integer,
    trajet_courant_travail integer,
    filiere text,
    bourse boolean
    );
    '''
    faire_requete(count_query)