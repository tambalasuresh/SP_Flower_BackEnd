from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('emp_list',EmpDetailsList,'Emp_list')
# router.register('updateEmp_list/<int:pk>',views.EmpDetailstUpdate,'updateEmp_list')
router.register('position_list',PositionList,'position_list')
router.register('comment_list',CommentList,'comment_list')
router.register('shoping_list',ShopingCheckoutList,'shoping_list')

urlpatterns = [
    path('', registration_create),
    path('registration_list/',registration_list, name='registration_list'),
    path("api/",include(router.urls))
    #  path('emp_list/', views.EmpDetailsList.as_view(),name='test'),
]