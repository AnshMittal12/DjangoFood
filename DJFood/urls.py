"""DJFood URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import Foodview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodinterface/',Foodview.FoodInterface),
    path('fetchallfoodtypes/',Foodview.FetchAllFoodTypes),
    path('fetchallfooditems/',Foodview.FetchAllFooditmes),
    path('foodsubmit',Foodview.FoodSubmit),
    path('fetchallfood/',Foodview.FetchAllFoods),
    path('displaybyid/',Foodview.DisplayById),
    path('edit_food_data',Foodview.Edit_Food_Data),
    path('displaypicture',Foodview.DisplayPicture),
    path('edit_picture',Foodview.Edit_Picture),
]

