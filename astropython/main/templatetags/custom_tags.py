from django import template
from markdown import markdown
import re
from main.utilities import get_section

register = template.Library()

def raw_content(value):
    value=markdown(value)
    return re.sub('<[^<]+?>', '', value)


def get_section(value):
    return value.__class__.__name__

def isEven(value,arg):
    if arg.index(value)%2==0:
        return True
    return False

register.filter('isEven',isEven)
register.filter('get_section',get_section)
register.filter('raw_content', raw_content)
