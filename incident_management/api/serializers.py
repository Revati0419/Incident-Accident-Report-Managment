from rest_framework import serializers
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

# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'employee_name', 'employee_department', 'employee_email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Hash the password before saving
        employee = Employee(**validated_data)
        employee.set_password(validated_data['password'])  # Use Django's password hashing
        employee.save()
        return employee


# Registration Request Serializer
class RegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationRequest
        fields = ['request_id', 'employee_name', 'employee_email', 'employee_department', 'role', 'status', 'created_at', 'updated_at']


# Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['dept_code', 'dept_name', 'dept_hod']


# User Role Serializer
class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['user_id', 'role']


# Witness Serializer
class WitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Witness
        fields = ['witness_id', 'report_id', 'employee_id']


# Incident Report Serializer
class IncidentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentReport
        fields = [
            'report_id',
            'incident_type',
            'reporter_first_name',
            'reporter_last_name',
            'employee_id',
            'incident_date',
            'incident_time',
            'location',
            'injuries',
            'property_damage',
            'description',
            'root_cause',
            'immediate_actions',
            'status',
            'created_at',
            'updated_at'
        ]


# Attachment Serializer
class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['attachment_id', 'report_id', 'file_path', 'created_at']


# Action Plan Serializer
class ActionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionPlan
        fields = ['action_plan_id', 'report_id', 'safety_officer_id', 'summary', 'tentative_date', 'created_at']


# Assigned Personnel Serializer
class AssignedPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedPersonnel
        fields = ['assignment_id', 'report_id', 'personnel_id', 'hod_id', 'action_description', 'status']


# Audit Trail Serializer
class AuditTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditTrail
        fields = ['audit_id', 'report_id', 'changed_by', 'timestamp', 'ip_address', 'changes']
