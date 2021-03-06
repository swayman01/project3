"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.conf.urls import url
from orders import views as core_views
from django.views.generic.base import TemplateView # see https://dev.to/jonesoncorners/series-login-logout-authentication-in-django-part-i-4gf4

urlpatterns = [
    path("", include("orders.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # see https://dev.to/jonesoncorners/series-login-logout-authentication-in-django-part-i-4gf4
    path('', TemplateView.as_view(template_name ='home.html'), name = 'home'),
    # path('logout/',
    # auth_views.Logout.as_view(template_name='logged_out.html'),)
    # url(r'^signup/$', core_views.signup, name='signup'),
    #path('project3/templates/registration/login.html'),
#project3/templates/registration
]
# print("32 urlpatterns: ", urlpatterns)
# BASE_DIR:  /Users/swayman/Documents/Classes/CS50/CS50_Web_Programming/project3

# urlpatterns:  [<URLResolver <module 'orders.urls' from '/Users/swayman/Documents/Classes/CS50/CS50_Web_Programming/project3/orders/urls.py'> (None:None) ''>,
# <URLResolver <URLPattern list> (admin:admin) 'admin/'>, <URLResolver <module 'django.contrib.auth.urls' from '/Users/swayman/anaconda3/lib/python3.7/site-packages/django/contrib/auth/urls.py'> (None:None) 'accounts/'>]

# Result from Django Tutorial : http://127.0.0.1:8000/accounts/login/?next=/catalog/
# <li><a href="{% url 'login'%}?next={{request.path}}">Login</a></li>
