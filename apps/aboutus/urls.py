from django.urls import path

from apps.aboutus import views

urlpatterns = [
    path("about/GetSingleHeader/", views.HeaderView.as_view()),
    path("about/GetSingleWhatWeDo/", views.WhatWeDoView.as_view()),
    path("about/GetFooterWhatWeDo/", views.WhatWeDoFooterView.as_view()),
    path("about/GetAllAboutCenterHistory/", views.AboutCenterHistoryView.as_view()),
    path("about/GetAllAboutCenterGoal/", views.AboutCenterGoalView.as_view()),
    path("about/GetAllStatistic/", views.StatisticView.as_view()),
    path("about/GetSingleManager/", views.ManagementSingleView.as_view()),
    path("about/GetAllManagement/", views.ManagementView.as_view()),
    path("about/GetAllRepresentative/", views.RepresentativeView.as_view()),
    path("about/GetDetailRepresentative/<slug:slug>/", views.RepresentativeDetailView.as_view()),
    path("about/GetAllVacancy/", views.VacancyAllView.as_view()),
    path("about/GetSingleVacancy/<slug:slug>/", views.VacancySingleView.as_view()),
    path("about/PostResumeApplication/<slug:slug>/", views.ResumeApplicationView.as_view()),
    path("about/PostResume/", views.ResumeCreateView.as_view(), name="resume-application"),
    path("about/GetStatusStatistic/", views.StatusStatisticView.as_view()),
]
