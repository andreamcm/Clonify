# Universidad del Valle de Guatemala
# Authors: Andrea Maria Cordon Mayen and Cristopher Sebastian Recinos Ramirez
# Id: 16076 and 16005
# main.py
# Clonifyapp main

# All the imports
from django.core.management.base import BaseCommand
import clonifyapp.models as mymodels
from django.contrib.auth.models import User

# Welcome to the app
print ('\nWelcome to Clonify\n')

# Main class and function
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        while (True):
            # Main menu
            print ('\n MAIN MENU')
            print ('Please choose one of the following options')
            print ('1. Sign in\n2. See all users\n3. Log in\n4. Exit')
            # Allow user to select one of the options
            choice = input('What is your choice?')
            # If user's choice is number 1
            if (choice == '1'):
                print ('\nSIGNING IN')
                print ('Users: ', User.objects.all().count())
                name = input('What is your name?: ')
                lastName = input('What is your last name?: ')
                username = input('What is your username?: ')
                email = input('What is your email?: ')
                my_user = User(first_name=name, last_name=lastName, username=username, email=email)
                my_user.save()
                print ('Users: ', User.objects.all().count())