from django import template

register = template.Library()

@register.filter
def get_item(dict, key):
    item = dict[key]
    if type(item) == list:
        return item[0].replace(',','')
    return item

@register.filter
def replace(item, chars):
    return item.replace(chars[0], chars[1])