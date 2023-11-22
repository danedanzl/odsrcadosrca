from django.db import models

class Task(models.Model):

    name = models.CharField(max_length = 100)
    max_points = models.IntegerField()
    category = models.CharField(max_length=3,
                                choices=[("nnz", "Nič ne znam"), ("obv", "obvladam")])

    def __str__(self):
        return f"{self.category} | {self.name} | {self.max_points}"

class MchoiceTask(Task):
    pass

class MchoiceQuestion(models.Model):
    nal = models.ForeignKey("MchoiceTask", on_delete = models.CASCADE, verbose_name = "Naloga vprašanja")
    vpr = models.CharField(max_length = 500, verbose_name = "vprašanje")

    def __str__(self):
        return f"{self.nal.category} | {self.nal.name}: {self.vpr}"

class MchoiceAnswer(models.Model):
    vpr = models.ForeignKey("MchoiceQuestion", on_delete = models.CASCADE, verbose_name = "vprašanje")
    ans = models.CharField(max_length = 200, verbose_name = "odgovor")
    odg = models.CharField(max_length = 200,
                           verbose_name = "odgovor, ki ga dobi uporabnik, če izbere ta odgovor", blank=True)
    prav = models.BooleanField(verbose_name = "odgovor je pravilen", default=False)

    def __str__(self):
        return f"{self.vpr.nal.category} | {self.prav} | {self.ans}"

class Attempt(models.Model):
    date = models.DateField()
    points = models.IntegerField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey('konzola.User', on_delete=models.CASCADE)


