from rest_framework.views import APIView,Response



class Index(APIView):
    """
    [This method will return welcome message]
    """
    def get(self,request):
        return Response({'message':'Welcome to Login and Registration App'})