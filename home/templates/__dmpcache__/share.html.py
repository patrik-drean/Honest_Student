# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520025358.9881558
_enable_loop = True
_template_filename = '/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/share.html'
_template_uri = 'share.html'
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
        def middle_content():
            return render_middle_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'global_content'):
            context['self'].global_content(**pageargs)
        

        __M_writer('\n\n\n')
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
        __M_writer('\n   <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">\n\n   <div id = "vertical_red_line"></div>\n   <div id = "horizontal_red_line"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_middle_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def middle_content():
            return render_middle_content(context)
        __M_writer = context.writer()
        __M_writer('\n   <br /><br /><br /><br /><br />\n\n   <h1 class="text-center">The world almost knows...</h1>\n   <br /><br />\n   <h2 class="text-center">Share with your friends!</h2>\n   <!--<a href="https://twitter.com/intent/tweet?text=Hello%20world" class="twitter-hashtag-button" data-size="large" data-show-count="false"></a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>\n\n   <div class="fb-share-button" data-href="http://memoryduck.com" data-layout="button" data-size="large" data-mobile-iframe="true"><a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fmemoryduck.com%2F&amp;src=sdkpreparse" class="fb-xfbml-parse-ignore">Share</a></div>\n\n   <script src="//platform.linkedin.com/in.js" type="text/javascript"> lang: en_US</script>\n   <script type="IN/Share" data-url="memoryduck.com"></script>-->\n\n\n   <br /><br /><br /><br /><br />\n   <a href="/home/"<button class=" btn btn-outline-primary float-right">Skip to what other people said</button></a>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/patrikdrean/Documents/python_projects/honest_student/honest_student/home/templates/share.html", "uri": "share.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 7, "47": 28, "53": 2, "59": 2, "65": 10, "71": 10, "77": 71}}
__M_END_METADATA
"""
