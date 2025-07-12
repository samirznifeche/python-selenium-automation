# Created by lenovo at 6/11/2025
Feature: Tests for Help functionality

  Scenario: Verify Target Help UI
    Given Open Target Help page
    Then Verify Target "Container" contains multiple links

  Scenario Outline:  Verify select topic works on Target Help page
    Given Open Help page for Returns
    Then Verify Help Returns page opened
    When Select Help <selected topic> topic
    Then Verify Help <expected header> page opened
    Examples:
    |selected topic     |expected header          |
    |Orders & Purchases | Print a receipt         |
    |Gift Cards         | Target GiftCard balance |
    |Technical Support  | Mobile & app support    |