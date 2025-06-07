# Created by lenovo at 6/5/2025
Feature: Target Cart

  Scenario: Verify Target Cart is empty
    Given open target home page
    When target home page is opened
    Then verify "Your cart is empty" message is shown

  Scenario: Navigate to Sign In page
    Given open target home page
    Then click "Account" button
    And click "Sign In" button
    And verify Sign In form opened