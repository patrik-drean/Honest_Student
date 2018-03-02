# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519965137.294091
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/optional_information.html'
_template_uri = 'optional_information.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['global_content', 'middle_content']


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
        def global_content():
            return render_global_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def middle_content():
            return render_middle_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'global_content'):
            context['self'].global_content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middle_content'):
            context['self'].middle_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_global_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def global_content():
            return render_global_content(context)
        __M_writer = context.writer()
        __M_writer('\n   <div id = "vertical_red_line"></div>\n   <div id = "horizontal_red_line"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_middle_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def middle_content():
            return render_middle_content(context)
        __M_writer = context.writer()
        __M_writer("\n<br /><br /><br /><br /><br />\n   <div id = 'optional_div'>\n      <h1>Optional Information</h1>\n      <hr />\n\n      ")
        __M_writer(str( form ))
        __M_writer('\n<br />\n      <div class="row">\n         <div class="col-md-1"></div>\n         <div class="checkbox">\n            <p><input name="mailing_list" class="" id="id_mailing_list" type="checkbox" > Mark here if you\'d like updates on our progress in this discussion</p>\n         </div>\n      </div>\n      <br />\n')
        __M_writer('         <p class="">\n            <button type="submit" class="btn btn-outline-primary float-right">')
        __M_writer(filters.html_escape(str( form.submit_text )))
        __M_writer('</button>\n            <button type="submit" class=" btn btn-outline-primary float-right">Skip</button>\n\n            <br /><br />\n         </p>\n         </form>\n     </div>\n\n   </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/optional_information.html", "uri": "optional_information.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 5, "48": 33, "54": 2, "60": 2, "66": 6, "73": 6, "74": 12, "75": 12, "76": 22, "77": 23, "78": 23, "84": 78}}
__M_END_METADATA
"""
