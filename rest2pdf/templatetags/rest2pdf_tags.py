from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='rst_heading')
def rst_heading(value, arg):
    """Provides an underline for restructured text heading.
    
    Syntax::

        {{ value|rst_heading:"=" }}

    Results in:
    
    ``value``
    
    ``=====``
    
    """
    return ''.join([value, '\n', arg*len(value)])

