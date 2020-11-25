from django.urls import path

from .views import ReadingView

urlpatterns = [path("", ReadingView.as_view())]
