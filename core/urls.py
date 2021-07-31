
from django.contrib import admin
from django.urls import path
from task2.views import ReviewEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    # reviews/
    path('', ReviewEmailView.as_view(), name='reviews')
]
