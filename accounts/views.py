from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'  # 또는 'email'