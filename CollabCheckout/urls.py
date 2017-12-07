from django.conf.urls import patterns, url
from CollabCheckout import views

urlpatterns = patterns('',
                       url(r"^$",views.checkout, name = 'checkout'),
                       url(r"^period_list/$", views.period_list, name='period_list'),
                       url(r"^room_list/$", views.room_list, name='room_list'),
                       url(r"^cs/$", views.active_rooms, name='cs'),
                       url(r"^manycheckouts/$", views.checkout_many_rooms, name=',many_checkouts'),
                       url(r"^login/$", views.user_login, name='login'),
                       )