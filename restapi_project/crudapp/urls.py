from django.urls import path, include
from crudapp import views

# Model View Set Operations
from rest_framework.routers import DefaultRouter
#create router object
router = DefaultRouter()
# register router
router.register('mixoperation', views.MultiOperation, basename='mixoperation')

urlpatterns = [
    path('newoperation/', views.NewOperation.as_view(), name='newoperation'),
    path('nextoperation/<int:pk>/', views.NextOperation.as_view(), name='nextoperation'),
    path('', include(router.urls)),
]
