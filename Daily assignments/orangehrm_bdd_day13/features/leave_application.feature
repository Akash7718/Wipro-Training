Feature: Leave Application Workflow

  Background:
    Given the user is logged in as "Admin" with password "admin123"
    And the user navigates to the Leave module

  Scenario: Apply for Medical Leave and verify balance deduction
    Given I store the initial leave balance
    When the user selects leave type "CAN - Medical"
    And the user enters from date and to date for leave
    And the user submits the leave application
    Then a success toast message should appear
    And the leave balance should be reduced by 1 day
