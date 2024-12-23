class Animal:
    def __init__(self,nom,espece,age):
        self.nom = nom
        self.espece = espece
        self.__age = age

    def getAge(self):
        return self.__age
    def affiche_Info(self):
        return f'Nom : {self.nom} , Espece : {self.espece} , Age : {self.getAge()}'

class Refuge:
    def __init__(self):
        self.animaux = []

    def Ajouter_Animaux(self,animal):
        self.animaux.append(animal)

    def Afficher_Animaux(self):
        for animal in self.animaux:
            print(animal.affiche_Info())

    def Adopter_Animal(self, nom):
        for animal in self.animaux:
            if animal.nom == nom:
                self.animaux.remove(animal)
                print(f'Adoption de {nom} avec succes')
                return
        print(f"Aucun animal nommé {nom} trouvé dans le refuge")

    def Adopte_Animal(self):
        self.Afficher_Animaux()
        nom = str(input("Veuillez donner le nom de l'animal : "))
        self.Adopter_Animal(nom)




if __name__ == "__main__":
    Animal_1 = Animal("Bobby","chien",2)
    Animal_2 = Animal("Mouss","chat",2)

    Refuge = Refuge()

    Refuge.Ajouter_Animaux(Animal_1)
    Refuge.Ajouter_Animaux(Animal_2)

    Refuge.Adopte_Animal()







