from django import template
from markdown import markdown
import re
from main.utilities import get_section

register = template.Library()

def raw_content(value):
    value=markdown(value)
    return re.sub('<[^<]+?>', '', value)
"""
def get_section(value):
    return value.__class__.__name__
register.filter('get_section',get_section)
"""
register.filter('raw_content', raw_content)
