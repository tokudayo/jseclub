from .views import *
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('event/', HomeView.as_view(type="event", title='Events', createbutton='Create an event'), name='homeevent'),
    path('event/create', login_required(CreateView.as_view(type='event', title='Create an event post now!', subtitle='Makes JS an even greater place to be a part of', selfurl='createevent', redirecturl='detailevent')), name='createevent'),
    path('event/<int:id>', login_required(DetailView.as_view(type = 'event', selfurl='detailevent')), name='detailevent'),

	path('training/', HomeView.as_view(type='training', title='Trainings', createbutton='Create a training post'), name='hometraining'),
    path('training/create', login_required(CreateView.as_view(type='training', title='Create a training post now!', subtitle='“Knowledge is power.” – Francis Bacon', selfurl='createtraining', redirecturl='detailtraining')), name='createtraining'),
    path('training/<int:id>', login_required(DetailView.as_view(type='training', selfurl='detailtraining')), name='detailtraining'),

    path('confession/', HomeView.as_view(), name='homeconfession'),
    path('confession/create', login_required(CreateView.as_view()), name='createconfession'),
    path('confession/<int:id>', login_required(DetailView.as_view()), name='detailconfession'),
]