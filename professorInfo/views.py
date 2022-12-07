from django.db import connection
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from professorInfo.models import *
from django.core.exceptions import ObjectDoesNotExist
import pymongo
from bson.json_util import dumps
import json

@api_view(('GET',))
def show_info(request):
    #client = pymongo.MongoClient(db='proj', host='mongodb+srv://cluster0.fhrqfoj.mongodb.net/cluster0', username='CS410FinalProject', password='YCoH1NhOE3pI4XRU')
    myclient = pymongo.MongoClient('mongodb+srv://CS410FinalProject:YCoH1NhOE3pI4XRU@cluster0.fhrqfoj.mongodb.net')

    mydb = myclient["proj"]
    mycol = mydb["professor"]


    mydoc = mycol.find({}, {"_id":0})
    json_data = json.dumps(list(mydoc))
    json_pretty = json.loads(json_data)

    return Response(json_pretty)

@api_view(('GET',))
def find_by_email(request, email):
    myclient = pymongo.MongoClient('mongodb+srv://CS410FinalProject:YCoH1NhOE3pI4XRU@cluster0.fhrqfoj.mongodb.net')

    mydb = myclient["proj"]
    mycol = mydb["professor"]

    email = email + '@illinois.edu'


    mydoc = mycol.find({"email": email}, {"_id":0})
    json_data = json.dumps(list(mydoc))
    json_pretty = json.loads(json_data)

    return Response(json_pretty)

