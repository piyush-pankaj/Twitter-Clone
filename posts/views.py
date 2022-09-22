from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import post 
from .forms import PostForm

# Create your views here.
# def index(request):
#     img=Pictures.objects.all()
#     ctx= {'Pictures':img}
#     return render(request,'templates/posts.html',ctx)
def index(request): 
    # If the Method is post 
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        # if the form is valid
        if form.is_valid():
            # if yes, save
            form.save()

             # Redirect to Home
            return HttpResponseRedirect('/')

                
        else:
            # no, show error
            return HttpResponseRedirect(form.erros.as_json())

    # get all posts , limit=20
    posts=post.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request,'posts.html',
                    {'posts':posts})


def delete(request,post_id):
    # Find post
    Post=post.objects.get(id=post_id)
    Post.delete()
    return HttpResponseRedirect('/')

# def edit(request,post_id):
#     # Find post
#     if request.method =='POST':
#         Post=post.objects.get(id=post_id)
#         if Post.is_valid():

#             Post.edit()
#             return HttpResponseRedirect('/')
#         else:
#             return HttpResponseRedirect(Post.erros.as_json())


def edit(request, post_id):
    # if request.method == "GET":
    #     posts = post.objects.get(id=post_id)
    #     return render(request, "edit.html", {"posts": post})
    posts = post.objects.get(id=post_id)
    if request.method == "POST":
       
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")

    return render(request,'edit.html', {'posts': posts})




def likebtn(request,post_id):
   
    like = post.objects.get(id=post_id)
    like.likes += 1
    like.save()
    return HttpResponseRedirect('/')
