from django.urls import path
from . import views


urlpatterns = [
    # URL de atores
    path('actors/', views.ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
