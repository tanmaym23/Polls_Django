from django.urls import path
from projectpolls.views import *

urlpatterns=[
    # path('showpolls/',show_polls)
    path('',index),
    path('<int:question_id>/',details,name='detail'),
    path('<int:question_id>/result/',result,name='result'),
    path('<int:question_id>/vote/',vote,name='vote')
]