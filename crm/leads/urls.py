from django.urls import path
from .views import LeadListAPIView, LeadDetail  # Corrected view import names

urlpatterns = [
    path('lead/', LeadListAPIView.as_view(), name='lead-list'),  # Added parentheses for as_view()
    path('lead/<int:pk>/', LeadDetail.as_view(), name='lead-details'),  # Added parentheses for as_view()
]
