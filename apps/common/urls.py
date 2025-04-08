from django.urls import path
from apps.common import views


urlpatterns = [
    path("common/GetAllFaq/" , views.FAQView.as_view() , name="faq"),
    path("common/GetAllFaqTags/", views.FAQTagView.as_view(), name="faq-tags"),
    path("common/PostApplication/", views.ApplicationView.as_view(), name="send-application"),
    path("common/GetContact/", views.ContactView.as_view(), name="contact"),
    path("common/PostFeedback/", views.FeedbackView.as_view(), name="post-feedback"),
    path("common/GetContactUser/", views.ContactUserView.as_view(), name="contact-user"),
   # path("common/GlobalSearch/", views.GlobalSearchView.as_view()),
    path("common/GetAllCountries/", views.CountryView.as_view(), name="country"),
    path("common/GetAllPages/", views.PagesListView.as_view()),
    path("common/GetDetailPage/<slug:slug>/", views.PagesDetailView.as_view()),
]
