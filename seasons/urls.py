from django.urls import path
from .views import SeasonDetailApiView

app_name = 'seasons'


urlpatterns = [
    path(
        '<int:number>/',
        SeasonDetailApiView.as_view(), 
    
    # name='news-year-archive'
    ),
]