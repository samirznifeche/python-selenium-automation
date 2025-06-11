# Created by lenovo at 6/5/2025
Feature: Tests for Cart functionality

  Scenario: Verify Target Cart is empty
    Given Open Target main page
    When Target home page is opened
    Then Verify "Your cart is empty" message is shown


  Scenario: Verify that cart has individual items
    Given Open Target main page
    Then Search for a tea
    When Select the product
    And Add the product to the cart & view cart
    Then Verify cart has individual items