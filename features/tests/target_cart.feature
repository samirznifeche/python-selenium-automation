# Created by lenovo at 6/5/2025
Feature: Target Cart

  Scenario: Verify Target cart is empty
    Given open target home page
    When target home page is opened
    Then Verify "Your cart is empty" message is shown

  Scenario: Navigate to Sign In page
    Given open target home page
    Then click "Account" button
    Then click "Sign In" button
    Then verify Sign In form opened