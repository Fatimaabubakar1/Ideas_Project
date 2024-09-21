from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('ai/', views.ai_page, name='ai'),
    path('blockchain/', views.blockchain_page, name='blockchain'),
    path('bi/', views.bi_page, name='bi'),
    path('cybersecurity/', views.cybersecurity_page, name='cybersecurity'),
    path('dataanalytics/', views.dataanalytics_page, name='dataanalytics'),
    path('softwareenginering/', views.softwareengineering_page, name='softwareenginering'),
    path('result/', views.result_page, name='result'),
]