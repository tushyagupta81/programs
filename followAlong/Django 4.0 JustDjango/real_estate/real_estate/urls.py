from django.contrib import admin
from django.urls import path

from listings.views import listings_list,listings_retrive,listings_form,listings_update,listings_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path("listings/",listings_list),
    path('listings/<pk>/',listings_retrive),
    path('add-listings/',listings_form),
    path('listings/<pk>/edit/',listings_update),
    path('listings/<pk>/delete/',listings_delete),
]
