from .models import Photos,Group
from rest_framework import serializers

class FlickrGroupDetailSerializers(serializers.ModelSerializer):
    #this serializer for details of group
    photocount = serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = ('id','groupname','photocount')

    def get_photocount(self, obj):
        return obj.gname.count()    #to get the count of childs in reverse relation ships, 'gname' is related object name

class FlickrGroupSerializers(serializers.ModelSerializer):
    #this serializer for photoid list
    photoidlist = serializers.PrimaryKeyRelatedField(source='gname',read_only=True,many=True)   #'gname' is the related field name
    class Meta:
        model = Group
        fields = ('id','photoidlist',)



class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ('id','photourl',)


class PhotoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ('id','owner','title')


