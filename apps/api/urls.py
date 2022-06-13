from api.views import *
from rest_framework import routers

router = routers.SimpleRouter()

# API Projects
router.register(r'projectlist', ProjectViewSet, basename='projects')

# API Blogs
router.register(r'bloglist', BlogViewSet, basename='blogs')


urlpatterns = router.urls

