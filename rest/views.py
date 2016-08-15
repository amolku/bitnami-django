from django.http import HttpResponse
from rest.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from rest.models import Snippet
from django.contrib.auth.models import User
from rest_framework import permissions
from rest.permissions import IsOwnerOrReadOnly # written by me
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from rest_framework import viewsets
from rest_framework.decorators import detail_route

from django.shortcuts import get_object_or_404, render

# not rest
def index(request):
    return render(request, 'rest/index.html', None)

class SnippetViewSet(viewsets.ModelViewSet):
    # This viewset automatically provides list, create, retrieve, update and destroy actions
    # Additionally, we also provide an extra "hihglight" action

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    # the decorator can be used to add any custom endpoints that dont fit into the standard
    # create/udpate/delete style
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # This viewset automatically provides list and detail actions
    queryset = User.objects.all()
    serializer_class = UserSerializer