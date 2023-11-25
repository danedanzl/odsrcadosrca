from django import forms
from django.urls import path, reverse
from django.shortcuts import render, redirect

class KT:
    def __init__(self, urlid, imgid, tasks, tip=None, location=None):
        self.urlid = urlid
        self.imgid = imgid
        self.obv = tasks[0]
        self.nnz = tasks[1]
        if tip is None:
            self.tip = "Tvoja mami"
        if location is None:
            self.location = "Brokopondo"

    def __lt__(self, other):
        return self.urlid < other.urlid
