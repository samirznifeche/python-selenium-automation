# Created by lenovo at 6/8/2025
Feature: Tests for Sign In functionality

  Scenario: Navigate to Sign In page
    Given Open Target main page
    When Click "Account" button
    Then Click "Sign In" button
    And Verify Sign In form opened

  Scenario: User can open and close Terms and Conditions from sign in page
   Given Open sign in page
   When Store original window
   And Click on Target terms and conditions link
   And Switch to the newly opened window
   Then Verify Terms and Conditions page is opened
   And User can close new window and switch back to original