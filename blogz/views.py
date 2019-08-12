from .forms import EmailPostForm, CommentForm
from .models import Post
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blogz/post/list.html'


def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  'blogz/post/comment.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = 'https://wordpress.com/view/techstudents1.wordpress.com'
            subject = ' {} {} recommends you reading " {} "'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm
    return render(request, 'blogz/post/share.html', {'post': post,
                                                     'form': form,
                                                     'sent': sent})


class form_add_post(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('',)


def add_post(request):
    if request.POST:
        form = form_add_post(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('post_list'))
        else:
            return render(request, 'blogz/post/add_post.html',
                          {'form': form})
    else:
        form = form_add_post
        return render(request, 'blogz/post/add_post.html' ,
                      {'form': form})