from django.db import models

class CFA(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    numero_siret = models.CharField(max_length=14)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    numero_securite_sociale = models.CharField(max_length=15)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=255)
    cfa = models.ForeignKey(CFA, on_delete=models.CASCADE)
    invite_par = models.ForeignKey(CFA, related_name='invitations', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
