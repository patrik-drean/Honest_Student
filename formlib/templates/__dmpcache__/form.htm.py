# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519934786.7710679
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/formlib/templates/form.htm'
_template_uri = 'form.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        csrf_input = context.get('csrf_input', UNDEFINED)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n<div class="form-container">\n    <form id="')
        __M_writer(str( form.form_id ))
        __M_writer('" action="')
        __M_writer(str( form.form_action or '' ))
        __M_writer('" method="')
        __M_writer(str( form.form_method ))
        __M_writer('">\n\n')
        __M_writer('        ')
        __M_writer(str( csrf_input ))
        __M_writer('\n\n')
        __M_writer('        ')
        __M_writer(str( form.as_p() ))
        __M_writer('\n\n        <!-- ## submit button\n        <p class="text-center"><button type="submit" class="btn btn-primary">')
        __M_writer(filters.html_escape(str( form.submit_text )))
        __M_writer('</button></p> -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/formlib/templates/form.htm", "uri": "form.htm", "source_encoding": "utf-8", "line_map": {"17": 0, "25": 3, "26": 3, "27": 6, "28": 6, "29": 6, "30": 6, "31": 6, "32": 6, "33": 9, "34": 9, "35": 9, "36": 12, "37": 12, "38": 12, "39": 15, "40": 15, "46": 40}}
__M_END_METADATA
"""
