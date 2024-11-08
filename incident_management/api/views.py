from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (
    Employee,
    RegistrationRequest,
    Department,
    UserRole,
    Witness,
    IncidentReport,
    Attachment,
    ActionPlan,
    AssignedPersonnel,
    AuditTrail
)
from .serializers import (
    EmployeeSerializer,
    RegistrationRequestSerializer,
    DepartmentSerializer,
    UserRoleSerializer,
    WitnessSerializer,
    IncidentReportSerializer,
    AttachmentSerializer,
    ActionPlanSerializer,
    AssignedPersonnelSerializer,
    AuditTrailSerializer
)

# Employee ViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

# Registration Request ViewSet

class RegistrationRequestViewSet(viewsets.ModelViewSet):
    queryset = RegistrationRequest.objects.all()
    serializer_class = RegistrationRequestSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to access this endpoint

    @action(detail=False, methods=['post'])
    def approve(self, request, pk=None):
        """Approve a registration request and create an employee."""
        registration_request = self.get_object()
        employee_data = {
            'employee_name': registration_request.employee_name,
            'employee_email': registration_request.employee_email,
            'employee_department': registration_request.employee_department,
            'password': 'auto-generated-password',  # Generate a real password here
        }
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            registration_request.status = 'approved'
            registration_request.save()
            return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
        return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """Approve a registration request and create an employee."""
        registration_request = self.get_object()
        employee_data = {
            'employee_name': registration_request.employee_name,
            'employee_email': registration_request.employee_email,
            'employee_department': registration_request.employee_department,
            'password': 'auto-generated-password',  # Generate a real password here
        }
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            registration_request.status = 'approved'
            registration_request.save()
            return Response(employee_serializer.data, status=status.HTTP_201_CREATED)
        return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Department ViewSet
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

# User Role ViewSet
class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [permissions.IsAuthenticated]

# Witness ViewSet
class WitnessViewSet(viewsets.ModelViewSet):
    queryset = Witness.objects.all()
    serializer_class = WitnessSerializer
    permission_classes = [permissions.IsAuthenticated]

# Incident Report ViewSet
class IncidentReportViewSet(viewsets.ModelViewSet):
    queryset = IncidentReport.objects.all()
    serializer_class = IncidentReportSerializer
    permission_classes = [permissions.IsAuthenticated]

# Attachment ViewSet
class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticated]

# Action Plan ViewSet
class ActionPlanViewSet(viewsets.ModelViewSet):
    queryset = ActionPlan.objects.all()
    serializer_class = ActionPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

# Assigned Personnel ViewSet
class AssignedPersonnelViewSet(viewsets.ModelViewSet):
    queryset = AssignedPersonnel.objects.all()
    serializer_class = AssignedPersonnelSerializer
    permission_classes = [permissions.IsAuthenticated]

# Audit Trail ViewSet
class AuditTrailViewSet(viewsets.ModelViewSet):
    queryset = AuditTrail.objects.all()
    serializer_class = AuditTrailSerializer
    permission_classes = [permissions.IsAuthenticated]

