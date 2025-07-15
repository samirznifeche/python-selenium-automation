# Created by lenovo at 6/5/2025
Feature: Tests for Cart functionality

  @smoke
  Scenario: Verify Target Cart is empty
    Given Open Target main page
    When Open Cart page
    Then Verify "Your cart is empty" message is shown

  Scenario: Verify that cart has individual items
    Given Open Target main page
    When Search for Tea
    Then Select the product
    When Click Add to cart button
    And Open Cart page
    Then Verify cart has individual items