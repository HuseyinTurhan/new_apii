from django.urls import path
from .views import UsersListView, StudentList, UsersList, StudentDetail, UsersDetail

urlpatterns = [
    path("",UsersListView.as_view(), name="userlist"),
    path("students", StudentList.as_view(), name="studentapi"),
    path("users", UsersList.as_view(), name="usersapi"),
    path("students/<int:pk>",StudentDetail.as_view(), name="studentdetail"),
    path("users/<int:pk>", UsersDetail.as_view(), name="usersdetail")
    ]