from django import template
from markdown import markdown
import re

register = template.Library()

def raw_content(value):
    value=markdown(value)
    return re.sub('<[^<]+?>', '', value)

register.filter('raw_content', raw_content)