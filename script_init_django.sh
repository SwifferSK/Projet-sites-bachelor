#!/bin/bash

sudo apt update -y
sudo apt upgrade -y

python3 -m pip install --upgrade pip
# Installation des paquets nécessaires pour Django
pip3 install django

# Création du projet Django
django-admin startproject django_project

# Se déplacer dans le répertoire du projet
cd django_project

# Création de l'application Django
python3 manage.py startapp bachelor_projects

# Création de l'arborescence pour les fichiers CSS et JavaScript
mkdir -p bachelor_projects/static/bachelor_projects/css
mkdir -p bachelor_projects/static/bachelor_projects/js
mkdir -p bachelor_projects/templates

# Création du fichier base.html avec le contenu "Projet Django Base"
echo "<html><head><title>Projet Django Base</title></head><body><h1>Projet Django Base</h1></body></html>" > bachelor_projects/templates/base.html

# Création du fichier views.py pour l'application bachelor_projects
echo "from django.shortcuts import render

def index(request):
    return render(request, 'base.html')" > bachelor_projects/views.py

# Création du fichier urls.py pour l'application bachelor_projects
echo "from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]" > bachelor_projects/urls.py

# Ajout de l'application bachelor_projects aux applications installées dans les paramètres du projet
sed -i "s/^INSTALLED_APPS = \[/&\n    'bachelor_projects',/" django_project/settings.py

# Effectuer les migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Lancement du serveur Django
python3 manage.py runserver
