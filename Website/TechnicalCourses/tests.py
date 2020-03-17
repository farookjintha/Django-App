from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Allcourses

class AllcoursesModelTests(TestCase):
    def test_was_published_recently_with_future_course(self):
        time = timezone.now()+datetime.timedelta(days = 30)
        future_question = Allcourses(startedfrom = time)
        self.assertIs(future_question.was_published_recently(), False)
