from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import ClientSerializer, UnLoadingSerializer, UnLoadingUpdateSerializer, UnLoadingListSerializer
from .models import Client, UnLoading


class ClientCreate(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CliensList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )


class UnLoadingCreate(generics.CreateAPIView):
    queryset = UnLoading.objects.all()
    serializer_class = UnLoadingSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # request.data._mutable = True
        # request.data['client'] = Clients
        serializer = UnLoadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdatePaid(APIView):
    queryset = UnLoading.objects.all()
    serializer_class = UnLoadingUpdateSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        unloading = UnLoading.objects.filter(id=request.data['id']).first()
        if unloading:
            try:
                unloading.alredy_paid = request.data['alredy_paid']
                unloading.save()
                serializer = UnLoadingUpdateSerializer(unloading)
                return Response(serializer.data)
            except:
                pass
        return Response({'error': 'can`t update model'})

class UnloadingList(generics.ListAPIView):
    queryset = UnLoading.objects.all()
    serializer_class = UnLoadingListSerializer
    permission_classes = (IsAuthenticated, )

class UnloadingClientList(generics.ListAPIView):
    queryset = UnLoading.objects.all()
    serializer_class = UnLoadingListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, client_id):
        client = Client.objects.filter(id=client_id).first()
        if client:
            # try:
            unloads = reversed(UnLoading.objects.filter(client=client))
            serializer = UnLoadingListSerializer(unloads, many=True)
            data = serializer.data
            debt = 0
            for i in data:
                to_pay = i['price'] + debt
                debt = to_pay - i['alredy_paid']
                i['debt'] = debt
            return Response(data)
            # except:
            #     pass
        return Response({'error': 'can`t filter model'})
