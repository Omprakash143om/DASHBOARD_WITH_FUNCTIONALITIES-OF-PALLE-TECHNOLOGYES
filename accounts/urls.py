from django.urls import path
from accounts import views
urlpatterns = [
    path('',views.home,name='home'),  # Home page
    path('login/', views.user_login, name='login'),  # Login page
    path('register/', views.register, name='register'),  # Registration page
    path('logout/', views.logout, name='logout'),  # Logout page (handled by the same view for simplicity)
    path('employee_list/', views.employee_list, name='employee_list'),
    path('student_list/', views.student_list, name='student_list'),
    path('add_new_student/', views.add_new_student, name='add_new_student'),
    path('update/<int:id>', views.update_student, name='update'),
    path('delete/<int:id>', views.delete_student, name='delete'),

]