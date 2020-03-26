from database import get_users_2, get_posts, create_user
import unittest

class TestDatabaseMethods(unittest.TestCase):

    def test_get_posts(self):
        posts = get_posts()
        self.assertEqual(posts[0]['title'], 'I am Bob')

    def test_create_user(self):
        create_user('Batman', 'Bruce Wayne', 'batman@gotham.com', 'IamtheNight')
        users = get_users_2()
        self.assertEqual(users['Batman'], 'Batman')
