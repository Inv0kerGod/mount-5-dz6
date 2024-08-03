from rest_framework.routers import DefaultRouter

from .views import TaskAPI


router = DefaultRouter()
router.register('task', TaskAPI, basename="task_api")

urlpatterns = [
    
]


urlpatterns += router.urls
