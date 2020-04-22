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

def estime_revenu(rev_moyen=17000,ecart_type=2000):
    """
    Calcule le revenu fiscal à l'aide d'une loi normale
    
    param rev_moyen : revenu fiscal moyen (moyenne de la loi normale)
    type rev_fin : float (par défaut l'étudiant est boursier le revenu moyen est de 17000€)
    param ecart_type : écart type de la loi normale
    type ecart_type : float (par défaut pour les boursiers l'écart type des revenus est de 2000€)
    
    """
    return np.random.randn(1)*ecart_type+rev_moyen

abscisse = np.linspace(0,1000,1000)
est_boursier = False

rev_init = 23000
rev_fin = 40000
dist = 0
seuil = 300

rev_moyen = calcul_exp(rev_fin,rev_init,seuil,dist)
ecart_type = 5000

# Si l'étudiant est boursier, on garde les valeurs par défaut, sinon on utilise les valeurs adaptées à la distance
if est_boursier:
    revenu_fisc = estime_revenu()
else:
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
    
