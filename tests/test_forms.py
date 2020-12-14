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
		
	def test_profileForm_invalidNoData(self):
		form = ProfileForm(data={})
		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 3)
		
	def test_searchForm(self):
		form = SearchForm(data={
			'search_field': 'whiplash'
		})
		self.assertTrue(form.is_valid())
		
	def test_searchForm_invalidNoData(self):
		form = SearchForm(data={})
		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 1)
		
	def test_bioForm(self):
		form = Bioform(data={
			'profile_bio': 'this is the bio'
		})
		self.assertTrue(form.is_valid())
		
	def test_bioForm_tooLong(self):
		form = Bioform(data={
			'profile_bio': 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'
		})
		self.assertFalse(form.is_valid())
		
	def test_pictureForm_Valid(self):
		form = PictureForm(data={
			'profile_image': 'WhatToWatch/static/LogoColor.png'
		})
		self.assertTrue(form.is_valid())
		
	def test_pictureForm_Default(self):
		form = PictureForm(data={})
		self.assertTrue(form.is_valid())