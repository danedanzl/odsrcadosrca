from django import template

register = template.Library()

@register.filter
def dict_lookup(obj, name):
    #print(f"dict lookup: {obj} {name}")
    if obj is None or name not in obj:
        return ""
    return obj[name]
