from django.urls import path
from rest_framework_simplejwt import views as auth_views

from budgets.infrastructure import views


urlpatterns = [
    path("api/v1/login", auth_views.TokenObtainPairView.as_view(), name="login"),
    path(
        "api/v1/login/refresh",
        auth_views.TokenRefreshView.as_view(),
        name="login_refresh",
    ),
    path("api/v1/register", views.UserRegistrationView.as_view(), name="register"),
    path("api/v1/budget", views.BudgetView.as_view(), name="budget"),
    path("api/v1/budget/invitation", views.InvitationView.as_view(), name="invitation"),
    path(
        "api/v1/budget/balance_change",
        views.BalanceChangeView.as_view(),
        name="balance_change",
    ),
]
