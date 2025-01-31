from django.urls import path    
from .views import HomePageView, AboutPageView,ReservationListView,ReservationCreateView,ReservationDetailView,ReservationUpdateView,ReservationDeleteView
from .views import CourtListView,CourtCreateView,CourtDetailView,CourtUpdateView,CourtDeleteView
from .views import FeedbackListView,FeedbackCreateView,FeedbackDetailView,FeedbackUpdateView,FeedbackDeleteView
from .views import BookingHistoryListView,BookingHistoryCreateView,BookingHistoryDetailView,BookingHistoryUpdateView,BookingHistoryDeleteView
from .views import PaymentListView,PaymentCreateView,PaymentDetailView,PaymentUpdateView,PaymentDeleteView

urlpatterns = [
    path('' , HomePageView.as_view(), name='home'),
    path('about/' , AboutPageView.as_view(), name='about'),

    path('reservationlist/' , ReservationListView.as_view(), name='reservation_list'),
    path('reservationcreate/' , ReservationCreateView.as_view(), name='reservation_create'),
    path('reservationdetail/<int:pk>' , ReservationDetailView.as_view(), name='reservation_detail'),
    path('reservationdetail/<int:pk>/edit' , ReservationUpdateView.as_view(), name='reservation_update'),
    path('reservationdetail/<int:pk>/delete' , ReservationDeleteView.as_view(), name='reservation_delete'),

    path('paymentlist/' , PaymentListView.as_view(), name='payment_list'),
    path('paymentcreate/' , PaymentCreateView.as_view(), name='payment_create'),
    path('paymentdetail/<int:pk>' , PaymentDetailView.as_view(), name='payment_detail'),
    path('paymentdetail/<int:pk>/edit' , PaymentUpdateView.as_view(), name='payment_update'),
    path('paymentdetail/<int:pk>/delete' , PaymentDeleteView.as_view(), name='payment_delete'),

    path('courtlist/' , CourtListView.as_view(), name='court_list'),
    path('courtcreate/' , CourtCreateView.as_view(), name='court_create'),
    path('courtdetail/<int:pk>' , CourtDetailView.as_view(), name='court_detail'),
    path('courtdetail/<int:pk>/edit' , CourtUpdateView.as_view(), name='court_update'),
    path('courtdetail/<int:pk>/delete' , CourtDeleteView.as_view(), name='court_delete'),

    path('feedbacklist/' , FeedbackListView.as_view(), name='feedback_list'),
    path('feedbackcreate/' , FeedbackCreateView.as_view(), name='feedback_create'),
    path('feedbackdetail/<int:pk>' , FeedbackDetailView.as_view(), name='feedback_detail'),
    path('feedbackdetail/<int:pk>/edit' , FeedbackUpdateView.as_view(), name='feedback_update'),
    path('feedbackdetail/<int:pk>/delete' , FeedbackDeleteView.as_view(), name='feedback_delete'),

    path('bookingHistorylist/' , BookingHistoryListView.as_view(), name='bookingHistory_list'),
    path('bookingHistorycreate/' , BookingHistoryCreateView.as_view(), name='bookingHistory_create'),
    path('bookingHistorydetail/<int:pk>' , BookingHistoryDetailView.as_view(), name='bookingHistory_detail'),
    path('bookingHistorydetail/<int:pk>/edit' , BookingHistoryUpdateView.as_view(), name='bookingHistory_update'),
    path('bookingHistorydetail/<int:pk>/delete' , BookingHistoryDeleteView.as_view(), name='bookingHistory_delete'),

]
