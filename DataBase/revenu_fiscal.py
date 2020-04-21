import numpy as np
import matplotlib.pyplot as plt


# Modèle exponentiel
def calcul_exp(rev_fin,rev_init,seuil,dist):
    """
    Calcule le revenu fiscal moyen des foyers
     
    param rev_fin : revenu fiscal moyen limite quand la distance tant vers l'infini
    type rev_fin : float
    param rev_init : revenu fiscal moyen des familles habitant sur le lieu d'étude
    type rev_init : float
    param seuil : distance type
    type seuil : float
    param dist : tableau des distances dont on souhaite connaître le revenu fiscal moyen
    type dist : array
    
    return : tableau des revenus fiscaux moyens 
    rtype : array
    """
    revenus = (rev_fin-rev_init)*(1-np.exp(-dist/seuil)) +rev_init
    return revenus

def estime_revenu(rev_moyen,ecart_type):
    """
    Calcule le revenu fiscal à l'aide d'une loi normale
    
    param rev_moyens : revenu fiscal moyen (moyenne de la loi normale)
    type rev_fin : array
    param ecart_type : écart type de la loi normale
    type ecart_type : float
    
    """
    return np.random.randn(1)*ecart_type+rev_moyen

abscisse = np.linspace(0,1000,1000)

rev_init = 20000
rev_fin = 40000
dist = 200
seuil = 300

rev_moyen = calcul_exp(rev_fin,rev_init,seuil,dist)
print(rev_moyen)
ecart_type = 5000

revenu_fisc = estime_revenu(rev_moyen,ecart_type)

# Affichage de la courbe
ordonnee = calcul_exp(rev_fin,rev_init,seuil,abscisse)

plt.figure()
plt.plot(abscisse,ordonnee)
plt.title("Revenu fiscal moyen par foyer en fonction de la distance")
plt.xlabel("Distance en km")
plt.ylabel("Revenu fiscal moyen par foyer en €")
plt.grid()
plt.show()

print("Le revenu fiscal est : "+str(revenu_fisc[0])+" €")
    