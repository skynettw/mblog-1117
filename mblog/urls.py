from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto, showpost


urlpatterns = [
	path('post/<str:slug>/', showpost),
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('', homepage),
]
