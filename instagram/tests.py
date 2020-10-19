from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Profile,Image,Comment
import datetime as dt


# Create your tests here.
class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile =Profile(profile_photo="'image.jpeg'",bio="God Above All")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    #Testing Save Method
    def test_save_method(self):
        self.new_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()



class ImageTestClass(TestCase):


    def setUp(self):
        self.new_image=Image(image="image.jpeg",name="Flower",caption="Naturelover",pub_date="two minutes ago",likes=4)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))


    def test_save_method(self):
        '''
        Function that tests whether an image is saved to database
        '''
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether an image can be deleted from the database
        '''
        self.new_image.save_image()
        self.new_image.delete_image()
