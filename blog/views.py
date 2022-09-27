from django.shortcuts import render

# Create your views here.
def blog_view(req):
    return render(req, 'blog/blog-home.html')


def blog_single(req):
    return render(req, 'blog/blog-single.html')
