from django.db import models

# Create your models here.

class User(models.Model):

	SEX = (('M', 'Male'), ('F', 'Female'))
	MARITAL = (('Single', 'Single'),('Married', 'Married'))
	BRANCH = (('CSE','Computer Science & Engineering'),
		('EEE','Electrical & Electronics Engineering'),
		('ECE','Electronics & Communications Engineering'),
		('EBE','Electronics & Biomedical Engineering'),)
	username = models.CharField(max_length = 20,primary_key = True)
	roll_number = models.CharField(max_length = 10)
	first_name = models.CharField(max_length = 15)
	middle_name = models.CharField(max_length = 15,blank = True)
	last_name = models.CharField(max_length = 15)
	sex = models.CharField(max_length = 1, choices = SEX, default = 'M')
	dob = models.DateField()
	branch = models.CharField(max_length = 3, choices = BRANCH, default = 'CSE')
	phone = models.CharField(max_length = 15)
	email = models.EmailField()
	alt_email = models.EmailField(blank = True)
	location = models.CharField(max_length = 20)
	display_pic = models.ImageField(blank = True)

	def __str__(self):
		return self.username
	
class WorkExperience(models.Model):
	username = models.OneToOneField(User,on_delete = models.CASCADE)
	company = models.CharField(max_length = 20)
	description = models.CharField(max_length = 300)
	start_year = models.IntegerField()
	end_year = models.IntegerField()
	position = models.CharField(max_length = 20)

	def __str__():
		return self.company + self.postition

class BroadcastMessage(models.Model):
	message = models.CharField(max_length = 500)
	dated = models.DateField()

class SocialMedia(models.Model):
	username = models.ForiegnKey(User)
	website = models.CharField(max_length = 20)
	web_id = models.CharField(max_length = 20)
