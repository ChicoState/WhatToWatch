from django.test import TestCase, Client
from django.urls import reverse
from watch.models import UserM, Profile
from watch.views import home, specific_movie, profile_view, login_view, logout_view, signup, room

class TestViews(TestCase):
	
	def setUp(self):
		self.client = Client()
		self.home_url = reverse('home')
		self.blank_url = reverse('blank')
		self.profile_url = reverse('profile')
		self.login_url = reverse('login')
		self.signup_url = reverse('signup')
		self.room_url = reverse('room')
		self.moviePage_url = reverse('moviePage')
		
	def test_homeview(self):
		response = self.client.get(self.home_url)
		self.assertEquals(response.status_code, 200) #accessed view correctly
		self.assertTemplateUsed(response, 'watch/templates/home.html') # assert what we tested returned home.html

	def test_blankview(self):
		response = self.client.get(self.blank_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'watch/templates/home.html')
		
	def test_profileview(self):
		response = self.client.get(self.profile_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'watch/templates/profile_page.html')
		
	def test_loginview(self):
		response = self.client.get(self.login_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'watch/templates/login.html')
		
	def test_signupview(self):
		response = self.client.get(self.signup_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'watch/templates/signup.html')
	def test_roomview(self):
		response = self.client.get(self.room_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'watch/templates/room.html')
		
	def test_moviePageview(self):
		response = self.client.get(self.moviePage_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'watch/templates/specific_movie.html')
