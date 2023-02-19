from django.shortcuts import render

from .models import ItemListings, User
# Create your views here.

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
            if(user.check_password(request.POST["password"])):
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
            return render(request, "add_listing.html", {"message": message})
        
    else:
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
        
