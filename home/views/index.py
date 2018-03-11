from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from home import models as hmod
from django.db.models import Avg

@view_function
def process_request(request):
    users = hmod.User.objects.all().order_by('-create_date')
    average_rating = hmod.Review.objects.all().aggregate(Avg('rating'))
    review_count = len(users)


    context = {
        'users': users,
        'review_count': review_count,
        'average_rating': round(average_rating['rating__avg'],1),
    }
    return request.dmp.render('index.html', context)
