# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520650255.46013
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['navbar', 'global_content', 'top_content', 'left_content', 'middle_content', 'right_content', 'footer_content', 'js_link']


import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navbar():
            return render_navbar(context._locals(__M_locals))
        def footer_content():
            return render_footer_content(context._locals(__M_locals))
        def top_content():
            return render_top_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def global_content():
            return render_global_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def middle_content():
            return render_middle_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def js_link():
            return render_js_link(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n      ')
        __M_writer('\n        <title>Honest Student</title>\n\n        <!-- jQuery -->\n        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n\n        <!-- Google fonts -->\n        <link href="https://fonts.googleapis.com/css?family=Nanum+Pen+Script" rel="stylesheet">\n\n        <!-- SVG cdn import -->\n        <script defer src="https://use.fontawesome.com/releases/v5.0.7/js/all.js"></script>\n\n       <!-- Bootstrap CSS link -->\n       <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">\n\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n    </head>\n    <body>\n      <!-- Importing the js for facebook share button -->\n            <div id="fb-root"></div>\n      <script>(function(d, s, id) {\n        var js, fjs = d.getElementsByTagName(s)[0];\n        if (d.getElementById(id)) return;\n        js = d.createElement(s); js.id = id;\n        js.src = \'https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.12\';\n        fjs.parentNode.insertBefore(js, fjs);\n      }(document, \'script\', \'facebook-jssdk\'));</script>\n\n\n         ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar'):
            context['self'].navbar(**pageargs)
        

        __M_writer('\n         ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'global_content'):
            context['self'].global_content(**pageargs)
        

        __M_writer('\n\n\n        <main>\n         <div class="row">\n           <div class="col-md-12" id="top-section">\n             ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_content'):
            context['self'].top_content(**pageargs)
        

        __M_writer('\n           </div>\n         </div>\n         <div class="row">\n           <div class="col-md-2" id="left-section">\n             ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\n           </div>\n           <div class="col-md-8" id="middle-section">\n             ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middle_content'):
            context['self'].middle_content(**pageargs)
        

        __M_writer('\n           </div>\n           <div class="col-md-2" id="right-section">\n             ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\n           </div>\n         </div>\n      </main>\n      <footer>\n             ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_content'):
            context['self'].footer_content(**pageargs)
        

        __M_writer('\n      </footer>\n\n      <!-- Bootstrap JS files -->\n      <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>\n      <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>\n      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_link'):
            context['self'].js_link(**pageargs)
        

        __M_writer('\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar():
            return render_navbar(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_global_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def global_content():
            return render_global_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_content():
            return render_top_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
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


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer_content():
            return render_footer_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_link(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def js_link():
            return render_js_link(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 6, "19": 0, "41": 2, "42": 6, "43": 22, "44": 25, "45": 26, "46": 26, "51": 41, "56": 42, "61": 48, "66": 53, "71": 56, "76": 59, "81": 64, "86": 71, "92": 41, "103": 42, "114": 48, "125": 53, "136": 56, "147": 59, "158": 64, "169": 71, "180": 169}}
__M_END_METADATA
"""
