
from platformdirs import api
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from .models import Data
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .serializers import DataSerializers
# Create your views here.

@api_view(['POST','GET'])
def storeData(request):
    queryset = Data.objects.all()
    serializer = DataSerializers(queryset)
    
    myfile = request.FILES('myfile')
    fs = FileSystemStorage()

    fName = fs.save(myfile.name,myfile)
    upFile = fs.url(fName)
    print(upFile)
    eData = pd.read_excel(fName)
    datas = eData
    for data in datas.itertuples():
        object = Data.objects.create(firstName =data.FirstName,last_name = data.LastName,
        gender = data.gender,country=data.Gender,age = data.Age,
        date = data.Date,Eid = data.Id)

        object.save()

    
    return Response(serializer.data)


