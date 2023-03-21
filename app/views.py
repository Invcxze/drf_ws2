
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
class ProductApiView(APIView):

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post' : serializer.data})

    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            w = Product.objects.all()
            return Response({'posts': ProductSerializer(w, many=True).data})
        w = Product.objects.get(pk=pk)
        return Response({'posts': ProductSerializer(w).data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'id is required'})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({'error': 'object not found'})

        serializer = ProductSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'id is required'})
        w = Product.objects.get(pk=pk)
        w.delete()
        return Response({'post': 'delete post' + str(pk)})