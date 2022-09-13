from django.core.exceptions import PermissionDenied
import datetime
import json


class LogUserInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        url = request.path_info
        method = request.method

        data = {
            'ip': ip,
            'date': start_time,
            'url': url,
            'method': method
        }
        with open('user_info.log', 'a') as f:
            f.write(json.dumps(data) + '\n')

        response = self.get_response(request)
        return response
#
#
# class SecondIPMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         blocked_ips = ['127.0.0.1']
#         ip = request.META.get('REMOTE_ADDR')
#         if ip in blocked_ips:
#             raise PermissionDenied
#         response = self.get_response(request)
#
#         return response


# class ThirdIPMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         time.sleep(10)
#         allowed_ips = ['127.0.0.1']
#         ip = request.META.get('REMOTE_ADDR')
#         if ip not in allowed_ips:
#             raise PermissionDenied
#         response = self.get_response(request)

        # return response


# class FourthIPMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         count = cache.get_or_set(f'ip:{ip_address}', 10)
#         count += 1
#         if count > 10:
#             raise Exception('Давай, - до свидания')
#         else:
#             cache.set(f'ip:{ip_address}', count, 5)
        #     allowed_ips = ['127.0.0.1']
        #     ip = request.META.get('REMOTE_ADDR')
        #     if ip not in allowed_ips:
        #         raise PermissionDenied
        #     response = self.get_response(request)
        #
        # return response