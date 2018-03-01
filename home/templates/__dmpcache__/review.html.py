# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519876529.15024
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/review.html'
_template_uri = 'review.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['top_content']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content():
            return render_top_content(context)
        __M_writer = context.writer()
        __M_writer('\n   <br /><br /><br /><br /><br /><br />\n   <h1 class="text-center">How would you rate your experience in secondary education?</h1>\n   <br />\n   <div class="row"id="star_div">\n      <div class="star_wrap"><i class="far fa-star fa-2x"></i></div>\n      <div class="star_wrap"><i class="far fa-star fa-2x"></i></div>\n      <div class="star_wrap"><i class="far fa-star fa-2x"></i></div>\n      <div class="star_wrap"><i class="far fa-star fa-2x"></i></div>\n      <div class="star_wrap"><i class="far fa-star fa-2x"></i></div>\n   </div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/review.html", "uri": "review.html", "source_encoding": "utf-8", "line_map": {"28": 0, "35": 1, "40": 16, "46": 3, "52": 3, "58": 52}}
__M_END_METADATA
"""
