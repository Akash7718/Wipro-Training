@Regression @Profile
Feature: Profile Update - My Info Section

  Background:
    Given the user is logged in as "Admin" with password "admin123"
    And the user navigates to the My Info section

  @Smoke @Profile
  Scenario: Update nickname and upload profile photograph
    When the user updates the nickname to "AdminNick"
    And the user clicks the save button on personal details
    Then the nickname should be saved successfully
    When the user uploads a profile photograph "profile_pic.jpg"
    Then the profile photograph should be updated successfully
