# RestAuth
This is basic DRF token authentication based django project skeleton, a  Mini version of Flickr API. This project is a cheat sheet for Token authentication with django-rest-auth lib.
Following endpoints have been designed
1) /api/v1/login/ -- This API when called with an username and password shouldreturn a Token
2) /api/v1/groups/ -- This API when called with the appropriate USER TOKEN usingDRF token authentication should return all the groups that below to the user withdetails such as group name, group id, number of photos etc.
3) /api/v1/group/<ID> -- This API when called with the appropriate USER TOKEN
using DRF token authentication should return all the photos <ID> belonging to the
group
4) /api/v1/photos/?group=<GID> -- This API when called with the appropriate USER
TOKEN using DRF token authentication and supplying a group id should return all
the photos belonging to the group
5) /api/v1/photos/<ID> -- This API when called with the appropriate USER TOKEN
using DRF token authentication should return details of the photo
6) /api/v1/logout – This API when called with the appropriate USER TOKEN using DRF
token authentication should logout the user and deactivate the token. Using the
same token to authenticate should fail.

Following are assumptions to use this skeleton
Following are assumptions and requirements to run this project
•	The project was built with python 3.6 

•	Groups are named as GroupA, GroupB and are given there own IDs ie, primary keys. Hence their ids are 1,2,3…These id are to be used while querying the API. Eg http://127.0.0.1:8000/api/V1/group/1/

•	Photos are given as their own id ie, their primary key. Hence their ids are 1,2,3,4….. These ids are to be used why querying. Eg. http://127.0.0.1:8000/api/V1/photos/?group=1


•	Superuser credentials
		Username: admin
		Password : Rasengan
•	Django-rest-auth framework has been used along with Django rest framework.

•	Login and logout methods are post methods
•	Data is already populated in sqllitDB
