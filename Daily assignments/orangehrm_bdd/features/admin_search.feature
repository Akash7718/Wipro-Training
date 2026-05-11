Feature: Admin User Search

  Background:
    Given user is logged in as "Admin" with password "admin123"
    And user navigates to the Admin module

  Scenario: Search users with multiple filter criteria using data table
    When search for a user with the following criteria:
      | Username  | Admin   |
      | User Role | Admin   |
      | Status    | Enabled |
    And clicking the search button
    Then search results should display matching user records
