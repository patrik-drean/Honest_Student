from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django_mako_plus import view_function, jscontext
from formlib import Formless
import re

@view_function
def process_request(request):
    form = ReviewForm(request)
    context = {
        "form": form,
    }
    if form.is_valid():
        form.commit()

        # Add sessions for responses to save later
        response = HttpResponse(request.dmp.render('optional_information.html'))

        request.session['message'] = form.cleaned_data.get('message')
        request.session['rating'] = form.cleaned_data.get('rating')

        return HttpResponseRedirect('/home/optional_information')


    return HttpResponse(request.dmp.render('review.html', context))




class ReviewForm(Formless):

    def init(self):
        '''Adds the fields for this form (called at end of __init__)'''
        self.fields['rating'] = forms.IntegerField(initial = 5,
                                                    widget = forms.HiddenInput())

        self.fields['message'] = forms.CharField(label = '', widget = forms.Textarea(attrs={'placeholder': 'Tell the world why...'}))

        self.submit_text = 'Next'

    def commit(self):
        pass
