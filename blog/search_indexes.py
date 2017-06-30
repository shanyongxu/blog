#!/usr/bin/env python
# coding=utf-8
from haystack import indexes
from blog.models import *
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_quertset(self, using=None):
        return self.get_model().objects.all()
