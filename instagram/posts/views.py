from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostSerializer
from .models import Post


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication, )
    permissions_classes = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        try:
            user = request.user
            instance = self.get_object()
            if user.is_anonymous or user.id != instance.user_id:
                return Response({'message': 'you aren`t owner of this post'}, status=status.HTTP_403_FORBIDDEN)
            self.perform_destroy(instance)
        except:
            return Response({'message': 'doesn`t exists'})
        return Response(status=status.HTTP_204_NO_CONTENT)
