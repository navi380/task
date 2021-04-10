from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from .views import *

from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
# router.register(r'item_found', ListFoundItem)

urlpatterns = [
    path('', include(router.urls)),
    path('found_items', found_items, name='found_items'),
    path('lost_items', lost_items, name='lost_items'),
    path('add_item', add_item, name='add_item'),
    path('item_instance/<int:id>/', detail_update_or_delete, name='item_instance'),
]