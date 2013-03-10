from django.db import models
from json import dumps

# Create your models here.

class Basemap(models.Model):
    dot_rep = models.TextField()
    svg_rep = models.TextField()

    finished = models.BooleanField()
    status = models.TextField()

    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)

    starting_year = models.IntegerField()
    ending_year = models.IntegerField()
    sample_size = models.IntegerField()
    ranking_algorithm = models.IntegerField()
    similarity_algorithm = models.IntegerField()
    filtering_algorithm = models.IntegerField()
    number_of_terms = models.IntegerField()

    author = models.CharField(max_length=255)
    conference = models.CharField(max_length=255)
    journal = models.CharField(max_length=255)

    documents_in_set = models.IntegerField(null=True, blank=True)
    documents_sampled = models.IntegerField(null=True, blank=True)

    def metadata(self):
        return {
            'status': self.status,
            'height': self.height,
            'width': self.width,
            'finished': self.finished,
            'starting_year': self.starting_year,
            'ending_year': self.ending_year,
            'sample_size': self.sample_size,
            'ranking_algorithm': self.ranking_algorithm,
            'similarity_algorithm': self.similarity_algorithm,
            'filtering_algorithm': self.filtering_algorithm,
            'number_of_terms': self.number_of_terms,
            'author': self.author,
            'conference': self.conference,
            'journal': self.journal,
            'documents_in_set': self.documents_in_set,
            'documents_sampled': self.documents_sampled
        }

    def json_metadata(self):
        return dumps(self.metadata())

class Heatmap(models.Model):
    terms = models.TextField()

    finished = models.BooleanField()
    status = models.TextField()

    starting_year = models.IntegerField()
    ending_year = models.IntegerField()
    sample_size = models.IntegerField()

    author = models.CharField(max_length=255)
    conference = models.CharField(max_length=255)
    journal = models.CharField(max_length=255)

    documents_in_set = models.IntegerField(null=True, blank=True)
    documents_sampled = models.IntegerField(null=True, blank=True)

    def metadata(self):
        return {
            'status': self.status,
            'finished': self.finished,
            'starting_year': self.starting_year,
            'ending_year': self.ending_year,
            'sample_size': self.sample_size,
            'author': self.author,
            'conference': self.conference,
            'journal': self.journal,
            'documents_in_set': self.documents_in_set,
            'documents_sampled': self.documents_sampled
        }

    def json_metadata(self):
        return dumps(self.metadata())

class Task(models.Model):
    basemap = models.ForeignKey(Basemap)
    heatmap = models.ForeignKey(Heatmap)
