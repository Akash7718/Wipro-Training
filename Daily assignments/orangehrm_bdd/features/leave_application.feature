Feature: Leave Application Workflow

  Background:
    Given user is logged in as "Admin" with password "admin123"
    And navigating to the Leave module

  Scenario: Apply for Medical Leave and verify pending status
    When select leave type "CAN - Medical"
    And enters from date and to date for leave
    And submits the leave application
    Then success toast message should appear
    And leave balance should be reduced on the screen
    And leave status should show "Pending Approval"
