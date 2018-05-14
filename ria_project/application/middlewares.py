from django.utils.timezone import now
from .models import User


class SetLastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            User.objects.filter(pk=request.user.pk).update(last_seen=now())
        return self.get_response(request)
