from django.urls import path
from .views import get, create, delete


urlpatterns = [
    path('get/',get.GetAll),
    path('get/<str:live_id>/',get.GetLive),
    path('delete/<str:live_id>/',delete.DeleteLive),
    path('create/',create.CreateLive),

]