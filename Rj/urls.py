"""
URL configuration for Rj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from user import views
from user.models import Menu
urlpatterns = [
    path('',views.index,name="home"),
    path('createid/',views.create_id,name="create_order_id"),
    path('datasave/',views.datasave,name="myform"),
    path('show_table/',views.menu,name="menu"),
    path('login/',views.register_p,name="manager"),
    path('register/',views.register_save,name="myform"),
    path('login_p/',views.login_page,name="login_page"),
    path('login_manager/',views.login22,name="login2_check"),
    path('manager/',views.addmenu,name="add_menu"),
    path('addmenu',views.addmenu2,name="menu_check"),
    path('show_t/',views.td,name="show_menu"),
    path('update_p/',views.showmenu2,name="menu_update"),
    path('idupdate/id_update/<int:id>/',views.id_update,name="menu_id_update"),
    path('menu_id_update/',views.save_update,name="menu_id_update"),
    path('id_delete/id_delete/<int:id>/',views.id_delete,name="menu_id_delete"),
    path('showtable/',views.show_menu,name="show_table"),
    path('show_menu2/',views.show_menu2,name="show_menu"),
    path('order/',views.order,name="order"),
    path('orderdata/',views.orderdata,name="orderdata"),
    path('bill_p/',views.bill_page,name="bill_page"),
    path('admin/', admin.site.urls),
    
    
]

