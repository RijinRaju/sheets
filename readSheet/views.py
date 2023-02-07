from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from .models import Data
from .serializers import DataSerializers
# Create your views here.


@api_view(['POST'])
def storeData(request):
    myfile = request.FILES('myfile')
    fs = FileSystemStorage()

    fileName = fs.save(myfile.name,myfile)
    uploadedFile = fs.url(fileName)
    
    eData = pd.read_excel(fileName)
    datas = eData
    for data in datas.itertuples():
        object = Data.objects.create(firstName =data.FirstName,last_name = data.LastName,
        gender = data.gender,country=data.Gender,age = data.Age,
        date = data.Date,Eid = data.Id)

        object.save()

    
    return Response()


