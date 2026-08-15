from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [

    # Home page
    path(
        "",
        views.home,
        name="home"
    ),

    # Django Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Login
    path(
        "djangoapp/login",
        views.login_user,
        name="login"
    ),

    # Logout
    path(
        "djangoapp/logout",
        views.logout_user,
        name="logout"
    ),

    # Dealer reviews API
    path(
        "djangoapp/dealer/<int:dealer_id>/reviews",
        views.get_dealer_reviews,
        name="dealer_reviews"
    ),

    # All dealers
    path(
        "djangoapp/get_dealers",
        views.get_all_dealers,
        name="get_all_dealers"
    ),

    # Dealer by ID
    path(
        "djangoapp/dealer/<int:dealer_id>",
        views.get_dealer_by_id,
        name="get_dealer_by_id"
    ),

    # Dealers by state
    path(
        "djangoapp/dealers/<str:state>",
        views.get_dealers_by_state,
        name="get_dealers_by_state"
    ),

    # All car makes and models
    path(
        "djangoapp/get_cars",
        views.get_all_car_makes,
        name="get_all_car_makes"
    ),

    # Sentiment analysis
    path(
        "djangoapp/analyze",
        views.analyze_review,
        name="analyze_review"
    ),

    # Dealer details + reviews webpage
    path(
        "dealer/<int:dealer_id>/reviews",
        views.dealer_details_reviews,
        name="dealer_details_reviews"
    ),

    # Post Review page
    path(
        "dealer/<int:dealer_id>/post-review",
        views.post_review_page,
        name="post_review"
    ),
]