# urls.py
from django.urls import path
from .views import classify_image, linear_regression

urlpatterns = [
    path('classification', classify_image, name='classify_image'),
    path('lin_reg', linear_regression, name='linear_reg')
]