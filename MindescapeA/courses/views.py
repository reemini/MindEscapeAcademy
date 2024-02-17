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


def generated_course(request):
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
        
        # Create a new course instance and save it by AI
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
    
    return render(request, 'generated_course.html')


from django.http import JsonResponse
import requests

def generate_description(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        # Call OpenAI API to generate the description
        response = requests.post(
            'https://api.openai.com/v1/engines/davinci/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer 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'
            },
            json={
                'prompt': f'Generate a course description for a course titled "{title}".',
                'max_tokens': 150
            }
        )

        # Extract the generated description from the response
        description = response.json()['choices'][0]['text'].strip()

        # Return the generated description as JSON response
        return JsonResponse({'description': description})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
