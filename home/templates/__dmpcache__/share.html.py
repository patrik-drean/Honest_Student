# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519997691.513362
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/share.html'
_template_uri = 'share.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['middle_content']


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
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middle_content'):
            context['self'].middle_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_middle_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def middle_content():
            return render_middle_content(context)
        __M_writer = context.writer()
        __M_writer('\n   <a href="https://twitter.com/intent/tweet?text=Hello%20world" class="twitter-hashtag-button" data-size="large" data-show-count="false"></a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>\n\n   <div class="fb-share-button" data-href="http://memoryduck.com" data-layout="button" data-size="large" data-mobile-iframe="true"><a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fmemoryduck.com%2F&amp;src=sdkpreparse" class="fb-xfbml-parse-ignore">Share</a></div>\n   \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/share.html", "uri": "share.html", "source_encoding": "utf-8", "line_map": {"28": 0, "35": 1, "40": 8, "46": 3, "52": 3, "58": 52}}
__M_END_METADATA
"""
