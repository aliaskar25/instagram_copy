from rest_framework import routers

from .views import PostView


router = routers.DefaultRouter()
router.register('', PostView)


urlpatterns = router.urls