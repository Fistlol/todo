from django.urls import include, path
from .views import TodoListViewSet,TodoListViewSetById,ListViewSet,ListByIdViewSet,TodosByTodoList
# from .views import ToDoListViewSet, ToDoListTasksViewSet, CompletedToDoListViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('todo_list/',TodoListViewSet.as_view({'get':'list','post':'create'})),
    path('todo_list/<int:pk>/',TodoListViewSetById.as_view({'get':'todo_list_by_id','put':'update'})),
    path('todos/', ListViewSet.as_view({'get': 'list','post': 'create'})),
    path('todos/<int:pk>/', ListByIdViewSet.as_view({'get': 'retrieve','put': 'update'})),
    path('todo_list/<int:pk>/todos/',TodosByTodoList.as_view({'get':'tasks_by_list'}))
    # path('todos/',ToDoListViewSet.as_view({'get': 'list'})),
    # path('todos/<int:pk>/', ToDoListTasksViewSet.as_view({'get': 'tasks_by_list'})),
    # path('todos/<int:pk>/completed/', CompletedToDoListViewSet.as_view({'get': 'completed_tasks'})),
]