from django.db import connection
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from planner.models import *
from .serializers import FoodSerializer
from django.core.exceptions import ObjectDoesNotExist
import json 

def show_info(request){
    try:
        
    except Food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
}
