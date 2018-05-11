from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'requests', views.RequestViewSet)
router.register(r'duty-payments', views.DutyPaymentViewSet)
router.register(r'intellectual-properties', views.IntellectualPropertyViewSet)
router.register(r'contract-intellectual-properties', views.ContractIntellectualPropertyViewSet)
router.register(r'intellectual-property-commercialization', views.IntellectualPropertyCommercializationViewSet)
router.register(r'intangible-assets', views.IntangibleAssetViewSet)
