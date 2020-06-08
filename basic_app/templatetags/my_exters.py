from django import template

register = template.lirary()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts outs all values of "arg" form the string!

    """
    return value.replace(arg,'')

#register.filter('cut',cut)
