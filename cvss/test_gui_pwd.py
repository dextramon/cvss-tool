import unittest
import mock
from controller import Controller
from graphical import GetCredentials
from graphical import CreateUser

class TestModel(unittest.TestCase):

    @classmethod
    def setUp(cls):
        pass 
    # runs once at the beginning

    @classmethod
    def tearDown(cls):
        pass
    # runs once at the end
    
    def setUp(self):
        pass
    # this will run before every test

    def tearDown(self):
        pass
    # this will run after every test

    ## Tests #######################

    def test_check_auth_gui_set(self):
        with mock.patch('os.path.isfile', return_value=False):
            with mock.patch('controller.CreateUser'):
                with mock.patch('controller.Tk'):
                    with mock.patch('controller.CreationView'):
                        c1 = Controller()
                        c1.set_user("test")
                        c1.set_password("test")
                        self.assertEqual(c1.check_auth_gui(), "set")

    def test_check_auth_gui_right(self):
        with mock.patch('os.path.isfile', return_value=True):
            with mock.patch('controller.GetCredentials'):
                with mock.patch('controller.Tk'):
                    with mock.patch('controller.CreationView'):
                        c1 = Controller()
                        c1.set_user("test")
                        c1.set_password("test")
                        self.assertEqual(c1.check_auth_gui(), True)
    
    def test_check_auth_gui_wrong_pwd(self):
        with mock.patch('controller.GetCredentials'):
            with mock.patch('controller.Tk'):
                with mock.patch('controller.CreationView'):
                    c1 = Controller()
                    c1.set_user("test")
                    c1.set_password("test1")
                    self.assertEqual(c1.check_auth_gui(), False)
    
    def test_check_auth_gui_wrong_user(self):
        with mock.patch('controller.GetCredentials'):
            with mock.patch('controller.Tk'):
                with mock.patch('controller.CreationView'):
                    c1 = Controller()
                    c1.set_user("test1")
                    c1.set_password("test")
                    self.assertEqual(c1.check_auth_gui(), False)
    
    def test_check_auth_gui_wrong_user_pwd(self):
        with mock.patch('controller.GetCredentials'):
            with mock.patch('controller.Tk'):
                with mock.patch('controller.CreationView'):
                    c1 = Controller()
                    c1.set_user("test1")
                    c1.set_password("test1")
                    self.assertEqual(c1.check_auth_gui(), False)
    
if __name__ == '__main__':
    unittest.main()