from django.urls import path
from ems import views

urlpatterns = [
    path('events/', views.eventlist, name='event_list'),
    path('events/<int:event_id>/', views.eventdetail, name='event_detail'),
    path('events/register/', views.register, name='register'),



    path('home/', views.home, name="home"),
    path('user/', views.User_create.as_view(), name="user"),
    path('classb/', views.MyView.as_view(), name="classbased"),
    path('create/', views.UserCreate.as_view(), name="usercreate"),
    path('eventcreate/', views.EventCreate.as_view(), name="eventcreate"),
    path('eventlist/', views.EventList.as_view(), name="eventlist"),
    path('<pk>/update/', views.EventUpdate.as_view(), name="eventupdate"),
    path('<pk>/delete/', views.DeleteEvent.as_view(), name="eventdelete"),
    path('register/', views.RegistrationCreateView.as_view(), name="create-registration"),
    path('<pk>/registerupdate', views.RegistrationUpdateView.as_view(), name="update-registration"),
    path('<pk>/registerdelete/', views.RegistrationDeleteView.as_view(), name="registerdelete"),
]
