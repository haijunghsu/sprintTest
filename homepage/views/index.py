from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from account import models as amod

@view_function
def process_request(request):

    # for i in range(10):
    #     u = amod.User()
    #     u.username = f'user{i}'
    #     u.first_name = 'first' + str(i)
    #     u.last_name = 'last' + str(i)
    #     u.email = f'me@some{i}.com'
    #     u.set_password('asdf')
    #     u.birthdate = datetime(2011,1,1)
    #     u.favcolor = 'red'
    #     u.save()

    utc_time = datetime.utcnow()
    context = {
        # sent to index.html:
        'utc_time': utc_time,
        # sent to index.html and index.js:
        jscontext('utc_epoch'): utc_time.timestamp(),
    }
    return request.dmp.render('index.html', context)