from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from backend.models import *

# Create your views here.
def post(request):
    upc = request.POST["upc"]
    poster = request.POST["poster"]
    contents = request.POST["contents"]
    prod = Product.objects.get(upc=upc)
    comment = Comment.objects.create(
        product=prod,
        poster=poster,
        contents=contents
    )
    return JsonResponse({
        "success": True,
        "id": comment.id,
        "poster": str(poster),
        "contents": str(contents),
        "score": 0
    })

def getPosts(request):
    upc = request.GET["upc"]
    posts = {
        "success": True,
        "posts": []
    }
    for comment in Comment.objects.filter(product__upc=upc).order_by('-score'):
        posts["posts"].append({
            "id": comment.id,
            "score": int(comment.score),
            "poster": str(comment.poster),
            "contents": str(comment.contents)
        })
    return JsonResponse(posts)

def auth(request):
    username = request.POST["username"]
    password = request.POST["password"]
    try:
        user = InsecureUser.objects.get(username=username)
        return JsonResponse({"success": True})
    except:
        return JsonResponse({"success": False})

def register(request):
    username = request.POST["username"]
    password = request.POST["password"]
    success = True
    try:
        user = InsecureUser.objects.create(username=username, password=password)
    except:
        success = false
    return JsonResponse({"success": success})

def vote(request):
    try:
        cid = request.POST["id"]
        increment = request.POST["increment"]
        cmt = Comment.objects.get(id=cid)
        print(cmt.score)
        cmt.score += int(increment)
        cmt.save()
        return JsonResponse({"success": True, "score": cmt.score})
    except:
        return JsonResponse({"success": True, "score": 0})

def lookup(request):
    try:
        upc = request.GET["upc"]
        product = get_object_or_404(Product, upc=upc)
        prodJson = {
            "upc": product.upc,
            "name": product.name,
            "recycle": product.recyclingType,
            "imageUrl": product.imageUrl,
            "harmful_ingredients": []
        }
        for hazmat in product.hazmats.all():
            prodJson["harmful_ingredients"].append(hazmat.material)
        return JsonResponse({
            "success": True,
            "product": prodJson
        })
    except(e):
        return JsonResponse({
            "success": False,
            "product": {}
        })

def search(request):
    try:
        response = {
            "success": True,
            "items": []
        }
        products = Product.objects.filter(Q(upc__icontains=request.GET["term"]) | Q(searchName__icontains=request.GET["term"]))[:10]
        for product in products:
            prodJson = {
                "upc": product.upc,
                "name": product.name
            }
            response["items"].append(prodJson)
        return JsonResponse(response)
    except:
        return JsonResponse({
            "success": False,
            "items": []
        })
