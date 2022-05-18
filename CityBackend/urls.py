# from django.urls import path
# from .views import polls_list, polls_detail

# urlpatterns = [
# 	path("polls/", polls_list, name="polls_list"),
# 	path("polls/<int:pk>/", polls_detail, name="polls_detail"),
# ]
from rest_framework.routers import DefaultRouter
#from .apiviews import PollViewSet

from django.urls import path
from .apiviews import *

router = DefaultRouter()
router.register('listusers', UserViewSet),
router.register('listparkings', ParkingViewSet)
router.register('parkings', PlaceViewSet)
router.register('bookings', BookingsViewSet)

urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path('parkinginfo',ParkingInfoCreate.as_view(), name='parkinginfo')
    path('createbookings', BookingsCreate.as_view(), name='createbookings')

]

urlpatterns += router.urls