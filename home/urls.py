from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index,name='home'),
     path("about", views.about,name='about'),
      path("contact", views.contact,name='contact'),
        path("services", views.services,name='services'),
          path("products", views.products,name='products'),
           path("login", views.loginuser,name='login'),
              path("loggedin", views.loggedin,name='loggedin'),
                path("logout", views.logoutuser,name='logout')
]
