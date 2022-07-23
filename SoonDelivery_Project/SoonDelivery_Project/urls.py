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
import chat.views as c
import delivery.views as d
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
account = 'account'


urlpatterns = [
    # path('실제 보이는 url', 뷰 메서드, name = '템플릿에서 부르는 액션 이름'),
    path('admin/', admin.site.urls),
    # path('', a.home, name="home"),
    path('', a.user_login, name='login'),
    path('logout/', a.user_logout, name='logout'),
    path('signup/', a.user_signup, name='signup'),
    path('activate/<str:uid64>/<str:token>', a.activate, name='activate'),
    path('login/find_id/', a.find_id, name='find_id'),
    path('login/find_password/', a.find_password, name='find_password'),
    path('my_delivery_history/<str:user_id>', a.my_delivery_history, name='my_delivery_history'),
    path('my_order_history/<str:user_id>', a.my_order_history, name='my_order_history'),
    path('delivery_detail/<str:delivery_id>', a.delivery_detail, name='delivery_detail'),
    path('order_detail/<str:delivery_id>', a.order_detail, name='order_detail'),
    path('finished_delivery/<str:delivery_id>', a.finish_delivery, name='finish_delivery'),
    path('finished_order/<str:delivery_id>', a.finish_order, name='finish_order'),
    path('mypage/<str:user_id>', a.mypage, name='mypage'),
    path('user/api/checkNickname', a.checkNickname),
    path('user/api/checkUsername', a.checkUsername),
    path('user/api/checkEmail', a.checkEmail),
    path('check/', a.check, name='check'),
    # path('mypage/<str:user_id>', a.update, name='update'),
    # path('', d.welcome, name="welcome"),
    path('chat/<str:user_id>', c.chat, name="chat"),
    path('chat/str:user_id/<str:room_name>/', c.room, name="room"),
    path('chat/create_room/', c.create_room, name="create_room"),
    path('main/', d.home, name="home"),
    path('order/<str:user_id>', d.order, name='order'),
    path('order_delivery/<str:order_id>', d.order_delivery, name="order_delivery"),
    path('start_delivery/<int:room_id>/<int:user_id>/<str:order_id>', d.start_delivery, name="start_delivery"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
