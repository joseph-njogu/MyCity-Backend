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
from . import views

router = DefaultRouter()
router.register('listusers', UserViewSet),
router.register('listparkings', ParkingViewSet)
router.register('parkings', PlaceViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path('parkinginfo',ParkingInfoCreate.as_view(), name='parkinginfo'),
    path('createbookings', BookingCreate.as_view(), name='createbookings'),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('callback/', views.MpesaCallBack, name='callback'),

]

urlpatterns += router.urls