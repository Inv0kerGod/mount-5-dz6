from django.urls import path

from .views import *

urlpatterns = [
    path('', SettingsAPIView.as_view(), name="api_settings"),
    path('create/', SettingsAPICreate.as_view(), name="api_settings_create"),
    path('<int:pk>/', SettingsAPIRetrieve.as_view(), name="api_settings_detail"),
    path('update/<int:pk>/', SettingsAPIUpdate.as_view(), name="api_settings_update"),
    path('destroy/<int:pk>/', SettingsAPIDestroy.as_view(), name="api_settings_destroy"),
]
