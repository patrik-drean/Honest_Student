# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519868089.184955
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['navbar']


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
        def navbar():
            return render_navbar(context._locals(__M_locals))
        datetime = context.get('datetime', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar'):
            context['self'].navbar(**pageargs)
        

        __M_writer('\n\n\n<p> © ')
        __M_writer(str( datetime.datetime.now().year ))
        __M_writer(' </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar():
            return render_navbar(context)
        __M_writer = context.writer()
        __M_writer('\n\n      <nav class="navbar navbar-toggleable-md navbar-inverse bg-inverse">\n     <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">\n      <span class="navbar-toggler-icon"></span>\n     </button>\n     <a class="navbar-brand" href="#">Pat\'s Brand</a>\n\n     <div class="collapse navbar-collapse" id="navbarsExampleDefault">\n      <ul class="navbar-nav mr-auto">\n         <li class="nav-item">\n          <a class="nav-link" href="#">Home</a>\n         </li>\n         <li class="nav-item">\n          <a class="nav-link" href="#">About</a>\n         </li>\n         <li class="nav-item">\n          <a class="nav-link" href="#">Contact</a>\n         </li>\n      </ul>\n      <!-- <form class="form-inline my-2 my-md-0">\n         <input class="form-control mr-sm-2" placeholder="Search" type="text">\n         <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>\n      </form> -->\n      <!-- <div class="nav-item dropdown ">\n        <a class="nav-link dropdown-toggle" href="http://example.com" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Login</a>\n        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdown01">\n          <a class="dropdown-item" href="#">Login</a>\n          <a class="dropdown-item" href="#">Signup</a>\n        </div>\n     </div> -->\n     </div>\n  </nav>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "41": 37, "42": 40, "43": 40, "49": 3, "55": 3, "61": 55}}
__M_END_METADATA
"""
