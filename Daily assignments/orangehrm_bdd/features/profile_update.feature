@Regression @Profile
Feature: Profile Update - My Info Section

  Background:
    Given logged in as "Admin" with password "admin123"
    And navigating to the My Info section

  @Smoke @Profile
  Scenario: Update nickname and upload profile photograph
    When updating the nickname to "AdminAntu"
    And click the save button on personal details
    Then nickname should be saved successfully
    When upload a profile photograph "profile_pic.jpg"
    Then profile photograph should be updated successfully
