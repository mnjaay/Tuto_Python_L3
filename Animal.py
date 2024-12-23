class Carnivore:
    def __init__(self, nom, type_viande):
        self.nom = nom  # Nom de l'animal
        self.type_viande = type_viande  # Type de viande qu'il mange

    def Manger(self):
        return f"Je mange de la viande."


class Herbivore:
    def __init__(self, nom, type_plante):
        self.nom = nom  # Nom de l'animal
        self.type_plante = type_plante  # Type de plante qu'il mange

    def Manger(self):
        return f"Je mange de l'herbe."


class Omnivore(Carnivore, Herbivore):
    def __init__(self, nom, poids, type_viande, type_plante):
        # Initialisation des attributs via les classes parentes
        Carnivore.__init__(self, nom, type_viande)
        Herbivore.__init__(self, nom, type_plante)
        self.poids = poids  # Poids de l'animal

    def Manger(self):
        return f"Je mange de tout."


# Création d'instances des classes
herbivore = Herbivore("Lapin", "Carottes")  # Un herbivore mangeant des carottes
omnivore = Omnivore("Ours", 200, "Poisson", "Baies")  # Un omnivore mangeant du poisson et des baies

# Affichage des comportements
print(herbivore.Manger())  # "Je mange de l'herbe."
print(omnivore.Manger())   # "Je mange de tout."
