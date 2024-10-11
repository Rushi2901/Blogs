from django.shortcuts import render,redirect , get_object_or_404
from .models import *
from django.contrib import messages
import random
# Create your views here.


def home (request):
    allpost = Post.objects.all()
    recentPost = Post.objects.all()[::-1]
    css_classes = [
    'text-primary',
    'text-success',
    'text-warning'
    ]

    random_choice = random.choice(css_classes)
    
    data = request.GET.get('category')
    if data != None :
            cat_data = Post.objects.filter(category=data)
            print(cat_data)
            context ={
               'cat_data':cat_data
            }

            return render (request,'blog/category.html',context)

    context = {
        'post':allpost,'recentPost':recentPost,
        'rand_choice': random_choice
    }

    return render (request,'blog/index.html',context)




def category (request):

    return render (request,'blog/category.html',{})


def page (request ,sno,slug):
    post = get_object_or_404(Post,sno=sno,slug=slug)
    recentPost = Post.objects.all()[::-1]
    comment_data = Comment.objects.filter(post=post)

    if request.method == "POST":
        
        name=request.POST['name']
        email=request.POST['email']
        postsno=request.POST.get('postsno')
        website=request.POST['website']
        message = request.POST['message']

        post_data = Post.objects.filter(sno=postsno)[0]
        comment = Comment(
            name=name,
            email=email,
            post=post_data,
            website=website,
            message=message
        )
        comment.save()
        messages.success(request,"Comment Sucessfully Submit")

        

    return render (request,'blog/page.html',{'post':post , 'recentPost':recentPost , 'comment_data':comment_data})



def contact (request):


    if request.method == 'POST':
        firstname= request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        subject=request.POST['subject']
        message= request.POST['message']
        
        contact = Contact(first_name= firstname ,last_name=lastname,email=email,subject=subject,message=message)
        contact.save()
        messages.success(request,'Successfully Form Submitted!')
        return redirect('/contact')
          
    return render (request,'blog/contact.html',{})


def blog (request):
    recentPost = Post.objects.all()[::-1]

    css_classes = [
    'text-primary',
    'text-success',
    'text-warning'
    ]

    random_choice = random.choice(css_classes)
    return render(request,'blog/blog.html',{'recentPost':recentPost,'rand_choice': random_choice})


def comment (request):
    if request.method == "POST":
        
        name=request.POST['name']
        email=request.POST['email']
        post=request.POST.get('postsno')
        website=request.POST['website']
        message = request.POST['message']

