Feature: Employee Management - PIM Module

  Background:
    Given user is logged in as "Admin" with password "admin123"
    And navigating to the PIM module

  Scenario Outline: Add multiple new employees
    When click the Add Employee button
    And entering first name "<FirstName>" and last name "<LastName>"
    And click the save button
    Then the employee "<FirstName> <LastName>" should be created successfully

    Examples:
      | FirstName | LastName  |
      | Adi       | Dash      |
      | Deep      | Pradhan   |
      | Suman     | Ashok     |
