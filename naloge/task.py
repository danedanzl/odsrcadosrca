from django.urls import path, reverse
from django.shortcuts import render

class Task:
    def __init__(self, name, display_name):
        self.name = name
        self.display_name = display_name
        self.task_view = lambda r: render(r, "naloge/task_tmplt.html", { 'task': self })
        def sol_view(r):
            raise NotImplementedError("TODO")
        self.sol_view = sol_view
        def info_view(request):
            return render(request, self.template(self.info_viewname), { 'task': self })
        self.info_view = info_view

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
                path(url(self.sol_viewname), self.sol_view, name=self.sol_viewname),
        ]
