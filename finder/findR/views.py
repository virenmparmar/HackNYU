from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .models import ItemListings, User
# Create your views here.

from django.contrib.auth.hashers import make_password

def index(request):
    return render(request, "base.html")


def register(request):
    if(request.method == "POST"):
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],
            email=request.POST["email"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
        )
        return render(request, "login.html")
    else:
        return render(request, "register.html")

def login(request):
    if(request.method == "POST"):
        print(request.POST)
        try:
            user = User.objects.get(username=request.POST["username"])
            print("hashed password is: ", make_password(request.POST["password"]))
            print("password stored is: ", user.password)
            if(user.check_password(make_password(request.POST["password"]))):
                user.is_authenticated = True
                return render(request, "add_listing.html")
            else:
                message = "Invalid password"
                return render(request, "login.html", {"message": message})
        except:
            message = "Username doesn't exist"
            return render(request, "login.html", {"message": message})
    elif(request.method == "GET"):
        return render(request, "login.html")

def add_listing(request):
    if (request.method == "POST" and request.FILES['post-photos']):
        user = User.objects.get(username=request.user) 
        upload = request.FILES['post-photos']       # Image object that was uploaded through the form
        fss = FileSystemStorage()                   # File System Storage object
        file = fss.save(upload.name, upload)        # Saving the image object using File System Storage object method
        file_url = fss.url(file)                    # Finding the image url in file system
        ItemListings.objects.create(
        user_id=user,
        photo_path=file_url,
        image=upload,
        longitutude=request.POST["post-longitude"],
        latitude=request.POST["post-latitude"],
        status='A',
        rating=0,
        )
        message = "Listing added"
        return render(request, "add_listing.html", {"message": message, "file_url": file_url})
    message = "Invalid username"
    return render(request, "add_listing.html")
        

def browse(request):
    if(request.method == "POST"):
        try:
            ItemListings.objects.create(
            user_id=User.objects.get(username=request.POST["username"]),
            photo_path=request.POST["photo_path"],
            longitutude=request.POST["longitude"],
            latitude=request.POST["latitude"],
            status=request.POST["status"],
            rating=request.POST["rating"],
            )
            message = "Listing added"
            return render(request, "login.html", {"message": message})
        except:
            message = "Invalid username"
            
    else:
        return render(request, "browse.html")
        
