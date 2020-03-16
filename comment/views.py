from django.shortcuts import render, redirect
from .models import Comment
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from confession.models import Confession

# Create your views here.
