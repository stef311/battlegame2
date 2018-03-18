from django import template

from account.appconfig import CLASS_CHOICES


def get_tribe_name(value):
    for num, name in CLASS_CHOICES:
        if num == str(value):
            return name
    return "something went wrong. cannot get class name"

    #add some try/catch approach above where appropriate


register = template.Library()
register.filter("get_tribe_name", get_tribe_name)