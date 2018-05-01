from django import template
from application.models import Employees
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def ground(user):
    if not user.is_superuser:
        emp = Employees.objects.get(user=user.id)
        return emp.ground.ground_code
    return 0
