from django.test import TestCase

# Create your tests here.
#objects = models.Manager()  # This is not needed, it’s automatically provided by Django



from django.contrib.auth.models import User
user = User.objects.get(username='postgres')
user.set_password('vova')
user.save()
