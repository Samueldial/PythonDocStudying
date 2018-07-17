from django.urls import path
from .views import home, produto

urlpatterns = [
    path('', home),
    path('produto/<int:codigo>/', produto),
]

#request > urls > view > model > response
