from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from formlib import Formless
import re
from django.contrib.auth import authenticate, login
from home import models as hmod


@view_function
def process_request(request):
    form = OptionalForm(request)
    context = {'form': form,}
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/home/share')


    return request.dmp.render('optional_information.html', context)

class OptionalForm(Formless):
    def init(self):
        self.fields['rating'] = forms.IntegerField(initial = self.request.session.get('rating'),
                                                    widget = forms.HiddenInput(),
                                                    required = False)

        self.fields['message'] = forms.CharField(initial =             self.request.session.get('message'),
                                                widget = forms.HiddenInput(),
                                                required = False)
        self.fields['name'] = forms.CharField(label = 'Name', required = False)
        self.fields['school'] = forms.CharField(label = 'School Name', required = False)
        self.fields['email'] = forms.CharField(label = 'Email Address', required = False)
        # self.fields['mailing_list'] = forms.BooleanField(label = '',)
    #     self.fields['name'].widget.attrs.update({
    #         'class': 'donkey'
    # })
    def clean_email(self):
        # Grab user from database with email. If a user comes back, throw exception
        email = self.cleaned_data.get('email')
        users = hmod.User.objects.filter(email = email)
        if users:
            raise forms.ValidationError('Email already exists in database')
        return email

    def commit(self):
        review = hmod.Review()
        review.rating = self.cleaned_data.get('rating')
        review.message = self.cleaned_data.get('message')

        review.save()
        review = hmod.Review.objects.latest('create_date')

        user = hmod.User()
        user.first_name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.school = self.cleaned_data.get('school')

        if self.request.POST.get('mailing_list') is not None:
            user.mailing_list = True
        user.review = review


        user.save()
