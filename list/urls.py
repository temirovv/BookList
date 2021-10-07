from django.urls import path
from .views import (  # BookListView,
    # BookCreateView,
    index,
    BookUpdateView,
    BookDeleteView,
)


urlpatterns = [
    path('', index, name='home'),
    #    path('', BookListView.as_view(), name='home'),
    #    path('create/', BookCreateView.as_view(), name='create'),
    path('edit/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete'),
]
