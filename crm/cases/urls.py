from django.urls import path
from .views import CaseList,CaseDetails

urlspatterns=[
    path('case/',CaseList.as_view,name='case-list'),
    path('case/<int:pk>/',CaseDetails.as_view,name='case-details')
]