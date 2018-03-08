# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520483994.510319
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/review.html'
_template_uri = 'review.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['css_link', 'global_content', 'top_content', 'middle_content']


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
        def middle_content():
            return render_middle_content(context._locals(__M_locals))
        def global_content():
            return render_global_content(context._locals(__M_locals))
        def top_content():
            return render_top_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def css_link():
            return render_css_link(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'css_link'):
            context['self'].css_link(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'global_content'):
            context['self'].global_content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middle_content'):
            context['self'].middle_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css_link(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def css_link():
            return render_css_link(context)
        __M_writer = context.writer()
        __M_writer('\n<link rel="stylesheet" href="/static/home/styles/review2.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_global_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def global_content():
            return render_global_content(context)
        __M_writer = context.writer()
        __M_writer('\n   <div id = "vertical_red_line"></div>\n   <div id = "horizontal_red_line"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content():
            return render_top_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n   <br /><br /><br /><br /><br /><br />\n   <div class="header_wrapper">\n\n      <h1 class="text-center">How would you rate your experience in secondary education?</h1>\n      <div class="row"id="star_div">\n         <div class="star_wrap 1"><i class="far fa-star fa-2x stars"></i></div>\n         <div class="star_wrap 2"><i class="far fa-star fa-2x stars"></i></div>\n         <div class="star_wrap 3"><i class="far fa-star fa-2x stars"></i></div>\n         <div class="star_wrap 4"><i class="far fa-star fa-2x stars"></i></div>\n         <div class="star_wrap 5"><i class="far fa-star fa-2x stars"></i></div>\n      </div>\n\n         <br />\n\n      ')
        __M_writer(str( form ))
        __M_writer('\n      <p id="textCharCount">280 of 280 characters remaining   </p>\n      <button type="submit" class="btn btn-outline-primary">')
        __M_writer(filters.html_escape(str( form.submit_text )))
        __M_writer('</button>\n   </form>\n   </div>\n   </div>\n\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_middle_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def middle_content():
            return render_middle_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/review.html", "uri": "review.html", "source_encoding": "utf-8", "line_map": {"28": 0, "42": 1, "47": 5, "52": 11, "57": 40, "62": 44, "68": 3, "74": 3, "80": 7, "86": 7, "92": 12, "99": 12, "100": 27, "101": 27, "102": 29, "103": 29, "109": 41, "115": 41, "121": 115}}
__M_END_METADATA
"""
