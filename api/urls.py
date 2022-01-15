from django.urls import include, path
from django.conf.urls import url, include
from rest_framework import routers
from .apiviews import RoomList, RoomDetails

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet) 

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path("", RoomList.as_view(), name="room-list"),
    path("room-details/<int:pk>/", RoomDetails.as_view(),name="room-details")
]
