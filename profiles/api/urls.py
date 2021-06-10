from django.urls import include, path
from profiles.api.views import ProfileViewSet, ProfileStatusViewset
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('profiles/', ProfileList.as_view(), name="profile-list"),
# ]

# profile_list = ProfileViewSet.as_view({'get': 'list'})
# profilr_detail = ProfileViewSet.as_view({'get': 'retrieve'})

# urlpatterns = [
#     path('profiles/', profile_list, name="profile-list"),
#     path('profiles/<int:pk>/', profilr_detail, name="profile-details"),
# ]

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
# router.register(r"status", ProfileStatusViewset)
router.register(r"status", ProfileStatusViewset, basename="status")
urlpatterns = [
    path("", include(router.urls))
]

