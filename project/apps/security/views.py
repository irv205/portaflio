from rest_framework import status, viewsets, exceptions, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import Response, APIView
from rest_framework.decorators import api_view, action
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from project.common.pagination import PageNumberPagination
from project.apps.security.models import User
from django.http import HttpResponse
from . import serializers
from . import utils
from . import models
import json

class UsersView(APIView):
    
    permission_classes = (permissions.IsAuthenticated, )

    def put(self, request, pk):
        user = models.User.objects.get(pk=pk)
        serializer = serializers.UserDetailSerializer(
            user, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            password = request.data.get('password', None)
            if password:
                user.set_password(request.data.get('password'))
                user.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = models.User.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return Response(None, 204)

class UserInfo(viewsets.ModelViewSet):

    model = models.User
    permission_classes = ()
    serializer_class = serializers.UserDetailSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.filter(queryset)

    def filter(self, queryset):
        kwargs = self.request.GET
        id = kwargs.get('id', None)
        type = kwargs.get('type', None)
        is_active = kwargs.get('is_active', None)
        first_name = kwargs.get('first_name',None)
        last_name = kwargs.get('last_name', None)

        queryset = queryset.filter(
            is_active=True,
        )

        if id:
            queryset = queryset.filter(
                id = id
            )

        if type:
            queryset = queryset.filter(
                type = type
            )

        if first_name:
            queryset = queryset.filter(
                first_name = first_name
            )
        if last_name:
            queryset = queryset.filter(
                last_name = last_name
            )

        if is_active:

            if is_active == 'false':
                is_active = False
            if is_active == 'true':
                is_active = True

            queryset = queryset.filter(
                is_active = is_active
            )

        return queryset

    @action(detail=False, methods=['get'], name='get-user-auth')
    def get_me(self, request):

        user = User.objects.filter(id = request.user.id).first()
        serializer = serializers.UserDetailSerializer(user)  

        return Response(serializer.data)            

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer


class ResetPasswordView(APIView):
    permission_classes = ()

    def put(self, request):
        serializer = serializers.ResetPasswordSerializer(
            data=request.data
        )
        if serializer.is_valid():
            user = utils.get_user_by_code(code=request.data.get('code'))
            # Set value reminder
            user.set_password(request.data.get('password'))
            user.reminder = None
            user.save()

            return Response({'success': 'ok'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecoverPasswordView(APIView):
    permission_classes = ()

    def post(self, request):

        email = request.data.get('email', None)

        user = utils.user_by_email(email=email)
        if not user:
            raise exceptions.ValidationError('Not exist email {}'.format(
                email
            ))

        # Send sms validation
        from project.common import utils as cutils
        from django.conf import settings
        reminder = cutils.random_with_N(10)
        # Set value reminder
        user.reminder = reminder
        user.save()

        link = '{}/reset-password/{}'.format(
            settings.URL_WEBSITE,
            reminder
        )
        subject = 'Recuperar contraseña'
        cutils.send_mail(
            recipient=[user.email],
            subject=subject,
            template='email/recover-password.html',
            context={
                    'display_name': user.display_name(),
                    'site': settings.APPNAME,
                    'link': link
            }
        )

        return Response({'success': 'ok'}, status=status.HTTP_200_OK)


class RegisterView(CreateAPIView):
    permission_classes = ()

    from django.views.decorators.debug import sensitive_post_parameters
    from django.utils.decorators import method_decorator
    sensitive_post_parameters_m = method_decorator(
        sensitive_post_parameters('password', 'password_confirm')
    )
    serializer_class = serializers.RegisterSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        from django.utils.six import text_type
        refresh = RefreshToken.for_user(user)
        cxt = {
            'refresh': text_type(refresh),
            'access': text_type(refresh.access_token)
        }
        # print('response data', cxt)
        return cxt

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            self.get_response_data(user),
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        # Send mail confirmation
        # user.send_confirmation_mail()
        return user


# Function 404
def error_404_def(request, exception):
    data = {
        'message': 'Endpoint was not found or has been removed',
        'code': 1019
    }

    return HttpResponse(
        json.dumps(data), content_type='application/json', status=400
    )


@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def error_404_view(request):
    # print(request.method)

    try:
        return Response(
            {
                'message': 'Endpoint was not found or has been removed',
                'code': 1019
            },
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        print(e)
        return Response(None, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
