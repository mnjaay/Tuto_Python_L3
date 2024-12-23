# Classe représentant un animal
class Animal:
    # Constructeur pour initialiser un animal avec un nom, une espèce et un âge
    def __init__(self, nom, espece, age):
        self.nom = nom  # Nom de l'animal (public)
        self.espece = espece  # Espèce de l'animal (public)
        self.__age = age  # Âge de l'animal (privé)

    # Méthode pour accéder à l'âge (encapsulation)
    def getAge(self):
        return self.__age

    # Méthode pour afficher les informations de l'animal
    def affiche_Info(self):
        return f'Nom : {self.nom} , Espece : {self.espece} , Age : {self.getAge()}'

# Classe représentant un refuge animalier
class Refuge:
    # Constructeur pour initialiser le refuge avec une liste vide d'animaux
    def __init__(self):
        self.animaux = []  # Liste pour stocker les animaux dans le refuge

    # Méthode pour ajouter un animal dans le refuge
    def Ajouter_Animaux(self, animal):
        self.animaux.append(animal)  # Ajoute un objet Animal à la liste des animaux

    # Méthode pour afficher tous les animaux présents dans le refuge
    def Afficher_Animaux(self):
        for animal in self.animaux:
            print(animal.affiche_Info())  # Affiche les informations de chaque animal

    # Méthode pour adopter un animal par son nom
    def Adopter_Animal(self, nom):
        for animal in self.animaux:
            if animal.nom == nom:  # Vérifie si un animal avec le nom donné existe
                self.animaux.remove(animal)  # Supprime l'animal de la liste
                print(f'Adoption de {nom} avec succes')  # Confirme l'adoption
                return
        print(f"Aucun animal nommé {nom} trouvé dans le refuge")  # Si l'animal n'existe pas

    # Méthode pour interagir avec l'utilisateur et permettre une adoption
    def Adopte_Animal(self):
        self.Afficher_Animaux()  # Affiche tous les animaux disponibles
        nom = str(input("Veuillez donner le nom de l'animal : "))  # Demande le nom de l'animal à adopter
        self.Adopter_Animal(nom)  # Tente l'adoption

# Bloc principal pour exécuter le programme
if __name__ == "__main__":
    # Création de deux animaux
    Animal_1 = Animal("Bobby", "chien", 2)
    Animal_2 = Animal("Mouss", "chat", 2)

    # Création du refuge
    Refuge = Refuge()

    # Ajout des animaux au refuge
    Refuge.Ajouter_Animaux(Animal_1)
    Refuge.Ajouter_Animaux(Animal_2)

    # L'utilisateur interagit pour adopter un animal
    Refuge.Adopte_Animal()
