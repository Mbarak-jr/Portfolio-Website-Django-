from django.shortcuts import render, HttpResponse
from home.models import Contact

def home(request):
    context = {
        "name": "Mbarak",
        "course": "Django"
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        # Ensure all fields are provided
        if name and email and phone and desc:
            ins = Contact(name=name, email=email, phone=phone, desc=desc)
            ins.save()
            print("The data has been written to the db")
            return HttpResponse("Form submitted successfully.")
        else:
            return HttpResponse("Please fill in all required fields.")

    # Render the form for a GET request
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')
