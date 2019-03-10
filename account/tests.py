from django.test import TestCase
from account import models as amod
from datetime import datetime
from lxml import etree
from django.contrib.auth import models as pmod

class AccountTests(TestCase):
    fixtures = ['account.yaml']

    # @classmethod
    # def setUpTestData(cls):
    #     # Set up data for the whole TestCase
    #     cls.foo = Foo.objects.create(bar="Test")
    #     ...
    def setUp(self):
        self.homer = amod.User()
        self.homer.username = "homer2"
        self.homer.set_password('doh!')
        self.homer.first_name = "Homer2"
        self.homer.last_name = "Simpson2"
        self.homer.birthdate = datetime(2000, 1, 1)
        self.homer.save()

    def test_user_get(self):
        # print('in test_user_get')
        u1 = amod.User.objects.get(id = 1)
        # print(u1) # this is not appropriate in a finished unit test
        self.assertEqual(u1.username, 'homer17', msg="user name should've been homer17")
        self.assertTrue(u1.check_password('password'), msg="Wrong password")

    def test_create_user(self):
        amod.User.objects.create_user(username='tester1', password='password', first_name='Test', last_name='Tester', email='test@emails.com').save()
        test_user = amod.User.objects.get(username='tester1')
        self.assertEqual(test_user.username, 'tester1')
        self.assertEqual(test_user.first_name, 'Test')
        self.assertEqual(test_user.last_name, 'Tester')
        self.assertEqual(test_user.email, 'test@emails.com')

    def test_update_password(self):
        amod.User.objects.create_user(username='tester1', password='password', first_name='Test', last_name='Tester', email='test@emails.com').save()
        test_user = amod.User.objects.get(username='tester1')
        self.assertEquals(test_user.check_password('password'), True)

        test_user.set_password('updated_password')
        test_user.save()
        self.assertEquals(test_user.check_password('updated_password'), True) 

    def test_user_login(self):
        credentials = {
            'username': 'homer2',
            'password': 'doh!'
        }
        response = self.client.post('/account/login/', credentials)
        request = response.wsgi_request
        self.assertTrue(request.user.is_authenticated, msg="User should have authenticated")
        self.assertEqual(request.user.id, self.homer.id, msg="User should have been homer")
        self.assertEqual(response.status_code, 302, msg="User wasn't redirected")

    def test_user_groups(self):
        #Add new group to db with user some persmissions
        test_group = pmod.Group()
        test_group.name = "Supervisor"
        test_group.save()
        test_group.permissions.add(pmod.Permission.objects.get(codename='add_user'))
        test_group.permissions.add(pmod.Permission.objects.get(codename='delete_user'))
        test_group.permissions.add(pmod.Permission.objects.get(codename='change_user'))
        test_group.save()

        #Add user to group
        self.homer.groups.add(test_group)

        #Check to see if user now has permissions from test_group
        self.assertTrue(self.homer.has_perm('account.add_user'), msg="No permission for add_user")
        self.assertTrue(self.homer.has_perm('account.delete_user'), msg="No permission for delete_user")
        self.assertTrue(self.homer.has_perm('account.change_user'), msg="No permission for change_user")

    def test_user_permissions(self):
        #Create a new permission
        test_permission = pmod.Permission(name='testing persmission', codename='test', content_type=pmod.Permission.objects.get(codename='add_user').content_type)
        test_permission.save()

        #Give user new permission
        self.homer.user_permissions.add(test_permission)

        #Check to see if user has permission
        self.assertTrue(self.homer.has_perm('account.test'), msg="Persmission test was not added to user")