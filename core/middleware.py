# middleware.py

import json
import requests
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

HCAPTCHA_VERIFY_URL = 'https://hcaptcha.com/siteverify'


class hCaptchaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip hCaptcha check for authenticated users or other criteria if needed
        if request.user.is_authenticated:
            return self.get_response(request)

        # Skip hCaptcha check for the hCaptcha challenge page itself
        if request.path == reverse('hcaptcha_challenge'):
            return self.get_response(request)

        if not request.session.get('hcaptcha_verified', False):
            return redirect('hcaptcha_challenge')

        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == 'POST' and request.path == reverse('hcaptcha_challenge'):
            hcaptcha_response = request.POST.get('h-captcha-response')
            if not hcaptcha_response:
                return HttpResponse('Captcha response is missing', status=400)

            data = {
                'secret': settings.HCAPTCHA_SITEKEY,
                'response': hcaptcha_response,
                'remoteip': request.META.get('REMOTE_ADDR')
            }
            response = requests.post(HCAPTCHA_VERIFY_URL, data=data)
            result = response.json()
            print(result)
            if not result.get('success'):
                request.session['hcaptcha_verified'] = True
                print("alo")
                return redirect(request.session.get('original_path', '/'))
            else:
                return HttpResponse('Captcha verification failed', status=400)

        return None
