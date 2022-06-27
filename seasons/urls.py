from django.urls import path
from .views import SeasonDetailApiView, SeasonApiView

app_name = 'seasons'


urlpatterns = [

    path("", SeasonApiView.as_view()),
    path('<int:number>/',
        SeasonDetailApiView.as_view(), 
        # name='news-year-archive'
    ),
]