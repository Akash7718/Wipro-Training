Feature: User Authentication

  Background:
    Given user navigates to the OrangeHRM login page

  Scenario: Successful login with valid credentials
    When entering username "Admin" and password "admin123"
    And click the login button
    Then user should be redirected to the dashboard page

  Scenario: Unsuccessful login with invalid password
    When entering username "Admin" and password "invalid123"
    And click the login button
    Then an error message "Invalid credentials" should be displayed
