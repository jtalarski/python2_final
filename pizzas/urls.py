from django.urls import path, include, re_path
from rest_framework import routers
from . import views

# Setup routers
# router = routers.DefaultRouter()
# router.register(r'pizza', views.PizzaViewSet)

urlpatterns = [
    # For initial function view
    # path('', views.home, name='pizzas-home'),
    
    # Builtin Django class views 
    path('', views.PizzaListView.as_view(), name='pizzas-home'),
    # Use dynamic URL syntax to pass pizza id
    path('pizza/<int:pk>', views.PizzaDetailView.as_view(), name="pizza-detail"),
    path('pizza/create/', views.PizzaCreateView.as_view(), name='pizzas-create'),
    path('pizza/<int:pk>/update/', views.PizzaUpdateView.as_view(), name="pizzas-update"),
    path('pizza/<int:pk>/delete/', views.PizzaDeleteView.as_view(), name="pizzas-delete"),
    path('about/', views.about, name='about the app'),
    path('recipe_text/', views.recipe_text, name="recipe_text"), 
    path("pizza/submission/", views.SubmissionCreateView.as_view(), name="submissions-create"),
    path('pizza/sub_list/', views.SubmissionListView.as_view(), name="sub-home"),
    path('sub_detail/<int:pk>', views.SubmissionDetailView.as_view(), name="submission-detail"),
    
    # Specific views that provide for Bokeh visualizations. These are used primarily because the views
    # are linked to different style sheets and Javascript libraries than those accessed through
    # pizzas/template/pizzas/base.html 
    path('graph3/', views.graph3, name='popular'),
    path('graph4/', views.graph4, name='calories'),
]