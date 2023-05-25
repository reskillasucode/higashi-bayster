from django.urls import path
from . import views

urlpatterns = [
    path('land/', views.LandListView.as_view(), name='land_list'),
    path('land/<int:pk>/', views.LandDetailView.as_view(), name='land_detail'),
    path('create/', views.LandeCreateView.as_view(), name='land_create'),
]
