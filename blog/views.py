from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post



#handel logic route
#use how we want to do when user
#map the url
def home(request):
	#return HttpResponse('<h1>Blog Home</h1>')

	
	
	context = {
		'posts': Post.objects.all(),
		
	}

	

	#render still return httpreq
	return render(request,'blog/home.html', context)


def latest_post(request):

    latest_post = Post.objects.order_by('-date_posted')[0]
    
    context = {

        'latest_post': latest_post
    }

    return render(request, 'blog/latest_post.html', context)


class PostListView(ListView):

	#tell view to query model data

	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts' #if you want to acces in code block in html, here us the 
	#post object you define 
	#context variable name that will be used to contain 
	#the list of data that this view is manipulating

	ordering = ['-date_posted']

	#You get 2 posts per page
	paginate_by = 5


#Only list the posts by same user
class UserPostListView(ListView):

	#tell view to query model data

	model = Post
	template_name = 'blog/user_post.html'
	context_object_name = 'posts' 
	#context variable name that will be used to contain 
	#the list of data that this view is manipulating

	ordering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')





class PostDetailView(DetailView):

	#by default the generic class view are looking for 
	#nameing convention <app>/<model>_<viewtype>.html
	#in this case is blog/post_detailview
	#create a templeta file, no need to specify as postlist view to 'blog/home.html'
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):

	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	
	#To test if current user is the post author
	def test_func(self):
		post = self.get_object()
		
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		
		if self.request.user == post.author:
			return True
		return False






def about(request):
	#return HttpResponse('<h1>Blog About</h>')
	return render(request,'blog/about.html')















# #fake post to see how to pass to blog page
# posts = [

# 	{
# 		'author':'cs',
# 		'title':'post 1',
# 		'content': 'lodf fd fdeat',
# 		'date_posted':'May 17'

# 	},
# 	{
# 		'author':'cs2',
# 		'title':'post 2',
# 		'content': 'lo second ',
# 		'date_posted':'May 11'

# 	}

# ]
