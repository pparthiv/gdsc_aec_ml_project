# urls.py
from django.urls import path
from .views import classify_image, linear_regression, index

urlpatterns = [
    path('', index, name='index'),
    path('classification', classify_image, name='classify_image'),
    path('lin_reg', linear_regression, name='linear_reg')
]