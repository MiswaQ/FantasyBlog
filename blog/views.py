from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, EditComments
from .forms import CommentForm

# Defines view functions for handling HTTP requests related to blog posts and comments.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True 

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True 

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class EditComments(View):
    template_name = 'edit_comment.html'

    def get(self, request, pk, *args, **kwargs):
        edit_comment = get_object_or_404(Comment, id=pk)
        edit_comments_form = CommentForm(instance=edit_comment)
        return render(
            request,
            self.template_name,
            {'edit_comment': edit_comment, 'edit_comments_form': edit_comments_form},
        )
    
    def post(self, request, pk, *args, **kwargs):
        edit_comment = get_object_or_404(Comment, id=pk)
        edit_comments_form = CommentForm(data=request.POST, instance=edit_comment)
        if edit_comments_form.is_valid():
            edit_comments_form.save()
            return redirect(reverse('post_detail', args=[str(edit_comment.post.slug)]))
        return render(
            request,
            self.template_name,
            {'edit_comment': edit_comment, 'edit_comments_form': edit_comments_form},
        )
            

def delete(request, id):
    slug = request.POST.get('slug', '')
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect(reverse('post_detail', args=[slug]))