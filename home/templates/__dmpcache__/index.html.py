# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520716390.887341
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['top_content', 'middle_content']


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
        def middle_content():
            return render_middle_content(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        def top_content():
            return render_top_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\n\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middle_content'):
            context['self'].middle_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def top_content():
            return render_top_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div id="video_content">\n</div>\n<div id="review_content">\n')
        for u in users:
            __M_writer('      <div class="review_wrap">\n         <div class="user_div">\n         <p class="name_text">')
            __M_writer(str( u.name if u.name != None else 'Anonymous' ))
            __M_writer('</p>\n         <p class="school_text">')
            __M_writer(str( u.school if u.school != None else '' ))
            __M_writer('</p>\n\n         <div class="row star_div " name = "')
            __M_writer(str( u.review.rating ))
            __M_writer('">\n            <div class="star_wrap 1"><i class="far fa-star fa-2x stars"></i></div>\n            <div class="star_wrap 2"><i class="far fa-star fa-2x stars"></i></div>\n            <div class="star_wrap 3"><i class="far fa-star fa-2x stars"></i></div>\n            <div class="star_wrap 4"><i class="far fa-star fa-2x stars"></i></div>\n            <div class="star_wrap 5"><i class="far fa-star fa-2x stars"></i></div>\n         </div>\n\n         </div>\n         <div class="message_div">\n         <p>')
            __M_writer(str( u.review.message ))
            __M_writer('</p>\n         </div>\n      </div>\n      <hr />\n')
        __M_writer('</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_middle_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def middle_content():
            return render_middle_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 29, "48": 34, "54": 3, "61": 3, "62": 7, "63": 8, "64": 10, "65": 10, "66": 11, "67": 11, "68": 13, "69": 13, "70": 23, "71": 23, "72": 28, "78": 34, "89": 78}}
__M_END_METADATA
"""
