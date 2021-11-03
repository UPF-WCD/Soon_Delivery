"""SoonDelivery_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import account.views as a
import delivery.views as d
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
account = 'account'


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', a.home, name="home"),
    path('login/', a.user_login, name='login'),
    path('signup/', a.user_signup, name='signup'),
    path('activate/<str:uid64>/<str:token>', a.activate, name='activate'),
    path('login/find_id/', a.find_id, name='find_id'),
    path('login/find_password/', a.find_password, name='find_password'),

    path('', d.home, name="home"),
    path('order/<str:user_id>', d.order, name='order'),
    path('order_delivery/<str:order_id>', d.order_delivery, name="order_delivery"),
    path('start_delivery/<str:order_id>', d.start_delivery, name="start_delivery"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
