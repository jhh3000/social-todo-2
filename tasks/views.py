from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Task

# Create your views here.

def dashboard(request):
	template = 'dashboard.html'
	task_list = Task.objects.filter(
		Q(user=request.user) |
		Q(collaborator1=request.user) |
		Q(collaborator2=request.user) |
		Q(collaborator3=request.user)
	)
	for task in task_list:
		if task.user == request.user:
			task.can_delete = True
	context = {
		'name': request.user.first_name.split(" ")[0],
		'task_list': task_list,
	}
	return render(request, template, context)

def create(request):
	if request.method == 'POST':
		print request.POST
		title = request.POST['title']
		description = request.POST['description']
		collaborator1 = User.objects.filter(username=request.POST['collaborator1']).first()
		collaborator2 = User.objects.filter(username=request.POST['collaborator2']).first()
		collaborator3 = User.objects.filter(username=request.POST['collaborator3']).first()
		Task.objects.create(
			user=request.user,
			title=title,
			description=description,
			collaborator1=collaborator1,
			collaborator2=collaborator2,
			collaborator3=collaborator3,
		)
	return redirect(reverse('dashboard'))

def delete(request, task_id):
	task = Task.objects.get(pk=task_id)
	task.delete()
	return redirect(reverse('dashboard'))

def toggle(request, task_id):
	task = Task.objects.get(pk=task_id)
	task.complete = not task.complete
	task.save()
	return redirect(reverse('dashboard'))
