from django.urls import path
from.views import index, about_, contact_, gallery_, service_,sample_
urlpatterns = [
    path('', index, name='index'),
    path('about/', about_, name='about'),
    path('contact/', contact_, name='contact'),
    path('gallery/', gallery_, name='gallery'),
    path('service/', service_, name='service'),
    path('product/', sample_, name='product')
]
