from django.urls import path

from apps.services.views import career, law, library, partner, volunteer

# library
urlpatterns = [
    path("services/GetAllCatalog/", library.LibraryCatalogView.as_view()),
    path("services/GetAllLibrary/", library.BookListView.as_view()),
    path("services/GetDetailLibrary/<slug:slug>/", library.BookDetailView.as_view()),
    path("services/GetDetailLibrary/<slug:slug>/recommend/", library.BookRecView.as_view()),
]

# volunteer
urlpatterns += [
    path("services/GetForVolunteer/", volunteer.ForVolunteerView.as_view()),
    path("services/PostVolunteerResume/", volunteer.VolunteerResumeCreateView.as_view()),
    path("services/GetAllVolunteer/", volunteer.VolunteerView.as_view()),
    path("services/GetAllCoordinator/", volunteer.CoordinatorView.as_view()),
    path("services/GetAllOpportunity/", volunteer.OpportunityView.as_view()),
]

# law
urlpatterns += [
    path("services/GetAllMigrationLaw/", law.MigrationLawView.as_view()),
    path("services/GetAllInsurance/", law.InsuranceView.as_view()),
    path("services/GetObligations/", law.ObligationsView.as_view()),
    path("services/GetAllCountryLaw/", law.CountryLawView.as_view()),
    path("services/GetDetailCountryLaw/<int:id>/", law.CountryLawDetailView.as_view()),
]

# career
urlpatterns += [
    path("services/GetCareerAbout/", career.CareerAboutView.as_view()),
    path("services/GetAllYoungInnovator/", career.YoungInnovatorView.as_view()),
    path("services/GetAllPhotoGallery/", career.PhotoGalleryView.as_view()),
    path("services/GetAllPhotoGalleryCompatriots/", career.PhotoGalleryCompatriotsView.as_view()),
    path("services/GetGratuitousHelp/", career.GratuitousHelpView.as_view()),
    path("services/GetAllServiceCategory/", career.ServiceCategoryView.as_view()),
    path("services/GetYoungCompatriots/", career.YoungCompatriotsView.as_view()),
    path("services/GetGoogleForm/", career.GoogleFormView.as_view()),
]

# partner
urlpatterns += [
    path("services/GetLegalLabAbout/", partner.LegalLabAboutView.as_view()),
    path("services/GetAllSupport/", partner.SupportView.as_view()),
    path("services/GetAllOrganizationCategory/", partner.OrganizationCategoryView.as_view()),
    path("services/GetAllEmbassy/", partner.EmbassyView.as_view()),
    path("services/GetDetailEmbassy/<slug:slug>/", partner.EmbassyDetailView.as_view()),
    path("services/GetAllPartnerCategory/", partner.PartnerCategoryView.as_view()),
    path("services/GetAllPartnership/", partner.PartnershipPartnershipView.as_view()),
    path("services/GetAllPartnerOrganization/", partner.PartnerOrganizationView.as_view()),
]
