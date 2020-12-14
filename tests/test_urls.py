from django.test import TestCase
from django.urls import reverse, resolve
from watch.views import home, specific_movie, profile_view, login_view, logout_view, signup, room
class TestUrls(TestCase):

	def test_url_blank(self):
		url = reverse('blank')
		self.assertEquals(resolve(url).func, blank)
		
	def test_url_home(self):
		url = reverse('homepage')
		self.assertEquals(resolve(url).func, home)
		
	def test_url_login_view(self):
		url = reverse('login')
		self.assertEquals(resolve(url).func, login_view)
		
	def test_url_logout_view(self):
		url = reverse('logout')
		self.assertEquals(resolve(url).func, logout_view)
		
	def test_url_signup(self):
		url = reverse('signup')
		self.assertEquals(resolve(url).func, signup)
		
	def test_url_profile_view(self):
		url = reverse('profile')
		self.assertEquals(resolve(url).func, profile_view)
		
	def test_url_room(self):
		url = reverse('room')
		self.assertEquals(resolve(url).func, room)