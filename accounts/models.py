from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(null=True,unique=True)
	phone_number = models.IntegerField(null=False)

	avatar = models.ImageField(null=True, default="avatar.svg")

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
\

	

class UserDetails(models.Model):
	'''detail interests of the user inorder to establish there relationships
	# 
	# jsonDec = json.decoder.JSONDecoder()->retireve list from datadase
    # myPythonList = jsonDec.decode(myModel.myList)
	'''

	'''store list into database'''

	# myModel = MyModel()
	# listIWantToStore = [1,2,3,4,5,'hello']
	# myModel.myList = json.dumps(listIWantToStore)
	# myModel.save()
	
	interest =  models.TextField(null=True) # JSON-serialized (text) version of your list
	country =  models.CharField(max_length=30)
	city =  models.CharField(max_length=30)
	lng =  models.CharField(max_length=30)
	lat =  models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
