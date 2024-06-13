from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CFA, Etudiant
from .serializers import CFASerializer, EtudiantSerializer

class CFAViewSet(viewsets.ModelViewSet):
    queryset = CFA.objects.all()
    serializer_class = CFASerializer

    @action(detail=True, methods=['post'])
    def inscription(self, request, pk=None):
        cfa = self.get_object()
        serializer = EtudiantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cfa=cfa, invite_par=cfa)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
