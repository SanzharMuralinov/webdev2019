from api.models import TaskList
from api.serializers import TaskListSerializer2, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib import auth
from django.contrib.auth.models import User, _user_get_all_permissions
from rest_framework import generics
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, BaseAuthentication

class TaskList2(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
    http_method_names = ['get']


class TaskList3(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (IsAuthenticated,)


@permission_classes((IsAuthenticated,))
@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)


