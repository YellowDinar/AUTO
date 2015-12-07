# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from models import *
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    result = []
    result.append(Post.objects.get(id=3))
    result.append(Post.objects.get(id=5))
    context = {
        'posts': result,
        'topics': getTopics()
    }
    return render(request, 'website/index.html', context)

def getPosts(request, id):
    if Topic.objects.get(id=id):
        topic = Topic.objects.get(id=id)
        posts = Post.objects.filter(topic=id)
    context = {
        'topics': getTopics(),
        'topic': topic,
        'posts': posts
    }
    return render(request, 'website/topic.html', context)

def getPost(request, id, post_id):
    if Post.objects.get(id=post_id):
        post = Post.objects.get(id=post_id)
    context = {
        'topics': getTopics(),
        'post': post
    }
    return render(request, 'website/post.html', context)


def getTopics():
    posts = Post.objects.all()
    random_list = []
    random_list.append(random.choice(posts))
    random_list.append(random.choice(posts))
    random_list.append(random.choice(posts))
    random_list.append(random.choice(posts))
    random_list.append(random.choice(posts))

    topics = Topic.objects.all()

    result = {
        'random_list': random_list,
        'topics': topics
    }

    return result

def randomPosts(request):
    posts = Post.objects.all()
    result = []
    result.append(random.choice(posts))
    result.append(random.choice(posts))
    result.append(random.choice(posts))
    context = {
        'topics': getTopics(),
        'posts': result
    }
    return render(request, 'website/random.html', context)