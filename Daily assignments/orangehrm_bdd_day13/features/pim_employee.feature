Feature: Employee Management - PIM Module

  Background:
    Given the user is logged in as "Admin" with password "admin123"
    And the user navigates to the PIM module

  Scenario Outline: Add multiple new employees
    When the user clicks the Add Employee button
    And I enter "<FirstName>" and "<LastName>"
    And the user clicks the save button
    Then the employee should be created successfully

    Examples:
      | FirstName | LastName  |
      | Akash     | Ghorai    |
      | Deep      | Patra     |
      | Suman     | Das       |
