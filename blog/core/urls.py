from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('core/', views.CoreList.as_view()),
    path('core/<int:pk>', views.CoreDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)