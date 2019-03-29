from django.conf import settings
from django_mako_plus import view_function, jscontext
from account import models as amod
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# @view_function
# def process_request(request):
#     # Create a form instance and populate it with data from the request (binding):
#     # form = LoginForm()
#     # If this is a POST request then process the Form data
#     if request.method == 'POST':    
#         # Create a form instance and populate it with data from the request (binding):
#         form = LoginForm(request.POST)
#         # Check if the form is valid:
#         if form.is_valid():
#             #login method (user)
#             login(request, form.user)
#             return HttpResponseRedirect('/homepage/index/')
#     else:
#         form = LoginForm()

#     context = {
#         'form': form,
#     }
#     return request.dmp.render('product.html', context)

# class LoginForm(forms.Form):
#     username = forms.CharField(help_text = "Enter your username")
#     password = forms.CharField(help_text = "Enter your password", widget=forms.PasswordInput)

#     #create a clean method
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')

#         self.user = authenticate(username = username, password = password)

#         if self.user is not None:
#             return self.cleaned_data
#         else:
#             raise forms.ValidationError('your username or password is not correct')