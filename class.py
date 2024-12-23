class Personne:
    def faty(self,nom):
        self.nom = nom

    def __str__(self):
        return f'{self.nom}'


A  = Personne()

A.faty("faty")

print(A)