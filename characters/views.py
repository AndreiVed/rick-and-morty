from random import choices
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from characters.models import Character
from serializer import CharacterSerializer


@api_view(["GET"])
def get_random_character_view(request: Request) -> Response:
    pks = Character.objects.values_list("pk", flat=True)
    # random_pk = choices(pks)
    random_pk = int("".join(map(str, choices(pks))))
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        queryset = Character.objects.all()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
