Feature: User Authentication

  Background:
    Given the user navigates to the OrangeHRM login page

  Scenario: Successful login with valid credentials
    When the user enters username "Admin" and password "admin123"
    And the user clicks the login button
    Then the current URL should contain "dashboard"

  Scenario: Unsuccessful login with invalid password
    When the user enters username "Admin" and password "invalid123"
    And the user clicks the login button
    Then an error message "Invalid credentials" should be displayed
