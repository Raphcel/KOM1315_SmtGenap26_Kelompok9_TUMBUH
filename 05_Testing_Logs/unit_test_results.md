# Unit Test Results

## Command

```bash
cd be-web
myenv\Scripts\python.exe -m pytest tests -v --tb=short
```

## Result

| Date | Command | Result | Notes |
|---|---|---|---|
| 2026-06-26 | `pytest tests -v` | **39 passed, 0 failed** | Python 3.13.1, pytest 8.3.3, ran in 10.03s |

## Detailed Test Output

```
============================= test session starts =============================
platform win32 -- Python 3.13.1, pytest-8.3.3, pluggy-1.6.0
asyncio: mode=Mode.STRICT

tests/test_account_security.py::AccountSecurityTests::test_deactivate_account_blocks_future_login PASSED
tests/test_account_security.py::AccountSecurityTests::test_delete_account_requires_matching_email_and_removes_owned_rows PASSED
tests/test_account_security.py::AccountSecurityTests::test_password_reset_email_allows_password_change PASSED
tests/test_alembic_migrations.py::test_alembic_revision_graph_has_single_head PASSED
tests/test_logbooks.py::LogbookApiTests::test_accepted_application_autofills_and_rejects_duplicates PASSED
tests/test_logbooks.py::LogbookApiTests::test_attachment_upload_validation_and_download PASSED
tests/test_logbooks.py::LogbookApiTests::test_legacy_singular_logbook_list_route_is_supported PASSED
tests/test_logbooks.py::LogbookApiTests::test_logbook_endpoints_are_student_only PASSED
tests/test_logbooks.py::LogbookApiTests::test_manual_logbook_create_entry_validation_and_pdf_export PASSED
tests/test_logbooks.py::LogbookApiTests::test_other_student_cannot_read_logbook PASSED
tests/test_notifications.py::OpportunityMatcherTests::test_empty_targeting_fields_do_not_match PASSED
tests/test_notifications.py::OpportunityMatcherTests::test_major_match_qualifies PASSED
tests/test_notifications.py::OpportunityMatcherTests::test_three_skill_matches_qualify PASSED
tests/test_notifications.py::OpportunityMatcherTests::test_two_skill_matches_do_not_qualify PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_company_follow_endpoint_is_student_only PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_company_opportunity_list_tolerates_malformed_requirements_json PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_followed_company_notification_suppresses_duplicate_fit_digest PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_followed_company_opportunity_notifies_matching_major_follower_only PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_followed_company_skips_already_applied_student PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_matching_opportunities_roll_up_student_digest_same_day PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_new_active_opportunity_notifies_matching_active_students_only PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_notification_service_marks_read_state PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_status_update_notifies_student PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_student_application_notifies_company_hr PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_student_application_rolls_up_hr_notification_same_day PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_student_can_follow_unfollow_company_without_duplicates PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_student_registration_creates_onboarding_notification PASSED
tests/test_notifications.py::NotificationWorkflowTests::test_unmatched_active_opportunity_creates_no_student_notifications PASSED
tests/test_organizations.py::OrganizationWorkflowTests::test_hr_can_create_pending_company_and_admin_can_approve_membership PASSED
tests/test_organizations.py::OrganizationWorkflowTests::test_hr_can_join_company_with_invite_code_once PASSED
tests/test_organizations.py::OrganizationWorkflowTests::test_organization_permissions_replace_direct_company_id_checks PASSED
tests/test_organizations.py::OrganizationWorkflowTests::test_public_lists_ignore_pending_companies_and_keep_approved_visible PASSED
tests/test_organizations.py::OrganizationWorkflowTests::test_recruiter_can_manage_only_their_own_opportunity PASSED
tests/test_security_service.py::test_encrypt_decrypt_text_roundtrip PASSED
tests/test_security_service.py::test_digital_signature_detects_tampering PASSED
tests/test_user_schema.py::UserSocialLinkValidationTests::test_social_links_add_missing_https PASSED
tests/test_user_schema.py::UserSocialLinkValidationTests::test_social_links_reject_plain_text PASSED
tests/test_user_schema.py::UserSocialLinkValidationTests::test_social_links_reject_wrong_platform_domain PASSED
tests/test_user_schema.py::UserSocialLinkValidationTests::test_social_links_remove_empty_values PASSED

============================== 39 passed, 19 warnings in 10.03s ===============
```

## Test Files

| File | Area | Tests | Result |
|---|---|---|---|
| `be-web/tests/test_security_service.py` | Encryption + digital signature | 2 | ✅ PASSED |
| `be-web/tests/test_account_security.py` | Account security + password flows | 3 | ✅ PASSED |
| `be-web/tests/test_alembic_migrations.py` | Migration graph integrity | 1 | ✅ PASSED |
| `be-web/tests/test_logbooks.py` | Student logbook behavior | 6 | ✅ PASSED |
| `be-web/tests/test_notifications.py` | Notification + opportunity matching | 18 | ✅ PASSED |
| `be-web/tests/test_organizations.py` | HR organization workflows | 5 | ✅ PASSED |
| `be-web/tests/test_user_schema.py` | User schema validation | 4 | ✅ PASSED |
| **Total** | | **39** | **✅ All passed** |
