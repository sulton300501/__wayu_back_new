from django.urls import path

from . import views

app_name = "news"


urlpatterns = [
    path("news/GetAllEventCategories/", views.EventCategoriesView.as_view(), name="event_category_list"),
    path("news/GetAllEvents/", views.EventsView.as_view(), name="events_list"),
    path("news/GetDetailEvent/<slug:slug>/", views.EventsDetailView.as_view(), name="events_detail"),
    path("news/GetAllNewsCategories/", views.NewsCategoryListView.as_view(), name="news_categories_list"),
    path("news/GetAllNewsTags/", views.NewsTagView.as_view(), name="news_tags_list"),
    path("news/GetAllCountryNews/", views.CountryNewsView.as_view()),
    path("news/GetAllNews/", views.NewsView.as_view(), name="news_list"),
    path("news/GetDetailNews/<slug:slug>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("news/GetDetailNews/<slug:slug>/reletions/", views.NewsRecView.as_view()),
]
