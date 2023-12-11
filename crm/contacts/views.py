from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Contact
from .serializers import contactSerializer

class contactListAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = contactSerializer
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = (IsAdminUser,)  # Uncomment and add necessary permissions

class contactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = contactSerializer
    permission_classes = [permissions.IsAuthenticated]  # Set authentication requirement
    
    def get_permissions(self):
        if self.request.method in ['GET']:
            return [permissions.IsAuthenticated()]  # Allow only authenticated users for GET requests
        return super().get_permissions()

    def get(self, request, *args, **kwargs):
        required_permission = 'account.can_access_account'
        if not request.user.has_perm(required_permission):
            return Response({"message": "Permission denied"}, status=403)
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        required_permission = 'account.can_access_account'
        if not request.user.has_perm(required_permission):
            return Response({"message": "Permission denied"}, status=403)
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        required_permission = 'account.can_access_account'
        if not request.user.has_perm(required_permission):
            return Response({"message": "Permission denied"}, status=403)
        return super().delete(request, *args, **kwargs)
