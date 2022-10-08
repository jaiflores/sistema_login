from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]



# Configure Admin Titles
admin.site.site_header = "Ômega 200 Adminitration page"
admin.site.site_title = "Ômega 200"
admin.site.index_title = "Ômega 200"