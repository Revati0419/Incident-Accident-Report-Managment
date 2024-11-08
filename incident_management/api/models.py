from django.db import models

# Employee Model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_department = models.CharField(max_length=100)
    employee_email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.employee_name


# Registration Request Model
class RegistrationRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField(unique=True)
    employee_department = models.CharField(max_length=100)
    role = models.CharField(max_length=20)  # e.g., 'initiator', 'hod', 'so'
    status = models.CharField(max_length=20, default='pending')  # e.g., 'pending', 'approved', 'denied'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Registration Request for {self.employee_name} ({self.status})"


# Department Model
class Department(models.Model):
    dept_code = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    dept_hod = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='hod_of_department')

    def __str__(self):
        return self.dept_name


# User Roles Model
class UserRole(models.Model):
    ROLE_CHOICES = [
        ('initiator', 'Initiator'),
        ('hod', 'Head of Department'),
        ('so', 'Safety Officer'),
    ]
    
    user_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user_id.employee_name} - {self.role}"


# Witness Model
class Witness(models.Model):
    witness_id = models.AutoField(primary_key=True)
    report_id = models.ForeignKey('IncidentReport', on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"Witness {self.witness_id} for Report {self.report_id}"


# Incident Report Model
class IncidentReport(models.Model):
    INCIDENT_TYPE_CHOICES = [
        ('incident', 'Incident'),
        ('accident', 'Accident'),
    ]
    
    STATUS_CHOICES = [
        ('initiated', 'Initiated'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ]

    report_id = models.AutoField(primary_key=True)
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPE_CHOICES)
    reporter_first_name = models.CharField(max_length=100)
    reporter_last_name = models.CharField(max_length=100)
    employee_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    incident_date = models.DateField()
    incident_time = models.TimeField()
    location = models.CharField(max_length=255)
    injuries = models.BooleanField(default=False)
    property_damage = models.BooleanField(default=False)
    description = models.TextField()
    root_cause = models.TextField(blank=True, null=True)
    immediate_actions = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='initiated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Report {self.report_id}: {self.incident_type} at {self.location}"


# Attachments Model
class Attachment(models.Model):
    attachment_id = models.AutoField(primary_key=True)
    report_id = models.ForeignKey(IncidentReport, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='attachments/')  # Adjust the upload path as needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment {self.attachment_id} for Report {self.report_id}"


# Action Plan Model
class ActionPlan(models.Model):
    action_plan_id = models.AutoField(primary_key=True)
    report_id = models.ForeignKey(IncidentReport, on_delete=models.CASCADE)
    safety_officer_id = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Assuming Safety Officer is an Employee
    summary = models.TextField()
    tentative_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    
# Assigned Personnel Model
class AssignedPersonnel(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    report_id = models.ForeignKey(IncidentReport, on_delete=models.CASCADE)
    personnel_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assigned_personnel')
    hod_id = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Assuming HoD is also an Employee
    action_description = models.TextField()
    
    STATUS_CHOICES = [
        ('assigned', 'Assigned'),
        ('completed', 'Completed'),
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')
    
   # Audit Trail Model
class AuditTrail(models.Model):
     audit_id  =  models.AutoField(primary_key=True) 
     report_id  =  models.ForeignKey(IncidentReport , on_delete=models.CASCADE) 
     changed_by  =  models.ForeignKey(Employee , on_delete=models.CASCADE) 
     timestamp  =  models.DateTimeField(auto_now_add=True) 
     ip_address  =  models.GenericIPAddressField() 
     changes  =  models.JSONField() 

     def __str__(self):
         return f"Audit Trail {self.audit_id} for Report {self.report_id}"

