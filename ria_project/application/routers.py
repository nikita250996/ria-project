from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'duty-payments', views.DutyPaymentViewSet, 'duty-payment')
router.register(r'intellectual-properties', views.IntellectualPropertyViewSet, 'intellectual-property')
router.register(r'intangible-assets', views.IntangibleAssetViewSet, 'intangible-asset')
router.register(r'intellectual-property-commercialization',
                views.IntellectualPropertyCommercializationViewSet, 'intellectual-property-commercialization')
router.register(r'notification',
                views.NotificationViewSet, 'notification')
router.register(r'messages', views.MessageViewSet, 'messages')
