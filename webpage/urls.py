from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.index_page, name="home"),
    path('login', views.login_page, name="login"),
    path('signup', views.signup_page, name="signup"),
    path('stocks', views.stocks_page, name ="stocks"),
    path('stocks/<str:symbol>/', views.get_stock_data, name='get_stock_data'),
    path('signout', views.signout, name ="signout"),
    path('portfolio', views.portfolio_page, name ="portfolio"),
    path('add_portfolio', views.add_portfolio, name="add_portfolio"),
    path('remove_portfolio', views.remove_portfolio, name="remove_portfolio")
]

