from rest_framework import generics
from .models import Core
from .serializers import CoreSerializer

# Create your views here.
class CoreList(generics.ListCreateAPIView):
    queryset = Core.objects.all()
    serializer_class = CoreSerializer

class CoreDetails(generics.RetrieveUpdateAPIView):
    queryset = Core.objects.all()
    serializer_class = CoreSerializer