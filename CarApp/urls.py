from django.urls import path
from .import views

urlpatterns = [
    path('',views.Car_list,name='Car_List'),
    path('<int:pk>',views.Car_details,name='Car_details'),
    path('showroom',views.Showroom_View.as_view(),name='showroom_view'),
    path('showroom/<int:pk>',views.Showroom_Detail.as_view(),name='showroom_detail'),
    path('rev',views.Review_view.as_view(),name='review_view'),
    path('rev/<int:pk>',views.Rev_Detail.as_view(),name='Rev_Detail'),

]
