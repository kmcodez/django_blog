from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm


# static damo data
# posts = [
#     {'id': 1, 'title': 'Post 1', 'content': 'Content of Post 1', 'type': 'sports'},
#     {'id': 2, 'title': 'Post 2', 'content': 'Content of Post 2', 'type': 'entertainment'},
#     {'id': 3, 'title': 'Post 3', 'content': 'Content of Post 3', 'type': 'politics'},
#     {'id': 4, 'title': 'Post 4', 'content': 'Content of Post 4', 'type': 'space'},
# ]

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")


def detail(resquest):
    return HttpResponse("You are viewing post detail page")


def detail_int(request, post_id):
    return HttpResponse("You are viewing post detail <interger> page. And ID is %s" % post_id)


def detail_str(request, post_id):
    return HttpResponse("You are viewing post detail <string> page. And ID is %s" % post_id)


# redirect
def old_url_redirect(request):
    return redirect("new_url")


def new_url_view(request):
    return HttpResponse("Hello, world. You're at the new url view.")


# use with reverse to redirect
def redirect_old_url(request):
    return redirect(reverse('blog:new_page_url'))


def redirect_new_url(request):
    return HttpResponse("Hello, world. You're at the new url view.")


def front_index(request):
    blog_title = "Latest Posts"
    # getting data by model
    all_posts = Post.objects.all()

    # paginate
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'index.html', {'blog_title': blog_title, 'page_obj': page_object})


def front_detail(request, slug):
    # static data
    # post = next((item for item in posts if item['id'] == int(post_id)), None)

    try:
        # getting data by model from post ID
        post = Post.objects.get(slug=slug)

        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404('Post does not Exist!')

    # logger = logging.getLogger("Testing")
    # logger.debug(f'post variable is {post}')
    return render(request, 'detail.html', {'post': post, 'related_posts': related_posts})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("Testing")

        if form.is_valid():
            logger.debug(
                f"POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}"
            )
            success_message = 'Your Email has been sent successfully!'
            return render(request, 'contact.html', {'form': form, 'success_message': success_message})

        else:
            logger.debug('Form Validation Failure')
        return render(request, 'contact.html', {'form': form, 'name': name, 'email': email, 'message': message})

    return render(request, 'contact.html')


def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request, 'about.html', {'about_content': about_content})