from django.urls import path
from .views import (
    index,
    BookUpdateView,
    BookDeleteView,
)


urlpatterns = [
    path('', index, name='home'),
    path('edit/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete'),
]
