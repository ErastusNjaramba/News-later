import unittest
from app.models import News,Article


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News
        self.new_article = Article

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
        self.assertTrue(isinstance(self.new_article,Article))

