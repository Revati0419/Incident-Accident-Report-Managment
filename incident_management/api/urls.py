# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    EmployeeViewSet,
    RegistrationRequestViewSet,
    DepartmentViewSet,
    UserRoleViewSet,
    WitnessViewSet,
    IncidentReportViewSet,
    AttachmentViewSet,
    ActionPlanViewSet,
    AssignedPersonnelViewSet,
    AuditTrailViewSet
)

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'registration-requests', RegistrationRequestViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'user-roles', UserRoleViewSet)
router.register(r'witnesses', WitnessViewSet)
router.register(r'incidents', IncidentReportViewSet)
router.register(r'attachments', AttachmentViewSet)
router.register(r'action-plans', ActionPlanViewSet)
router.register(r'assigned-personnel', AssignedPersonnelViewSet)
router.register(r'audit-trails', AuditTrailViewSet)

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include all viewset URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT obtain token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh token
]
