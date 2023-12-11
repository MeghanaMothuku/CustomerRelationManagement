from django.urls import path
from .views import contactListAPIView, contactDetail  # Corrected view import names

urlpatterns = [
    path('contact/', contactListAPIView.as_view(), name='contact-list'),  # Added parentheses for as_view()
    path('contact/<int:pk>/', contactDetail.as_view(), name='contact-details'),  # Added parentheses for as_view()
]
