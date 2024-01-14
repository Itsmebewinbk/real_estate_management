from rest_framework import generics
from moonhive_real_estate.permission import IsAuthenticatedUser, IsAdmin
from core.models import Rental
from api.v1.core.serializers import RentalSerializer


class RentalListCreateView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = (IsAuthenticatedUser, IsAdmin)

    def get_queryset(self):
        return Rental.objects.filter(unit_id=self.kwargs.get("unit_id"))

    def get_serializer_context(self):
        return {
            "unit_id": self.kwargs.get("unit_id"),
        }


class RentalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = (IsAuthenticatedUser, IsAdmin)
    allowed_methods = ("GET", "PATCH", "DELETE")
