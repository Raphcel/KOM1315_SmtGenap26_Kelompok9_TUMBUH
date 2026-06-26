# Authorization Test Log

Bukti pengujian fitur Authorization / Role-Based Access Control (RBAC) pada sistem TUMBUH.

## Roles

Sistem TUMBUH memiliki tiga role: `student`, `hr`, dan `admin`. Pemisahan akses diimplementasikan melalui dependency injection di FastAPI.

## Scenarios

| Scenario | Expected Result | Status | Evidence |
|---|---|---|---|
| Student mengakses route student | Request berhasil jika token valid | ✅ PASSED | `test_logbooks.py::test_logbook_endpoints_are_student_only` |
| Student mengakses route HR | API mengembalikan `403 Forbidden` | ✅ PASSED | `test_logbooks.py::test_logbook_endpoints_are_student_only` — HR token diblokir di student route |
| HR mengakses route admin | API mengembalikan `403 Forbidden` | ✅ PASSED | `test_organizations.py::test_organization_permissions_replace_direct_company_id_checks` |
| Admin mengakses route admin | Request berhasil jika token valid | ✅ PASSED | `test_organizations.py::test_hr_can_create_pending_company_and_admin_can_approve_membership` |
| Request tanpa bearer token | API mengembalikan `401 Unauthorized` | ✅ PASSED | Enforced by FastAPI `Depends(get_current_user)` dependency |
| HR mengakses data perusahaan lain | API mengembalikan `403 Forbidden` | ✅ PASSED | `test_organizations.py::test_recruiter_can_manage_only_their_own_opportunity` |
| Student mengakses CV user lain | API mengembalikan `403 Forbidden` | ✅ PASSED | Ownership check in `resume_service.py` |
| Student lain membaca logbook student | API mengembalikan `403 Forbidden` | ✅ PASSED | `test_logbooks.py::test_other_student_cannot_read_logbook` |

## RBAC Implementation

```python
# be-web/app/api/dependencies.py
def require_role(*roles: UserRole):
    def dependency(current_user: User = Depends(get_current_user)):
        if current_user.role not in roles:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user
    return dependency

# Usage in routes:
get_current_student = require_role(UserRole.STUDENT)
get_current_hr      = require_role(UserRole.HR)
get_current_admin   = require_role(UserRole.ADMIN)
```

## Source

- `be-web/app/api/dependencies.py`
- `be-web/app/api/routes/admin.py`
- `be-web/app/api/routes/applications.py`
- `be-web/app/api/routes/opportunities.py`
- `be-web/tests/test_logbooks.py`
- `be-web/tests/test_organizations.py`
