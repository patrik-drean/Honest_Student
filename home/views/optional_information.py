from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.conf import settings
from formlib import Formless
from django import forms



@view_function
def process_request(request):
    form = OptionalForm(request)
    context = {'form': form,}
    if form.is_valid:
        # form.commit()
        pass

    return request.dmp.render('optional_information.html', context)

class OptionalForm(Formless):
    def init(self):
        self.fields['rating'] = forms.IntegerField(initial = self.request.session.get('rating'),
                                                    widget = forms.HiddenInput())

        self.fields['message'] = forms.CharField(initial = self.request.session.get('message'),
                                                widget = forms.HiddenInput())
        self.fields['name'] = forms.CharField(label = 'Name', required = False)
        self.fields['school'] = forms.CharField(label = 'School Name', required = False)
        self.fields['email'] = forms.CharField(label = 'Email Address', required = False)
        # self.fields['mailing_list'] = forms.BooleanField(label = '',)
    #     self.fields['name'].widget.attrs.update({
    #         'class': 'donkey'
    # })
