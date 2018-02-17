from django.db import models
# Create your models here.

class listemail(models.Model):
	email = models.CharField(max_length=256)
    # listemail model is a class that subclasses django.db.models.Model inheriting its attributes
    # Model class lives in django.db.models.base and is imported into the
    # __init__.py file in that directory thus can be referenced as models.Model


class formcontact(models.Model):
	name = models.CharField(max_length=70)
	email = models.CharField(max_length=256)
	msg = models.CharField(max_length=1000)

    # Think of migrations as a version control system for the database schema
    # perform a migration when changes made to models.py
    #     $python3 manage.py makemigrations contact

    # Now that the migration file is created, apply it to the database
    #     $python3 manage.py migrate contact  

    # View migrations
    #     $python3 manage.py showmigrations --list