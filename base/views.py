from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.http import Http404
from django.contrib import messages
# Create your views here.


class HomeView(View):
    def get(self,request):
        todos = self.get_all_todos()
        count = todos.count()
        context={
            'todos':todos,
            'count':count,
        }
        return render(request, "home.html",context)
    
    def get_all_todos(self):
        return Todo.objects.all().order_by('-id')
    

class DetailView(View):
    def get(self,request,pk):
        todo = self.get_todo(pk)
        related_todos = self.get_related_todo(todo.category)
        context={
            'todo':todo,
            'related_todos':related_todos,
        }
        return render(request, 'detail.html',context)


    def get_todo(self,pk):
        try:
            return Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get_related_todo(self,category):
        return Todo.objects.filter(category=category)

class CreateView(View):
    def get(self,request):
        categories = Category.objects.all()
        context={
            'categories':categories,
        }
        return render(request, 'create.html',context)

    def post(self,request):
        heading = request.POST.get('heading')
        body = request.POST.get('body')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        todo = Todo(heading=heading,body=body,category=category)

        todo.save()

        messages.success(request, 'Todo is created successfully.')

        # print(heading,body,category)

        return redirect('/')



class UpdateView(View):
    def get(self,request,pk):
        categories = Category.objects.all()
        todo = self.get_todo(pk)
        context={
            'categories':categories,
            'todo':todo,
        }
        return render(request, 'update.html',context)

    def get_todo(self,pk):
        try:
            return Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            raise Http404

    def post(self,request,pk):
        todo = self.get_todo(pk)
        heading = request.POST.get('heading')
        body = request.POST.get('body')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        todo.heading = heading
        todo.body =body
        todo.category = category


        todo.save()

        messages.success(request, 'Todo is updated successfully.')

        # print(heading,body,category)

        return redirect('/')


class DeleteView(View):

    def get(self,request,pk):
        todo = self.get_todo(pk)
        context={
            'todo':todo,
        }

        return render(request, 'delete.html',context)

    def post(self,request,pk):
        todo = self.get_todo(pk)

        todo.delete()

        messages.success(request, 'Todo is deleted....')

        return redirect('/')

    def get_todo(self,pk):
        try:
            return Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            raise Http404
