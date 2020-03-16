from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.models import User
from .models import Post
from comment.models import Comment
from django.views import View

# Create your views here.

class HomeView(View):
	#default
	type = "confession"
	template = 'post/home.html'
	title = "Confessions"
	createbutton = "Create a confession"
	def get(self, request):
		base = self.title[:len(self.title)-1]
		base = base.lower()
		createaddress = "create" + base
		detailaddress = "detail" + base
		queryset = Post.objects.filter(type=self.type).order_by('-pub_date')
		context = {"object_set": queryset, "title":self.title, "createaddress":createaddress, "createbutton":self.createbutton, "detailaddress":detailaddress}
		return render(request, self.template, context)

class CreateView(View):

	template = 'post/create.html'
	type = 'confession'
	selfurl = 'createconfession'
	title = 'Nothing to conceal, create a confession now!'
	subtitle = 'Let your voice be heard!'
	redirecturl = 'detailconfession'
	context = {}

	def init(self):
		default = ""
		if self.type=='event':
			default = """**Event start date**:

**Event end date**:

##Event description:
"""
		self.context = {"selfurl":self.selfurl, "title":self.title, "subtitle":self.subtitle, "default":default}
		if self.type == 'confession': 
			self.context['anonymous'] = True

	def get(self, request):
		self.init()
		return render(request, self.template, self.context)

	def post(self, request):
		if request.POST['title'] and request.POST['body']:
			instance = Post()
			instance.type = self.type
			instance.title = request.POST['title']
			instance.body = request.POST['body']
			instance.pub_date = timezone.datetime.now()
			try:
				if request.POST['anonymous']:
					instance.author = User.objects.get(pk=1)
			except:
				instance.author = request.user
			instance.save()
			return redirect(self.redirecturl, instance.pk) #NOT DONE YET
		else:
			self.init()
			return render(request, self.template, self.context)

class DetailView(View):
	type = 'confession'
	template = 'post/details.html'
	selfurl = 'detailconfession'
	context = {}

	def init(self, id):
		try:
			global instance
			instance = Post.objects.get(pk=id)
		except Post.DoesNotExist:
			return redirect('home') #NOT DONE YET
		comments = instance.comments.all()
		self.context = {'instance': instance, 'comments': comments, 'selfurl': self.selfurl}

	def get(self, request, id):
		self.init(id)
		return render(request, self.template, self.context)

	def post(self, request, id):
		self.init(id)
		newcomment = Comment()
		newcomment.text = request.POST['text']
		newcomment.pub_date = timezone.datetime.now()
		newcomment.author = request.user
		newcomment.save()
		instance.comments.add(newcomment)
		return redirect(self.selfurl, instance.pk)
