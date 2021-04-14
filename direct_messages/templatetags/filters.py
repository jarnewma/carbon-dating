from django import template
from direct_messages.models import Message


register = template.Library()


@register.filter
def unread_count(request):
    count = Message.objects.filter(receiver=request.user, viewed=False).count()
    return count
