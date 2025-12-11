from django import template

register = template.Library()

@register.filter
def get_item(dict, key):
    item = dict[key]
    if type(item) == list:
        return item[0].replace(',','')
    return item