from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"  # "127.0.0.1:8000/account/hello" -> "accountapp:hello"

urlpatterns = [
    # path('hello/', hello, name="hello"),
    path('create/', AccountCreateView.as_view(), name='create'),

    # For LoginView, indicating 'template_name' is required.
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Detail(Read)
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

    # Update
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

    # Delete
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]