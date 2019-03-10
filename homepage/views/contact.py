from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):
    # did the user submit?
    if request.method == "POST":
        # check all the variables
        # we assume the user does it wrong
        print(request.POST)
        # fi user ddi it right:
        # do the work (reset passwrod, created account, finalize the sale)
        # return HttpResponseRedirect('/index')
    context = {

    }
    return request.dmp.render('contact.html', context)