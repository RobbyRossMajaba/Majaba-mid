from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from .models import Reservation, Payment, Court, Feedback, BookingHistory
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'    

class ContactPageView(TemplateView):
    template_name = 'app/navbar.html'   

def get_context_data(self, **kwargs):
        context_service = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if self.request.user.is_superuser:
            context_service['super_user'] = True
        else:
            context_service['super_user'] = False
        return context_service   
        
# =======================================================================================================
class ReservationListView(ListView):
    model = Reservation
    context_object_name = 'reservation'
    template_name = 'app/reservation_list.html'

def get_context_data(self, **kwargs):
        context_service = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if self.request.user.is_superuser:
            context_service['super_user'] = True
        else:
            context_service['super_user'] = False
        return context_service    

class ReservationDetailView(DetailView):
    model = Reservation
    context_object_name = 'reservation'
    template_name = 'app/reservation_detail.html'      

class ReservationCreateView(CreateView):
    model = Reservation
    fields = ['reservation_date','start_time','end_time','location']
    template_name = 'app/reservation_create.html'

class ReservationUpdateView(UpdateView):
    model = Reservation
    fields = ['reservation_date','start_time','end_time','location']
    template_name = 'app/reservation_update.html'

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'app/reservation_delete.html'    
    context_object_name = 're'
    success_url = reverse_lazy('reservation_list')
# ========================================================================================================
class PaymentListView(ListView):
    model = Payment
    context_object_name = 'payment'
    template_name = 'app/payment_list.html'

def get_context_data(self, **kwargs):
        context_service = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if self.request.user.is_superuser:
            context_service['super_user'] = True
        else:
            context_service['super_user'] = False
        return context_service 

class PaymentDetailView(DetailView):
    model = Payment
    context_object_name = 'payment'
    template_name = 'app/payment_detail.html'    

class PaymentCreateView(CreateView):
    model = Payment
    fields = [ 'amount','payment_date','payment_status']
    template_name = 'app/payment_create.html'         
    
class PaymentUpdateView(UpdateView):
    model = Payment
    fields = [ 'amount','payment_date','payment_status']
    template_name = 'app/payment_update.html'       

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'app/payment_delete.html'    
    context_object_name = 're'
    success_url = reverse_lazy('payment_list')  

# ========================================================================================================
class CourtListView(ListView):
    model = Court
    context_object_name = 'court'
    template_name = 'app/court_list.html'

def get_context_data(self, **kwargs):
        context_service = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if self.request.user.is_superuser:
            context_service['super_user'] = True
        else:
            context_service['super_user'] = False
        return context_service 

class CourtDetailView(DetailView):
    model = Court
    context_object_name = 'court'
    template_name = 'app/court_detail.html'     
      
class CourtCreateView(CreateView):
    model = Court
    fields = [ 'court_Id','courtStatus','location', 'date', 'available']
    template_name = 'app/court_create.html'

class CourtUpdateView(UpdateView):
    model = Court
    fields = [ 'court_Id','courtStatus','location', 'date', 'available']
    template_name = 'app/court_update.html'    

class CourtDeleteView(DeleteView):
    model = Court
    template_name = 'app/court_delete.html'    
    context_object_name = 're'
    success_url = reverse_lazy('court_list')    
# ========================================================================================================
class FeedbackListView(ListView):
    model = Feedback
    context_object_name = 'feedback'
    template_name = 'app/feedback_list.html'

def get_context_data(self, **kwargs):
        context_service = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if self.request.user.is_superuser:
            context_service['super_user'] = True
        else:
            context_service['super_user'] = False
        return context_service     

class FeedbackDetailView(DetailView):
    model = Feedback
    context_object_name = 'feedback'
    template_name = 'app/feedback_detail.html'    

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['rating','comment', 'date']
    template_name = 'app/feedback_create.html'         
    
class FeedbackUpdateView(UpdateView):
    model = Feedback
    fields = ['rating','comment', 'date']
    template_name = 'app/feedback_update.html'       

class FeedbackDeleteView(DeleteView):
    model = Feedback
    template_name = 'app/feedback_delete.html'    
    context_object_name = 're'
    success_url = reverse_lazy('feedback_list')         
# ======================================================================================================== 
class BookingHistoryListView(ListView):
    model = BookingHistory
    context_object_name = 'bookingHistory'
    template_name = 'app/bookingHistory_list.html'

def get_context_data(self, **kwargs):
        context_service = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if self.request.user.is_superuser:
            context_service['super_user'] = True
        else:
            context_service['super_user'] = False
        return context_service

class BookingHistoryDetailView(DetailView):
    model = BookingHistory
    context_object_name = 'bookingHistory'
    template_name = 'app/bookingHistory_detail.html'    

class BookingHistoryCreateView(CreateView):
    model = BookingHistory
    fields = [ 'rating','reservation_date','location']
    template_name = 'app/bookingHistory_create.html'         
    
class BookingHistoryUpdateView(UpdateView):
    model = BookingHistory
    fields = [ 'rating','reservation_date','location']
    template_name = 'app/bookingHistory_update.html'       

class BookingHistoryDeleteView(DeleteView):
    model = BookingHistory
    template_name = 'app/bookingHistory_delete.html'    
    context_object_name = 're'
    success_url = reverse_lazy('bookingHistory_list')  
# ======================================================================================================== 
