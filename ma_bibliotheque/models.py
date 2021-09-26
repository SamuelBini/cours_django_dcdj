from django.db import models

# Create your models here.

class Auteur(models.Model):
    nom_auteur = models.CharField(max_length=225)
    adr_auteur = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_auteur
    

class Editeur(models.Model):
    nom_edit = models.CharField(max_length=225)
    adr_edit = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_edit

class Rayon(models.Model):
    num_rayon = models.IntegerField()
    loc_rayon = models.CharField(max_length=50)

    def __str__(self):
        return "Rayon {}".format(self.num_rayon)



class Theme(models.Model):
    libelle_th = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle_th



class Mot_Cle(models.Model):
    libelle_mot = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle_mot
    


class Abonné(models.Model):
    nom_abonné = models.CharField(max_length=250)
    adr_abonné = models.CharField(max_length=250)
    tel_abonné = models.CharField(max_length=15)
    date_adh = models.DateField(auto_now_add=True)
    date_nais = models.DateField()
    cat_prof = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_abonné
    

class Livre(models.Model):
    code_livre = models.CharField(max_length=50, unique=True)
    nom_livre = models.CharField(max_length=100)
    rayon = models.ForeignKey(Rayon, on_delete=models.CASCADE)
    mots_clés = models.ManyToManyField(Mot_Cle)
    themes = models.ManyToManyField(Theme)
    auteur = models.ManyToManyField(Auteur)

    def __str__(self):
        return "{} de {}".format(self.nom_livre, self.auteur)


class Exemplaire(models.Model):
    date_acquisition = models.DateField()
    cote_livre = models.CharField(max_length=50, unique=True)
    etat_usure = models.CharField(max_length=50)
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

    def __str__(self):
        return "{} édité par {}".format(self.livre, self.editeur)



class Pret(models.Model):
    date_dem_pret = models.DateField(auto_now_add=True)
    date_pret = models.DateField()
    date_depot = models.DateField()
    date_effective_de_retour = models.DateField()
    livre = models.ManyToManyField(Exemplaire)
    preteur = models.ForeignKey(Abonné, on_delete=models.CASCADE)

    def __str__(self):
        return "Date de demande : {}, Date de prêt : {}, Date de retour : {}".format(self.date_dem_pret, self.date_pret, self.date_depot)
