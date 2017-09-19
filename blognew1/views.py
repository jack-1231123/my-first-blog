# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the blognew1 index.")
	return render(request, 'blognew1/index.html', {})
# Create your views here.
