from .models import Stock
from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from django.core.cache import cache



class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def list(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        cache.clear()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        stock = self.get_object()
        serializer = self.get_serializer(stock)
        cache.clear()
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.clear()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        stock = self.get_object()
        serializer = self.get_serializer(stock, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.clear()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        stock = self.get_object()
        stock.delete()
        cache.clear()
        return Response(status=status.HTTP_204_NO_CONTENT)


