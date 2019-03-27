# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553646993.002376
_enable_loop = True
_template_filename = 'C:/Users/PC/sprint1/catalog/templates/product.html'
_template_uri = 'product.html'
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
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product = context.get('product', UNDEFINED)
        def site_center():
            return render_site_center(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h1 class="text-center">Products</h1>\r\n\r\n        <div id="catalog" class="row col-md-12">\r\n        \r\n            <div class="product-tile col-md-4 offset-md-2">\r\n                <div class="product-image"><img class="tile-image" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.image_url() ))
        __M_writer('"></img></div>\r\n                <div class="product-name">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.name ))
        __M_writer('</div>\r\n                <div class="product-price">$')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.price ))
        __M_writer('</div>\r\n                <div class="product-name">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.description ))
        __M_writer('</div>\r\n                <div class="product-quantity">Remaining quantity: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.quantity ))
        __M_writer('</div>\r\n            </div>\r\n            <div class="col-md-4">\r\n            </br></br></br></br></br></br></br></br>\r\n                <form method="post">\r\n                    <table>\r\n                        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\r\n                    </table>\r\n                    <input type="submit" value="Buy Now">\r\n                </form>\r\n                \r\n            </div>\r\n            <div class="col-md-8 offset-md-2">\r\n')
        for url in product.image_urls():
            __M_writer('                    <img class="small-image" src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( url ))
            __M_writer('"></img>\r\n')
        __M_writer('            </div>\r\n\r\n        </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/PC/sprint1/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 33, "51": 3, "61": 3, "62": 9, "63": 9, "64": 9, "65": 10, "66": 10, "67": 11, "68": 11, "69": 12, "70": 12, "71": 13, "72": 13, "73": 19, "74": 19, "75": 26, "76": 27, "77": 27, "78": 27, "79": 27, "80": 29, "86": 80}}
__M_END_METADATA
"""
