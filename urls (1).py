from django.urls import path
from . import views
urlpatterns = [path("health/",views.health),path("bank/",views.bank),path("partner/",views.partner),path("control/",views.control)]
