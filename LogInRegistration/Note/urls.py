from django.urls import path
from Note import views as NoteView

urlpatterns = [
    path('notes', NoteView.Notes.as_view(), name='notes'),
]