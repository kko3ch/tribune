from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Tom = Editor(first_name = 'Tom', last_name = 'Koech', email = 'tomko3ch@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.Tom,Editor))

    def test_save_method(self):
        self.Tom.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        #Creating a new editor and saving it
        self.tomtom = Editor(first_name="tomtom",last_name="tomtom",email="tomtom@gmail.com")
        self.tomtom.save_editor()

        #creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article = Article(title = 'Test Article',post = 'This is a random test Post',editor = self.tomtom)

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)
    
    def test_get_news_by_date(self):
        test_date = '2017-03-2017'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

