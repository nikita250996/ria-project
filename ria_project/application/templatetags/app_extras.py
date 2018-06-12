# coding: utf-8
from django import template
from application.models import EmployeeInfo, Notification, Message

register = template.Library()


@register.simple_tag
def ground(user):
    if not user.is_superuser:
        emp = EmployeeInfo.objects.get(user=user.id)
        return emp.ground.ground_code
    return 0


@register.simple_tag
def update_variable(value):
    """Allows to update existing variable in template"""
    return value


@register.simple_tag
def check(url):
    message = Message.objects.get(id=url.split('/')[-2])
    #if not message.read:
    #    answer = Message.objects.create(receiver=message.sender, sender=message.receiver, text='Это мой ответ')
    #    answer.save()
    message.read = True

#    print('Получатель: {0} | Sender: {1}'.format(message.receiver, message.sender))

#    temporary = message.receiver
#    message.receiver = message.sender
#    message.sender = temporary
#    print('Получатель: {0} | Sender: {1}'.format(message.receiver, message.sender))
    message.save()
#    message = Message.objects.get(id=url.split('/')[-2])
#    print('Получатель: {0} | Sender: {1}'.format(message.receiver, message.sender))


    return "Сообщение прочитано"
