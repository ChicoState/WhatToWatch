from django.test import TestCase
from watch.models import UserM, Profile

class TestModels(TestCase):

	def setUp(self)
		self.aUser = UserM.objects.create(
			username = 'MovieWatcher'
			email = 'emailad@gmail.com'
			password = 'Movies4Fun!'
		)
		self.aProfile = Profile.objects.create(
			profile_fname = 'Lukas'
			profile_lname = 'Pecson'
			profile_bio = 'I watch movies'
			profile_user = 'movieshine409'
			profile_image = 'WhatToWatch/static/LogoColor.png'
		)
		self.aBadProfile = Profile.objects.create(
			profile_fname = 'qowieuryalsdkjhfzmxcnbvaslkdjfhgqpwoeirytalskdjfgoewfouinemcincvhzikdfvhnaowiudhfcouiohretnaksdjfhgw'
			profile_lname = 'Pecson'
			profile_bio = 'I watch movies'
			profile_user = 'movieshine409'
			profile_image = 'WhatToWatch/static/LogoColor.png'
		)
	def testBadUser(self):
		User = UserM.objects.create(
			username = 'insanemoviegoerneverstopthegrindweoutheremakingbigmoneyandmyusernameisverysuperlongbazingaiamjusttryingtomake'
			email = 'justawholelotofgarbagetbhadkjhfalksjhdfqiviuboqwnduciohusdcqioaijdncpaiodhuvnaopefrdgocaisndlfsasasd@gmail.com'
			password = 'qowieuryalsdkjhfzmxcnbvaslkdjfhgqpwoeirytalskdjfgoewfouinemcincvhzikdfvhnaowiudhfcouiohretnaksdjfhgw'
		)
		retVal = User._str_(self)
		assertGreater(50, retVal.len())
		
	def testGoodUser(self):
		retVal = User._str_(self.aUser)
		assertGreater(50, retVal.len())
		
	def testProfile(self):
		retVal = Profile.__str__(self.aProfile)
		assertEqual(retVal, 'Lukas Pecson')