# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Course



# def educator_courses(request):
#     if request.method == 'POST':
#         # Process the form submission to create a new course
#         title = request.POST.get('title')
#         # Get other form data...
#         new_course = Course.objects.create(title=title, description=description, difficulty=difficulty_level)
#         # Redirect to home page after course creation
#         return redirect('home')
#     return render(request, 'educator_courses.html')

# def home(request):
#     latest_courses = Course.objects.order_by('-id')[:3]  # Retrieve latest 3 courses
#     return render(request, 'home.html', {'latest_courses': latest_courses})

# def course_detail(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     return render(request, 'course_detail.html', {'course': course})

##اخر كود اشتغل فيه الصور
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course

def educator_courses(request):
    if request.method == 'POST':
        print("Form submitted")
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        
        # Process the form submission to create a new course
        title = request.POST.get('title')
        description = request.POST.get('description')
        difficulty_level = request.POST.get('difficulty')
        picture = request.FILES.get('picture')  # Get the uploaded picture file
        materials = request.FILES.getlist('material')  # Get the list of uploaded material files
        
        print("Title:", title)
        print("Description:", description)
        print("Difficulty:", difficulty_level)
        print("Picture:", picture)
        print("Materials:", materials)
        
        # Create a new course instance and save it
        new_course = Course.objects.create(
            title=title,
            description=description,
            difficulty=difficulty_level,
            picture=picture,  # Assign the picture file to the 'picture' field
        )
        
        # Save each material file
        for material in materials:
            new_course.files.create(file=material)
        
        # Redirect to home page after course creation
        return redirect('home')
    
    return render(request, 'educator_courses.html')


def home(request):
    latest_courses = Course.objects.order_by('-id')
    return render(request, 'home.html', {'latest_courses': latest_courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_detail.html', {'course': course})
