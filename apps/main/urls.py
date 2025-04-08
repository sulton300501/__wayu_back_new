from django.urls import path

from . import views

urlpatterns = [
    # path("mainpage/GetSlider/", views.SliderView.as_view()),
    path("mainpage/GetPayStatistic/", views.PayStatisticView.as_view()),
    path("mainpage/GetAllBannerMenu/", views.BannerMenuView.as_view()),
    path("mainpage/GetAllHeaderMenu/", views.HeaderMenuListView.as_view()),
    path("mainpage/GetAllUsefulLink/", views.UsefulLinkView.as_view()),
    path("mainpage/GetQuote/", views.QuoteView.as_view()),
    path("mainpage/GetCharityProject/", views.CharityProjectView.as_view()),
    path("mainpage/PostNewsletterEmail/", views.NewsletterEmailView.as_view()),
    path("mainpage/InstagramPhotos/", views.InstagramPhotoListView.as_view()),
 #   path("mainpage/GetDonationAmount/", views.DonationAmount.as_view()),
    # path("GetDonationStatistics/", views.DonationStatistics.as_view()),
    path("mainpage/GetAllStatistics/", views.MusofirDonationView.as_view()),
    path("mainpage/GetDownloadMusofirFile/<int:pk>/", views.MusofirDonationFileDownloadView.as_view()),
]
