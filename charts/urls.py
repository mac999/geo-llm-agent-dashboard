from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('charts/', views.index, name='charts'),
	path('scan_view/', views.scan_view, name='scan_view'),
	path('flow_view/', views.flow_view, name='flow_view')
]