from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Post,Category,Comment,Contactinfo
from .forms import PostForm
# Create your views here.

def Home(request):
    featured = Post.objects.order_by('-id').filter(section='Featured')[0:4]
    main_post = Post.objects.order_by('-id').filter(main_post=True)[0:1]
    latest_post = Post.objects.order_by('-id').filter(section='Latest')
    cat = Category.objects.all()
    Trending = Post.objects.order_by('-id').filter(section='Trending')[:6]
    popular = Post.objects.order_by('-id').filter(section='popular')[:6]
    Most_viewed = Post.objects.order_by('-id').filter(section='Most_viewed')
    life_style= Post.objects.order_by('-id').filter(section='life_style')[:2]
    top= Post.objects.order_by('-id').filter(section='top')[:1]
    new =  Most_viewed = Post.objects.order_by('-id').filter(section='new')[:1]
    
    # comment = Comment.objects.filter(blog_id=post.id).order_by('-date')
    
    
    context ={
        'featured':featured,
        'main_post':main_post,
        'latest':latest_post,
        'cat':cat,
        'most_viewed':Most_viewed,
        'Trending':Trending,
        'life_style':life_style,
        'popular':popular,
        'top':top,
        'new':new
        # 'comment':comment,
        
    }
    return render(request, 'core/index.html',context)

def PostDetails(request,slug):
    category = Category.objects.all()
    post = get_object_or_404(Post,blog_slug = slug)
    comment = Comment.objects.filter(blog_id=post.id).order_by('-date')
    
    context ={
        'post':post,
        'category':category,
        'comment':comment
    }
    return render(request, 'core/detail-page.html', context)

def category(request, slug):
    cat = Category.objects.all()
    blog_cat = Category.objects.filter(slug=slug)
    context={
        'cat':cat,
        'active_cat':slug,
        'blog_cat':blog_cat,
        
    }
    return render(request, 'core/category.html')


def Add_comment(request, slug):
    if request.method == 'POST':
        post= get_object_or_404(Post, blog_slug=slug)
        comment = request.POST.get('comment')
        name = request.POST.get('name')
        email = request.POST.get('email')
      
        parent = request.POST.get('parent')
        
        parent_comment = True
        
        if parent:
            parent_comment = get_object_or_404(Comment, id= parent)
       
        Comment.objects.create(
            post=post,
            comment=comment,
            name= name,
            email=email,
            parent=parent 
        ) 
        return redirect('post-details', slug = post.blog_slug)
    return render(request, 'core/detail-page.html')
    
    

@login_required
def createPost(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            
            return redirect('home')
        else:
            print(form.has_error)
        
    else:
        form = PostForm()
    context = {
        'form':form
    }
    return render(request, 'core/create.html', context)


def Contact(request):
    contact = Contactinfo.objects.order_by('-id')[0:1]
    context ={
        'contact':contact
    }
    
    return render(request, 'core/contact.html',context)

def handler404(request,exception):
    return render(request,'core/404.html', status=404)
