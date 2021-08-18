from rest_framework.views import APIView
from .serializer import NoteSerializer
from .models import Notes
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from django.contrib.auth.models import User
from Note.utils import verify_token
from log import get_logger

# Logger configuration
logger = get_logger()

class Notes(APIView):
    
    @verify_token
    def get(self, request):
        """
            This method is used to read data by id.
            :param request: It accepts id as parameter.
            :return: It returns the user information by using id.
        """
        try:
            user_note_id= request.data.get('id')
            if user_note_id is not None:
                data = Notes.objects.filter(user_note=user_note_id)
                serializer=NoteSerializer(data, many=True)
                return Response({"data":{"note-list": serializer.data}}, status=status.HTTP_200_OK)
            return Response({"message":"Put user id to get notes"}, status=status.HTTP_400_BAD_REQUEST)    
        except AssertionError as e:
            logger.exception(e)
            return Response({"message":"Put user id to get notes"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def post(self, request):
        """
            This method is used to insert data to create new note.
            :param request: It accepts user_id,title and description as parameter.
            :return: It returns Notes created after successful insertion.
        """
        try:
            id= User.objects.filter(id=request.data.get("id"))
            serializer = NoteSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            notes = Notes(user_note=id[0], title=serializer.data.get('title'), description=serializer.data.get('description'))
            notes.save()        
            return Response({'message': 'Notes created successfully'}, status=status.HTTP_200_OK)
        except KeyError as e:
            logger.exception(e)
            return Response({'message': 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            logger.exception(e)
            return Response({'message': 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token  
    def put(self,request):
        """
            This method is used to update note using note_id.
            :param request: It accepts note_id,title and description as parameter.
            :return: It returns Data Updated after successful updation.
        """
        try:

            id = request.data.get("note_id")
            notes = Notes.objects.get(pk=id)
            serializer = NoteSerializer(notes, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Complete Data Updated'}, status=status.HTTP_200_OK)
        except ValueError as e:
            logger.exception(e)
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            logger.exception(e)
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def delete(self,request):
        """
            This method is used to delete note using note_id.
            :param request: It accepts note_id as parameter.
            :return: It returns Data deleted after successful deletion.
        """
        try:
            id = request.data.get("note_id")
            user = Notes.objects.get(id=id)
            user.delete()
            return Response({'msg':'Data Deleted'}, status=status.HTTP_200_OK) 
        except ValueError as e:
            logger.exception(e)
            return Response({"message": 'Invalid Input'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(e)
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
