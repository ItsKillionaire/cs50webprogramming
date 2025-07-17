from django.http import HttpResponse
# from django.shortcuts import render


# Create your views here.
def index(request):
    # Option A: Leave as string (recommended for simplicity, accept Pyright warning)
    # return HttpResponse("Hello, world!")

    # Option B: Explicitly encode to bytes (silences Pyright)
    return HttpResponse("Hello, world!".encode("utf-8"))


def kevin(request):
    # Option A: Leave as string
    # return HttpResponse("Hello, Kevin!")

    # Option B: Explicitly encode to bytes
    return HttpResponse("Hello, Kevin!".encode("utf-8"))


def greet(request, name):
    # Option A: Leave as string
    # return HttpResponse(f"Hello, {name.capitalize()}!")

    # Option B: Explicitly encode to bytes
    return HttpResponse(f"Hello, {name.capitalize()}!".encode("utf-8"))
