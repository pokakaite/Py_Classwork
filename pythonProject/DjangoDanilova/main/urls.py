from django.contrib import admin
from django.urls import path, include
from . import views


# urlpatterns = [
#     path('', views.one)
    # path('', views.lol),
    # path('about', views.about)
# ]

# urlpatterns = [
#     path('', views.main),
#     path('news/', views.news),
#     path('about/', views.about),
#     path('contacts/', views.contacts)
# ]


urlpatterns = [
    path('', views.main),
    # path(f'z/<int:age>', views.z_age),
    # path(f'm/<int:age>', views.m_age),
]

