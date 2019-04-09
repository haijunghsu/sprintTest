# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553838706.6789095
_enable_loop = True
_template_filename = 'C:/Users/PC/sprint1/catalog/templates/receipt.html'
_template_uri = 'receipt.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


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
        sale = context.get('sale', UNDEFINED)
        self = context.get('self', UNDEFINED)
        saleitems = context.get('saleitems', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        sale = context.get('sale', UNDEFINED)
        self = context.get('self', UNDEFINED)
        saleitems = context.get('saleitems', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h1>Receipt</h1>\r\n<table>\r\n    <tr>\r\n    <th></th>\r\n    <th>Product Name</th>\r\n    <th>Quantity</th>\r\n    <th>Price</th>\r\n    <th>Extended</th>\r\n    <th>Actions</th>\r\n    </tr>\r\n')
        for si in saleitems:
            __M_writer('        <tr>\r\n         <td>\r\n                <img id="product_image" src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.product.image_url() ))
            __M_writer('" alt="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(django.utils.html.escape( si.product.name )))
            __M_writer('" />\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.product.name ))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.quantity ))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.product.price * si.quantity ))
            __M_writer('\r\n            </td>\r\n        </tr>\r\n')
        __M_writer('    <tr>\r\n        <td>Subtotal</td>\r\n        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.subtotal))
        __M_writer('</td>\r\n    </tr>\r\n    <tr>\r\n        <td>Tax</td>\r\n        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.tax))
        __M_writer('</td>\r\n    </tr>\r\n    <tr>\r\n    <td>Total</td>\r\n        <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.total))
        __M_writer('</td>\r\n    </tr>\r\n</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/PC/sprint1/catalog/templates/receipt.html", "uri": "receipt.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "50": 3, "60": 3, "61": 15, "62": 16, "63": 18, "64": 18, "65": 18, "66": 18, "67": 18, "68": 21, "69": 21, "70": 24, "71": 24, "72": 27, "73": 27, "74": 31, "75": 33, "76": 33, "77": 37, "78": 37, "79": 41, "80": 41, "86": 80}}
__M_END_METADATA
"""
