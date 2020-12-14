from django import TestCase
from watch.forms import ProfileForm, SearchForm, BioForm, PictureForm, RegistrationForm

class TestForms(TestCase):
	
	def test_profileForm_valid(self):
		form = ProfileForm(data={
		'profile_bio': 'this is a bio',
		'profile_fname': 'John',
		'profile_lname': 'Ber'
		})
		self.assertTrue(form.is_valid())