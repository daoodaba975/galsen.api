from django.urls import path

from . import views

urlpatterns = [

    path('', views.pays_view, name='home'),
    path('departement/', views.departement_view, name='departement'),
    path('region/', views.region_view, name='region'),
    path('village/', views.village_view, name='village'),


    path('api/pays/', views.PaysList.as_view(), name='pays_list'),
    path('api/departements/', views.DepartementsList.as_view(), name='departements_list'),
    path('api/departements/<int:pk>/', views.DepartementsDetail.as_view(), name='departements_detail'),
    path('api/regions/', views.RegionsList.as_view(), name='regions_list'),
    path('api/regions/<int:pk>/', views.RegionsDetail.as_view(), name='regions_detail'),
    path('api/villages/', views.VillageList.as_view(), name='villages_list'),
    path('api/villages/<int:pk>/', views.VillageDetail.as_view(), name='villages_detail'),
]
