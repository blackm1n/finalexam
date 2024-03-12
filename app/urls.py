from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('all_recipes/<int:page>/', views.all_recipes, name='all_recipes'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('your_recipes/<int:page>/', views.your_recipes, name='your_recipes'),
    path('edit_recipe/<int:id>/', views.edit_recipe, name='edit_recipe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)