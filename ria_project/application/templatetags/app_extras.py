from django import template
from application.models import EmployeeInfo, Notification

register = template.Library()


@register.simple_tag
def ground(user):
    if not user.is_superuser:
        emp = EmployeeInfo.objects.get(user=user.id)
        return emp.ground.ground_code
    return 0
