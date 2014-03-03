from django.db import models
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse

from datetime import datetime

class IdeaManager(models.Manager):

    def with_total_votes(self):
        return self.get_query_set().annotate(
            total_votes=models.Sum('vote__value')
        )

class Idea(models.Model):
    title = models.CharField(max_length=2048)
    description = models.TextField()

    owner = models.ForeignKey('auth.User')

    created = models.DateTimeField(default=datetime.now)

    objects = IdeaManager()

    def __unicode__(self):
        return self.title		
	
    def get_absolute_url(self):
        return reverse('idea-detail', args=[str(self.id)])

    def get_voteup_url(self):
        return reverse('idea-vote-up', args=[str(self.id)])

    def get_votedown_url(self):
        return reverse('idea-vote-down', args=[str(self.id)])

    def get_comment_url(self):
        return ('idea-comment', (), {'idea_id': self.pk})

    def get_thank_you_url(self):	
        return reverse('idea-thank-you', args=[str(self.id)])
	
    @cached_property
    def total_votes(self):
        return self.vote_set.aggregate(total = models.Sum('value'))['total']

class Vote(models.Model):
    idea = models.ForeignKey('Idea')
    user = models.ForeignKey('auth.User')

    value = models.IntegerField(choices=(
        (-1, 'Down'),
        (1, 'Up'),
    ))

    class Meta:
        unique_together = (
            ('user', 'idea'),
        )

class Comment(models.Model):
    idea = models.ForeignKey('Idea')
    user = models.ForeignKey('auth.User')

    created = models.DateTimeField(default=datetime.now)

    comment = models.TextField()

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.comment