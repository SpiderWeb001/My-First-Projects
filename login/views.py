from django.shortcuts import render
from login.models import Login
# Create your views here.
def loginpage(request):
    posts = Login.objects.all()
    return render(request , "logincode.html",{'posts':posts})

def login(request):
    return render(request,"login.html")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # return HttpResponse(post)
    return render(request, "page.html", {'post': post})


def post_create(request):
    form = PostForm()
    return render(request, "post_create.html", {'form': form})