from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django_mako_plus import view_function, jscontext
from formlib import Formless
import re

@view_function
def process_request(request):
    context = {'dogs': 2}
    response =  HttpResponse(request.dmp.render('review.html', context))
    response.set_cookie('hi', 'dogs')
    print('>>>>>>>>>>' + str(request.COOKIES.get('hi') ))
    return response

def ReviewForm(Formless):
    pass
