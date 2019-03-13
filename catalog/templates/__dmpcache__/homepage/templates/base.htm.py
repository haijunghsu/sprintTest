# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552358965.6165557
_enable_loop = True
_template_filename = 'C:/Users/PC/sprint1/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'header_maintenance', 'menu', 'site_left', 'site_center', 'site_right']


import datetime 

import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def menu():
            return render_menu(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def header_maintenance():
            return render_header_maintenance(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def site_left():
            return render_site_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>Sprint 1 &ndash; ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap.bundle.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/popper.min.js"></script>\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap.css">\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        <!--this command put everything back together: base.css, base.js which are in a different folder, just to keep the code clean -->\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png">\r\n\r\n    </head>\r\n    <body>\r\n        <div id="maintenance_message" class="alert alert-danger hidden">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_maintenance'):
            context['self'].header_maintenance(**pageargs)
        

        __M_writer('\r\n        </div>\r\n        <header id="header">         \r\n                <nav class="navbar navbar-expand-lg navbar-dark">\r\n                    <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" alt="python" width="40" height="40"/>\r\n                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\r\n                        <span class="navbar-toggler-icon"></span>\r\n                    </button>\r\n                    <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">\r\n                        <ul class="navbar-nav mr-4">\r\n                            <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('"><a class="nav-link" href="/">Home</a></li>\r\n                            <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('"><a class="nav-link" href="/contact">Contact</a></li>\r\n                            <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('"><a class="nav-link" href="#">About</a></li>\r\n                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n')
        if request.user.is_authenticated:
            __M_writer('                                <li class="nav-item dropdown">\r\n                                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                                    Welcome. User\r\n                                    </a>\r\n                                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">\r\n                                    <a class="dropdown-item" href="#">Account</a>\r\n                                    <a class="dropdown-item" href="#">Porfile</a>\r\n                                    <div class="dropdown-divider"></div>\r\n                                    <a class="dropdown-item" href="/account/logout">LogOut</a>\r\n                                    </div>\r\n                                </li>\r\n')
        else:
            __M_writer('                                <li class="nav-item"><a class="nav-link" href="/account/login/">Login</a></li>\r\n')
        __M_writer('                        </ul>\r\n                    </div>\r\n                </nav>\r\n        </header>\r\n\r\n        <main>\r\n            <div id="site_left">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_right">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n\r\n        <footer>\r\n            <br>\r\n            <div class="center_text">&copy;Copyright ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( datetime.datetime.today().year))
        __M_writer('. All rights reserved</div>\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_maintenance(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_maintenance():
            return render_header_maintenance(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n                            <li class="nav-item"><a class="nav-link" href="#">OverrideMe</a></li>\r\n                            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    <p>something i dont need</p>\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/PC/sprint1/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 84, "22": 0, "42": 2, "47": 8, "48": 11, "49": 11, "50": 11, "51": 12, "52": 12, "53": 13, "54": 13, "55": 14, "56": 14, "57": 17, "58": 19, "59": 19, "60": 20, "61": 20, "66": 25, "67": 29, "68": 29, "69": 35, "70": 35, "71": 36, "72": 36, "73": 37, "74": 37, "79": 40, "80": 41, "81": 42, "82": 53, "83": 54, "84": 56, "89": 65, "94": 69, "99": 73, "100": 79, "101": 79, "102": 84, "108": 8, "119": 25, "130": 38, "136": 38, "142": 63, "148": 63, "154": 68, "160": 68, "166": 72, "172": 72, "178": 172}}
__M_END_METADATA
"""
