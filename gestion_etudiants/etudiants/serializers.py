from rest_framework import serializers
from .models import CFA, Etudiant

class CFASerializer(serializers.ModelSerializer):
    class Meta:
        model = CFA
        fields = ['id', 'nom', 'email', 'numero_siret']

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ['id', 'prenom', 'nom', 'email', 'numero_securite_sociale', 'date_naissance', 'adresse', 'cfa', 'invite_par']
