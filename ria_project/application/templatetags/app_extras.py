from django import template
from application.models import EmployeeInfo, Request

register = template.Library()


@register.simple_tag
def ground(user):
    if not user.is_superuser:
        emp = EmployeeInfo.objects.get(user=user.id)
        return emp.ground.ground_code
    return 0


@register.simple_tag
def get_latest_created_requests_number(user):
    last_login = user.last_seen
    return Request.objects.filter(created_at__gte=last_login).count()
