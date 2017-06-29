#!/usr/bin/env python
# coding=utf-8
from django import template
from ..models import *

from django.db.models.aggregates import Count
register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('create_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)




