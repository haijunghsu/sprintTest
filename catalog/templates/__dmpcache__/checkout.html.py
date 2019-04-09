# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553836360.4711401
_enable_loop = True
_template_filename = 'C:/Users/PC/sprint1/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


from decimal import Decimal 

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        def site_center():
            return render_site_center(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    Checkout\r\n    <form method="POST">\r\n        <table>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
        __M_writer('</table>\r\n        <form action="your-server-side-code" method="POST">\r\n            <script\r\n              src="https://checkout.stripe.com/checkout.js" class="stripe-button"\r\n              data-key=\'pk_test_kBGIrn6ltFl45eOmqMQGrBzW00OtTqJb2y\'\r\n              data-amount= \'')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cart.total * Decimal("100.0")))
        __M_writer('\'\r\n              data-name="Demo Site"\r\n              data-description="Widget"\r\n              data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\r\n              data-locale="auto">\r\n            </script>\r\n          </form>\r\n    </form>\r\n\r\n \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/PC/sprint1/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "41": 1, "42": 2, "47": 21, "53": 3, "62": 3, "63": 6, "64": 6, "65": 11, "66": 11, "72": 66}}
__M_END_METADATA
"""
