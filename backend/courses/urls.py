from django.urls import path
from .views import *


urlpatterns = [
    path("create-course/", CreateCourseView.as_view(), name="create-course"),
    path("list-course/", ListCourseView.as_view(), name="list-course"),
    path("update-course/<int:pk>/", UpdateCourseView.as_view(), name="update-course"),
    path("delete-course/<int:pk>/", DeleteCourseView.as_view(), name="delete-course"),
    path("create-session/", CreateSessionView.as_view(), name="create-session"),
    path("list-session/<int:course_id>/", ListSessionView.as_view(), name="list-session"),
    path("session-detail/<int:pk>/", SessionDetailView.as_view(), name="session-detail"),
]

