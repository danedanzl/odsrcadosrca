from django import forms
from django.urls import path, reverse
from django.shortcuts import render, redirect

class Task:
    def __init__(self, name, display_name, form=None):
        self.name = name
        self.display_name = display_name
        if form is None:
            def f(r):
                raise NotImplementedError("TODO")
            self.task_view = f
        else:
            self.form = form

    def info_view(self, request):
        return render(request, self.template(self.info_viewname), { 'task': self })

    def task_view(self, request):
        if request.method == 'POST':
            form = self.form(request.POST)
            if form.is_valid():
                return render(request, self.template(self.sol_viewname),
                              form.correct() | { 'task' : self })
        else:
            form = self.form()

        return render(request, self.template(self.task_viewname),
                      { 'task': self, 'form': form })

    @staticmethod
    def template(viewname):
        return f"naloge/{viewname}.html"

    @property
    def info_viewname(self):
        return f"{self.name}_text"
    @property
    def task_viewname(self):
        return f"{self.name}_task"
    @property
    def sol_viewname(self):
        return f"{self.name}_sol"

    def urlpatterns(self):
        def hsh(s):
            return str(sum(ord(c)*17**i for i,c in enumerate(s)))[-3:]
        def url(viewname):
            return f"{hsh(viewname)}_{viewname}"
        return [
                path(url(self.info_viewname), self.info_view, name=self.info_viewname),
                path(url(self.task_viewname), self.task_view, name=self.task_viewname),
        ]
