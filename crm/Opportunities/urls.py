from django.urls import path
from .views import opportunityList,opportunityDetail


urlspatterns=[
    path('opportunity/',opportunityList.as_view,name='opportunity-list'),
    path('opportunity/<int:pk>/',opportunityDetail.as_view,name='opprtunity-details')
]