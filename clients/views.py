from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import ClientSerializer, UnLoadingSerializer, UnLoadingUpdateSerializer, UnLoadingListSerializer
from .models import Client, UnLoading
from rest_framework import status
import datetime

class ClientCreate(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CliensList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )


class UnLoadingCreate(generics.CreateAPIView):
    queryset = UnLoading.objects.all()
    serializer_class = UnLoadingSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = UnLoadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdatePaid(generics.CreateAPIView):
    queryset = UnLoading.objects.all()
    serializer_class = UnLoadingUpdateSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = UnLoadingUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnloadingList(generics.ListAPIView):
    queryset = reversed(UnLoading.objects.all())
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
            unloads = UnLoading.objects.filter(client=client)
            serializer = UnLoadingListSerializer(unloads, many=True)
            data = serializer.data
            debt = 0
            for i in data:
                date = datetime.datetime.strptime(i['date'], '%Y-%m-%d')
                i['date'] = date.strftime('%d-%m-%Y')
                to_pay = debt
                if i['price']:
                    to_pay = i['price'] + debt
                debt = to_pay - i['alredy_paid']
                i['debt'] = debt
            return Response(reversed(data))
            # except:
            #     pass
        return Response({'error': 'can`t filter model'}, status=status.HTTP_400_BAD_REQUEST)
