from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('list', views.DoctorViewset) # router er antena
router.register('designation', views.DesignationViewset) 
router.register('specialization', views.SpecializationViewset) 
router.register('available_time', views.AvailableTimeViewset) 
router.register('review', views.ReviewViewset) 

urlpatterns = [
    path('', include(router.urls)),
]