from django.shortcuts import render
from .models import Event, Registration
from .forms import EventForm, RegistrationForm


def eventlist(request):

    events = Event.objects.all()
    return render(request, 'eventlist.html', {"events":events} )


def eventdetail(request, event_id):

    event = Event.objects.get(id=event_id)
    return render(request, 'eventdetail.html', {'event':event})
    

def register(request, event_id):


    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = Registration(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email']
            )

            registration.save()
            return render(request, 'registration_confirmation.html')
    else:
        form = RegistrationForm()

        return render(request, 'register.html', {'form': form})


from django.shortcuts import render, HttpResponse, redirect
from .models import User, Event, Registration
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User


# Create your views here.

def home(request):

    return HttpResponse("This s home page")


class MyView(View):
    name = "Dawood"
    def get(self, request):
        # return HttpResponse('Class based view!')
        return HttpResponse(self.name)
    

class UserCreate(CreateView):

    template_name = 'user_form.html'

    model = User

    fields = ['name', 'email', 'address']


class EventCreate(CreateView):

    template_name = 'event_form.html'
    model = Event
    fields = ['title', 'description', 'location']
    success_url = '/cbv/thanks/'


class EventList(ListView):

    template_name = 'event_list.html'
    model = Event
    fields = ['title', 'description', 'location']


class EventUpdate(UpdateView):

    template_name = 'event_form.html'
    model = Event
    fields = ['title', 'description', 'location']


class DeleteEvent(DeleteView):

    template_name = 'event_confirm_delete.html'
    model = Event
    fields = ['title', 'description', 'location']


class RegistrationCreateView(CreateView):

    model = Registration
    template_name = 'registration_form.html'
    fields = ['event', 'name', 'email']


class RegistrationUpdateView(UpdateView):

    model = Registration
    template_name = 'registration_form.html'
    fields = ['event', 'name', 'email']


class RegistrationDeleteView(DeleteView):

    model = Registration
    template_name = 'registration_confirm_delete.html'


class User_create(CreateView):

    model = User
    template_name = 'user_form.html'
    fields = ['username', 'email', 'password']
    success_url = '/thanks.html/'


