from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Mapping
from .serializers import MappingSerializer

class MappingViewSet(ModelViewSet):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def get_doctors_by_patient(self, request, patient_id=None):
        mappings = Mapping.objects.filter(patient_id=patient_id)
        data = [
            {
                "doctor_id": m.doctor.id,
                "doctor_name": m.doctor.name
            }
            for m in mappings
        ]
        return Response(data)