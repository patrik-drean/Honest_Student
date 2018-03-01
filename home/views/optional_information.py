from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.conf import settings



@view_function
def process_request(request):
    print('>>>>>>>>>>' + str(request.session.get('message')))
    context = {}
    return request.dmp.render('optional_information.html', context)
