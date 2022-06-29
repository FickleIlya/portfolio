from api.views import *
from rest_framework import routers

router = routers.SimpleRouter()

# API Projects
router.register(r'projects', ProjectViewSet, basename='projects')


urlpatterns = router.urls

