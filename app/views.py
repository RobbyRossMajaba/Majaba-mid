from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from .models import Reservation
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'    

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'   


class ReservationListView(ListView):
    model = Reservation
    context_object_name = 'reservation'
    template_name = 'app/reservation_list.html'

class ReservationDetailView(DetailView):
    model = Reservation
    context_object_name = 'reservation'
    template_name = 'app/reservation_detail.html'      

class ReservationCreateView(CreateView):
    model = Reservation
    fields = ['date','start_time','end_time','is_confirmed']
    template_name = 'app/reservation_create.html'

class ReservationUpdateView(UpdateView):
    model = Reservation
    fields = ['date','start_time','end_time','is_confirmed']
    template_name = 'app/reservation_update.html'

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'app/reservation_delete.html'    
    context_object_name = 're'
    success_url = reverse_lazy('reservation_list')

    
 
