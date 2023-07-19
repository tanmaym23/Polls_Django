from django.urls import path
from . import views
# from myapp.views import hi

urlpatterns=[
    path('hello/',views.hello),
    path('info/',views.info),
    path('classhi/',views.hi.as_view())
]