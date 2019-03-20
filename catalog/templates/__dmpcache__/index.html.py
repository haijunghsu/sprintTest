# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552536953.869305
_enable_loop = True
_template_filename = 'C:/Users/PC/sprint1/catalog/templates/index.html'
_template_uri = 'index.html'
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
        products = context.get('products', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        page = context.get('page', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        category = context.get('category', UNDEFINED)
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
        products = context.get('products', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        page = context.get('page', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h1 class="text-center">Products</h1>\r\n\r\n        <div id="catalog" class="center-div">\r\n')
        for product in products:
            __M_writer('                <span class="product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.id ))
            __M_writer('"></span>\r\n')
        if category is not None:
            if page == 1: 
                __M_writer('                    <a class="button disabled" href="/catalog/index/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category.id))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page))
                __M_writer('">Previous </a>\r\n')
            else:
                __M_writer('                    <a class="button" href="/catalog/index/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category.id))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page - 1))
                __M_writer('">Previous </a>\r\n')
            __M_writer('\r\n')
            if page == numpages:
                __M_writer('                    <a class="button disabled" href="/catalog/index/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category.id))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page))
                __M_writer('">Next </a>\r\n')
            else:
                __M_writer('                    <a class="button" href="/catalog/index/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category.id))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page + 1))
                __M_writer('">Next </a>\r\n')
        else:
            if page == 1: 
                __M_writer('                    <a class="button disabled" href="/catalog/index/0/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page))
                __M_writer('">Previous </a>\r\n')
            else:
                __M_writer('                    <a class="button" href="/catalog/index/0/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page - 1))
                __M_writer('">Previous </a>\r\n')
            __M_writer('\r\n')
            if page == numpages:
                __M_writer('                    <a class="button disabled" href="/catalog/index/0/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page))
                __M_writer('">Next </a>\r\n')
            else:
                __M_writer('                    <a class="button" href="/catalog/index/0/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page + 1))
                __M_writer('">Next </a>\r\n')
        __M_writer('        </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/PC/sprint1/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 43, "52": 3, "63": 3, "64": 12, "65": 13, "66": 13, "67": 13, "68": 15, "69": 16, "70": 17, "71": 17, "72": 17, "73": 17, "74": 17, "75": 18, "76": 19, "77": 19, "78": 19, "79": 19, "80": 19, "81": 21, "82": 22, "83": 23, "84": 23, "85": 23, "86": 23, "87": 23, "88": 24, "89": 25, "90": 25, "91": 25, "92": 25, "93": 25, "94": 27, "95": 28, "96": 29, "97": 29, "98": 29, "99": 30, "100": 31, "101": 31, "102": 31, "103": 33, "104": 34, "105": 35, "106": 35, "107": 35, "108": 36, "109": 37, "110": 37, "111": 37, "112": 41, "118": 112}}
__M_END_METADATA
"""
