"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import math
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def rectangle_area(request, height, width):
        response = HttpResponse(f'<h1> HEIGHT * WIDTH = AREA<h1><h2> {height} * {width} = {height * width}<h2>')
        return response
        # response.status_code = 400

def rectangle_perimeter(request, height, width):
        response = HttpResponse(f'<h1> HEIGHT + WIDTH * 2 = PARRIMETER<h1><h2> {height} + {width} * 2 = {(height + width)*2}<h2>')
        return response
        # response.status_code = 400

def circle_area(request, radius):
        response = HttpResponse(f'<h1>A=πr2<h1><h2> AREA = π * RADIUS^2 <h2><h3>{round(math.pi, 2)} * {radius}^2 ≈ {round(radius**2 * math.pi, 2)}<h3>')
        return response
        # response.status_code = 400

def circle_perimeter(request, radius):
        response = HttpResponse(f'<h1>C=2πr<h1><h2> CIRCUMFERENCE = 2 * π * RADIUS<h2><h3> 2 * {round(math.pi, 2)} * {radius} ≈ {round(radius * 2 * math.pi, 2)}<h3>')
        return response
        # response.status_code = 400

# def response_error_handler(request, exception=None):
#     return HttpResponse('Error handler content', status=403)


# def permission_denied_view(request):
#     raise PermissionDenied

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/area/<int:height>/<int:width>/', rectangle_area),
    path('rectangle/perimeter/<int:height>/<int:width>/', rectangle_perimeter),
    path('circle/area/<int:radius>/', circle_area),
    path('circle/perimeter/<int:radius>/', circle_perimeter),
    # path('403/', permission_denied_view),
    ]

# handler403 = response_error_handler


# # ROOT_URLCONF must specify the module that contains handler403 = ...
# @override_settings(ROOT_URLCONF=__name__)
# class CustomErrorHandlerTests(SimpleTestCase):

#     def test_handler_renders_template_response(self):
#         response = self.client.get('/403/')
#         # Make assertions on the response here. For example:
#         self.assertContains(response, 'Error handler content', status_code=403)