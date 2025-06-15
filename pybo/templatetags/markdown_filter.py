from django import template
import markdown

register = template.Library()

@register.filter
def markdownx(text):
    return markdown.markdown(text)