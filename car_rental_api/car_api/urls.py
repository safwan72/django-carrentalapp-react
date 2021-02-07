
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent_car/', include('rent_a_car.urls')),
    path('',views.index,name='index'),
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)