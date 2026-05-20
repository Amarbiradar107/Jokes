from django.contrib import admin
from django.urls import path
from .views import JokesDetails
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',JokesDetails.as_view(),name='jokes'),
]
