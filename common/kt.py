from django import forms
from django.urls import path, reverse
from django.shortcuts import render, redirect

class KT:
    def __init__(self, urlid, imgid, tasks, tip, location):
        self.urlid = urlid
        self.imgid = imgid
        self.obv = tasks[0]
        self.nnz = tasks[1]
        self.tip = tip
        self.location = location

    def __lt__(self, other):
        return self.urlid < other.urlid
