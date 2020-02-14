from rest_framework import serializers, viewsets
from .models import Note, PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    # Inner class nested inside PersonalNoteSerializer
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note


class PersonalNoteViewset(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = Note.objects.none()

    def get_queryset(self):
        user = self.request.user
        return PersonalNote.objects.none() if user.is_anonymous else PersonalNote.objects.filter(user=user)
