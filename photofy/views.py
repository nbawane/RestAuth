from django.shortcuts import render, HttpResponse
# from .loadimagestoDB import SimulateTest
from rest_framework import generics,status
from rest_framework.authentication import TokenAuthentication
from .models import Group,Photos,CeleryData
from .flickrserializer import PhotoDetailsSerializer,FlickrGroupSerializers,FlickrGroupDetailSerializers,PhotoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_auth.views import LogoutView,APIView
from rest_framework import viewsets
from .tasks import download_data
from django.http import JsonResponse
from celery.result import AsyncResult
from django.shortcuts import get_object_or_404

# Create your views here.
# def builddb(request):
#     print('loading data')
#     ob = SimulateTest()
#     ob.extract_url()
#     return HttpResponse('<h1>done</h1>')

class Logout(LogoutView):
    #current implementation in library not asking for token
    # for logout, hence inheriteded to ass tokenauthentication
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):

    """
    This viewset automatically provides `list` and `detail` actions on Groups
    like list of photoid in that group/all groups in that group.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Group.objects.all()
    serializer_class = FlickrGroupSerializers

class GroupDetailsViewSet(GroupViewSet):
    '''
    this viewset gives output groupdetails like group name, id number of photos in that group
    '''
    #inheriting and changing serializer as per requirement
    serializer_class = FlickrGroupDetailSerializers

class PhotosViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    like photoid, photoname, photourl, owner.
     """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Photos.objects.all()
    serializer_class = PhotoDetailsSerializer

    def get_queryset(self):
        #upon querying with param group should return all the photos url in group
        if self.request.query_params.get('group',None): #extract group param from url
            print('entered in list ')
            self.serializer_class = PhotoSerializer
            # serializer_class = PhotoSerializer
            groupid= self.request.query_params.get('group',None)
            queryset = Photos.objects.filter(groupid=groupid)
            return queryset

        elif self.kwargs.get('pk'): #for retrive mode if we get pk
            # return photodetails
            queryset = Photos.objects.all()
            return queryset
        else:
            queryset = Photos.objects.all()
            return queryset


class downloadmedia(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        print('post')
        downloadlink = request.POST['downloadlink']
        resp = download_data.delay(downloadlink)
        id = resp.id
        obj = CeleryData(celeryid=id)
        obj.save()
        data = {'poling_id':id}
        return JsonResponse(data,status=status.HTTP_202_ACCEPTED)


    def get(self,request):
        print('polling')
        celeryid = request.query_params.get('cid',None)
        if celeryid:
            res = AsyncResult(celeryid)
            taskstat = res.state
            data = {'result':taskstat}
            return JsonResponse(data , status=status.HTTP_200_OK)
        else:
            data = {'result':'id not found'}
            return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)


