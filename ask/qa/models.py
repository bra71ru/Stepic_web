from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Question(models.Model):

    title = models.CharField(max_length=255, db_index=True)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes')

    def get_url(self):
        return reverse('question', kwargs={'id': self.id})

    class Meta:
        db_table = 'questions'


class Answer(models.Model):

    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def get_url(self):
        return self.question.get_url()

    class Meta:
        db_table = 'answers'
