class Carnivore:
    def __init__(self,nom,type_viande):
        self.nom = nom
        self.type_viande = type_viande

    def Manger(self):
        return f'Je mange de la viande'
class Herbivore:
    def __init__(self, nom, type_plante):
        self.nom = nom
        self.type_plante = type_plante
    def Manger(self):
        return f'Je mange de l herbe '
class Omnivore(Carnivore,Herbivore):
    def __init__(self,nom,poids,type_viande,type_plante):
        Carnivore.__init__(self,nom,type_viande)
        Herbivore.__init__(self,nom,type_plante)
        self.poids = poids

    def Manger(self):
          return f'Je mange de tout'

Herbivore = Herbivore()
Omnivore = Omnivore()

print(Herbivore.Manger())
print(Omnivore.Manger())