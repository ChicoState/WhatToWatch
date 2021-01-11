from django.test import TestCase

# Create your tests here.
class TestUrls(TestCase):

	def test_


class TestForms(TestCase):

	def test_ProfileForm(self):
	profileForm = ProfileForm()
	profileForm.profile_bio = "this is a bio"
	profileForm.profile_fname = "John"
	profileForm.profile_lname = "Smith"
	
	