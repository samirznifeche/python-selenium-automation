# Created by lenovo at 6/8/2025
Feature: Tests for Sign In functionality

  Scenario: Navigate to Sign In page
    Given Open Target main page
    When Click "Account" button
    Then Click "Sign In" button
    And Verify Sign In form opened