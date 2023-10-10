from rest_framework import generics

from account.models import CustomUser
from account.api.serializers import UserSerializer


class GetUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        print(123)
        return CustomUser.objects.all()
