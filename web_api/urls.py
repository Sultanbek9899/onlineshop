from django.urls import path
from .views import CategoryListView

urlpatterns = [
    path('<slug:category_slug>/', CategoryListView.as_view()),
    path('', CategoryListView.as_view())
]