from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Student
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Here you would typically authenticate the user
        # For simplicity, we are just returning a success message
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.info(f"Attempting registration for username:{username}")
            return redirect('home')
        else:
            messages.error(request,'username and password not matched')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.Please try again')
                return render(request, 'register.html')

            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.Please try again')
                return render(request, 'register.html')

            # Create user
            CustomUser.objects.create(
                username=username,
                email=email,
                password=make_password(password1),
                role='sales'
            )
            messages.success(request, 'User registered successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html')

"""
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # Here you would typically create a new user
        # For simplicity, we are just returning a success message
        if password1==password2:
            
            if CustomUser.objects.filter(username=username).exists():
                #messages.error(request, 'Email already exists.')
                return render(request, 'register.html')
            else:
                user=CustomUser.objects.create(username=username,
                                                email=email,
                                                password=make_password(password1),
                                                role='sales')
            return redirect('login')
        else:
            messages.error(request,'password not matched')
    return render(request, 'register.html')
"""
def logout(request):
    #request('logout')
    return redirect('login')

def employee_list(request):
    employees=CustomUser.objects.all().values()
    return render(request, 'employee_list.html',{'employees':employees})

def student_list(request):
    #student_data=Student.objects.all().values()
    user=request.user
    if user.role=='admin':
        student_data=Student.objects.select_related('added_by').all()
    else:
        student_data=Student.objects.select_related('added_by').filter(added_by=user)
    return render(request, 'student_list.html',{'studentdata':student_data})

"""
def add_new_student(request):
    if request.method=="POST":
        if request.user.role=='admin':
            added_by_id = request.POST.get('added_by')
            added_by= CustomUser.objects.get(id=added_by_id)
        else:
            added_by = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        place = request.POST.get('place')
        gender = request.POST.get('gender')
        skills_list = request.POST.getlist('skillset')
        skills = ', '.join(skills_list)
        state = request.POST.get('state')
        Student.objects.create(
            added_by=added_by,
            name=name,
            email=email,
            age=age,
            place=place,
            gender=gender,
            skills=skills,
            state=state
        )
        return redirect("student_list")
        
    users=CustomUser.objects.all() if request.user.role=='admin' else [request.user]
    return render(request, 'add_new_student.html',{"users":users})"""


def add_new_student(request):
    if request.method == "POST":
        # Get added_by depending on user role
        if request.user.role == 'admin':
            added_by_id = request.POST.get('added_by')
            added_by = CustomUser.objects.get(id=added_by_id)
        else:
            added_by = request.user

        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        place = request.POST.get('place')
        gender = request.POST.get('gender')
        skills_list = request.POST.getlist('skillset')
        skills = ', '.join(skills_list)
        state = request.POST.get('state')

        # Check for duplicate email
        if Student.objects.filter(email=email).exists():
            messages.error(request, "A student with this email already exists.")
            users = CustomUser.objects.all() if request.user.role == 'admin' else [request.user]
            return render(request, 'add_new_student.html', {"users": users})

        # Save the new student
        Student.objects.create(
            added_by=added_by,
            name=name,
            email=email,
            age=age,
            place=place,
            gender=gender,
            skills=skills,
            state=state
        )
        messages.success(request, "Student added successfully.")
        return redirect("student_list")

    users = CustomUser.objects.all() if request.user.role == 'admin' else [request.user]
    return render(request, 'add_new_student.html', {"users": users})
"""
@login_required
def update_student(request, id):
    student=get_object_or_404(Student, id=id)
    users=CustomUser.objects.all() 
    if request.method=='POST':
        email = request.POST.get('email')
        if Student.objects.exclude(id=id).filter(email=email).exists():
            skills=student.skills.split(',') if student.skills else []  
            return render(request, 'add_new_student.html',{"users":users, "student": student, "skills":skills})
        student.name = request.POST.get('name')
        student.email = email
        student.age = request.POST.get('age')
        student.place = request.POST.get('place')
        student.gender = request.POST.get('gender')
        skills_list = request.POST.getlist('skillset')
        student.skills = ', '.join(skills_list)
        student.state = request.POST.get('state')
        added_by_id = request.POST.get('added_by')
        student.added_by= CustomUser.objects.get(id=added_by_id)
        student.save()
        return redirect("student_list")
    skills=student.skills.split(',') if student.skills else []  
    return render(request, 'add_new_student.html',{"users":users, "student": student, "skills":skills})"""

@login_required
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    users = CustomUser.objects.all() 
    if request.method == 'POST':
        email = request.POST.get('email')
        if Student.objects.exclude(id=id).filter(email=email).exists():
            skills = [s.strip() for s in student.skills.split(',')] if student.skills else []
            return render(request, 'add_new_student.html', {
                "users": users,
                "student": student,
                "skills": skills,
                "error": "Email already exists."
            })
        student.name = request.POST.get('name')
        student.email = email
        student.age = request.POST.get('age')
        student.place = request.POST.get('place')
        student.gender = request.POST.get('gender')
        skills_list = request.POST.getlist('skillset')
        student.skills = ', '.join(skills_list)
        student.state = request.POST.get('state')
        added_by_id = request.POST.get('added_by')
        student.added_by = CustomUser.objects.get(id=added_by_id)
        student.save()
        return redirect("student_list")
    
    skills = [s.strip() for s in student.skills.split(',')] if student.skills else []
    return render(request, 'add_new_student.html', {
        "users": users,
        "student": student,
        "skills": skills
    })

        
def delete_student(request, id):
    student_data = Student.objects.get(id=id)
    student_data.delete()
    return redirect("student_list")