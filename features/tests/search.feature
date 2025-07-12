Feature: Tests for Search functionality

  Scenario: User can search for tea
    Given Open Target main page
    When Search for tea
    Then Verify search worked for tea

  Scenario Outline: User can search for a product
    Given Open Target page
    When Input <search_word> into search field
    And Click on search icon
    Then Product results for <search_word> are shown
    Examples:
    |search_word |
    |tea         |
    |coffe       |
    |milk        |

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods
    Then Verify that every product has a name and an image

  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown