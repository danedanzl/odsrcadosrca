from django.db import models
from django.shortcuts import render

class Task(models.Model):

    name = models.CharField(max_length = 100)
    display_name = models.CharField(max_length = 100)
    max_points = models.IntegerField()
    category = models.CharField(max_length=3,
                                choices=[("nnz", "Nič ne znam"), ("obv", "obvladam")])

    def __str__(self):
        return f"{self.category} | {self.display_name} | {self.max_points}"

    @property
    def fullname(self):
        return f"{self.category}_{self.name}"

class MchoiceTask(Task):

    def form(self):
        from django import forms

        form_fields = {}
        for q in self.questions.all():
            form_fields[q.vpr] = forms.ChoiceField(required=False,
                                                         choices=q.choices(),
                                                         widget=forms.RadioSelect)
        return type('MchoiceForm', (forms.Form,), form_fields)

    def info_view(self, request):
        return render(request, self.template(self.info_viewname), { 'task': self })

    def task_view(self, request):
        if request.method == 'POST':
            form = self.form()(request.POST)
            if form.is_valid():
                result = {}
                for q in self.questions.all():
                    uradni = q.answers.get(prav=True)
                    result[q.id] = {'uradni': uradni.ans}
                    if form.cleaned_data[q.vpr]:
                        if uradni.id == int(form.cleaned_data[q.vpr]):
                            result[q.id]['tip'] = 'tvojpravilni'
                        else:
                            result[q.id]['tip'] = 'uradnitvoj'
                            result[q.id]['tvoj'] = q.answers.get(id=form.cleaned_data[q.vpr]).ans
                    else:
                        result[q.id]['tip'] = 'pravilni'
                return render(request, self.template(self.sol_templname),
                              { 'result': result, 'task': self })
        else:
            form = self.form()()

        return render(request, self.template(self.task_templname),
                      { 'task': self, 'form': form, 'inv':
                       f"{self.fullname}_task" })

    @staticmethod
    def template(viewname):
        return f"naloge/{viewname}.html"

    @property
    def info_viewname(self):
        return f"{self.fullname}_text"
    @property
    def task_templname(self):
        return f"mchoice_task"
    @property
    def sol_templname(self):
        return f"mchoice_sol"
    @property
    def task_viewname(self):
        return f"{self.fullname}_task"
    @property
    def sol_viewname(self):
        return f"{self.fullname}_sol"

    def urlpatterns(self):
        from django.urls import path
        def hsh(s):
            return str(sum(ord(c)*17**i for i,c in enumerate(s)))[-3:]
        def url(viewname):
            return f"{hsh(viewname)}_{viewname}"
        return [
                path(url(self.info_viewname), self.info_view, name=self.info_viewname),
                path(url(self.task_viewname), self.task_view, name=self.task_viewname),
        ]

class MchoiceQuestion(models.Model):
    nal = models.ForeignKey("MchoiceTask", on_delete = models.CASCADE, verbose_name = "Naloga vprašanja", related_name="questions")
    vpr = models.CharField(max_length = 500, verbose_name = "vprašanje")
    kom = models.CharField(max_length = 500,
                           verbose_name = "komentar po rešenem vprašanju", blank=True)

    def __str__(self):
        return f"{self.nal.category} | {self.nal.name}: {self.vpr}"

    def choices(self):
        return [(a.id, a.ans) for a in self.answers.all()]

class MchoiceAnswer(models.Model):
    vpr = models.ForeignKey("MchoiceQuestion", on_delete = models.CASCADE, verbose_name = "vprašanje", related_name="answers")
    ans = models.CharField(max_length = 200, verbose_name = "odgovor")
    prav = models.BooleanField(verbose_name = "odgovor je pravilen", default=False)

    def __str__(self):
        return f"{self.vpr.nal.category} | {self.prav} | {self.ans}"

class Attempt(models.Model):
    date = models.DateField()
    points = models.IntegerField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey('konzola.User', on_delete=models.CASCADE)


