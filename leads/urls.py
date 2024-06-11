from django.urls import path

from .views import (DetailView, LeadCreateView, LeadDeleteView, LeadListView,
                    LeadUpdateView, lead_create, lead_delete, lead_detail,
                    lead_list, lead_update)

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', DetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
]
