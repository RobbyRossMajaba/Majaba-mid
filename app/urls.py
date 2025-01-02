from django.urls import path    
from .views import HomePageView, AboutPageView, ContactPageView,ReservationListView,ReservationCreateView,ReservationDetailView,ReservationUpdateView,ReservationDeleteView

urlpatterns = [
    path('' , HomePageView.as_view(), name='home'),
    path('about/' , AboutPageView.as_view(), name='about'),
    path('contact/' , ContactPageView.as_view(), name='contact'),
    path('reservationlist/' , ReservationListView.as_view(), name='reservation_list'),
    path('reservationcreate/' , ReservationCreateView.as_view(), name='reservation_create'),
    path('reservationdetail/<int:pk>' , ReservationDetailView.as_view(), name='reservation_detail'),
    path('reservationdetail/<int:pk>/edit' , ReservationUpdateView.as_view(), name='reservation_update'),
    path('reservationdetail/<int:pk>/delete' , ReservationDeleteView.as_view(), name='reservation_delete'),
]