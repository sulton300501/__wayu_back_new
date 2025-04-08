from django.urls import path

from . import views

urlpatterns = [
    path("project/GetAllProjects/", views.ProjectListView.as_view(), name="projects_list"),
    path("project/GetProject/<slug:slug>/", views.ProjectView.as_view()),
    # path("GetIntroduction/<slug:slug>/", views.IntroductionView.as_view(), name="introduction"),
    # path("GetAboutProject/<slug:slug>/", views.AboutProjectView.as_view()),
    # path("GetAllGoalAndMission/", views.GoalAndMissionView.as_view(), name="goals_missions"),
    # path("GetAllDocument/", views.DocumentView.as_view()),
    # path("GetProjectDocument/<slug:slug>/", views.ProjectDocumentView.as_view(), name="project_document"),
    # path("GetAllTeamMembers/", views.TeamMemberView.as_view(), name="team_members"),
    path("project/PostFeedbackProject/", views.FeedbackProjectView.as_view(), name="feedback_create"),
]
