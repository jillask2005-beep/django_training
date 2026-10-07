from django.urls import path
from .views import StudentView
from .views import EmployeeView
from .views import MovieView
from .views import productView
from .views import BookView
from .views import StudentdetailsView
from .views import EmployeeDetailView,BookDetailsView,MovieDetailsView,ProductDetailView,filterView
from .views import *


urlpatterns = [
    path("getstud/", StudentView.as_view()),
    path("getemp/",EmployeeView.as_view()),
    path("getmovie/",MovieView.as_view()),
    path("getprot/",productView.as_view()),
    path("getBook/",BookView.as_view()) ,
    path("getstudet/<int:pk>/",StudentdetailsView.as_view()),
    path("getempd/<int:pk>/",EmployeeDetailView.as_view()),
    path("getbooksd/<int:pk>/",BookDetailsView.as_view()),
    path('getmoviesd/<int:pk>/',MovieDetailsView.as_view()),
    path('getproductd/<int:pk>/',ProductDetailView.as_view()),
    path("getfilt/",filterView.as_view()),
    path('img/',Imageview.as_view()),
    path('imgd/<int:pk>/',ImageViewDeails.as_view()),
    path('sign/',Signup.as_view()),
    path('login/',LoginView.as_view())
    
]

