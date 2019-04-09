# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553832660.1913903
_enable_loop = True
_template_filename = 'C:/Users/PC/sprint1/catalog/templates/cart.html'
_template_uri = 'cart.html'
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
        cart = context.get('cart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        saleitems = context.get('saleitems', UNDEFINED)
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
        cart = context.get('cart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        saleitems = context.get('saleitems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table>\r\n        <tr>\r\n        <th></th>\r\n        <th>Product Name</th>\r\n        <th>Quantity</th>\r\n        <th>Price</th>\r\n        <th>Extended</th>\r\n        <th>Actions</th>\r\n        </tr>\r\n')
        for si in saleitems:
            __M_writer('            <tr>\r\n            <td>\r\n                <img id="product_image" src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.product.image_url() ))
            __M_writer('" alt="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(django.utils.html.escape( si.product.name )))
            __M_writer('" />\r\n                </td>\r\n                <td>\r\n                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.product.name ))
            __M_writer('\r\n                </td>\r\n                <td>\r\n                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.quantity ))
            __M_writer('\r\n                </td>\r\n                <td>\r\n                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.product.price ))
            __M_writer('\r\n                </td>\r\n                <td>\r\n                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( si.product.price * si.quantity ))
            __M_writer('\r\n                </td>\r\n                <td>\r\n                    <a href="/catalog/cart.remove/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(si.id))
            __M_writer('">Remove</a>\r\n                </td>\r\n            </tr>\r\n')
        __M_writer('        <tr>\r\n            <td>Subtotal</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cart.subtotal))
        __M_writer('</td>\r\n        </tr>\r\n        <tr>\r\n            <td>Tax</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cart.tax))
        __M_writer('</td>\r\n        </tr>\r\n        <tr>\r\n        <td>Total</td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cart.total))
        __M_writer('</td>\r\n        </tr>\r\n    </table>\r\n    <button><a href="/catalog/checkout/">Checkout</a></button>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/PC/sprint1/catalog/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "50": 3, "60": 3, "61": 13, "62": 14, "63": 16, "64": 16, "65": 16, "66": 16, "67": 16, "68": 19, "69": 19, "70": 22, "71": 22, "72": 25, "73": 25, "74": 28, "75": 28, "76": 31, "77": 31, "78": 35, "79": 37, "80": 37, "81": 41, "82": 41, "83": 45, "84": 45, "90": 84}}
__M_END_METADATA
"""
