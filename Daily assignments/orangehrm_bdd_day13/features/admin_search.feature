Feature: Admin User Search

  Background:
    Given the user is logged in as "Admin" with password "admin123"
    And the user navigates to the Admin module

  Scenario: Search users with multiple filter criteria
    When I enter the following search criteria:
      | Username  | Admin   |
      | User Role | Admin   |
      | Status    | Enabled |
    And the user clicks the search button
    Then the search results should display matching user records
