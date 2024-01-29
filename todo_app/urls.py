from django.urls import path
from . import views


urlpatterns = [

    # Add task 
    path('addTask/', views.AddTask.as_view(), name='addTask'),
    
    # Mark as done
    path('mark_as_done/<int:pk>', views.Mark_as_done.as_view(), name='mark_as_done'),
    
    # mark as undone
    path('mark_as_undone/<int:pk>', views.Mark_as_undone.as_view(), name='mark_as_undone'),

    # EDIT Feature 
    path('edit_task/<int:pk>', views.Edit_task.as_view(), name='edit_task'),

    # DELETE Feature 
    path('delete_task/<int:pk>', views.Delete_task.as_view(), name='delete_task'),
]
