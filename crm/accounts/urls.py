from django.urls import path
from .views import AccountListAPIView,AccountDetail


urlpatterns = [
    path('account/',AccountListAPIView.as_view(),name='account-list'),
    path('account/<int:pk>/',AccountDetail.as_view(),name='account-detail')
]
