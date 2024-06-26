from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredients/', include('ingredients.urls')),
    path('recipe/', include('recipe.urls'))
]