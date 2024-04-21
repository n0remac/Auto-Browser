Feature: Scrape Interactive Web Elements
  As an automated system, I want to scrape all interactable elements from a given web page.

  Scenario: Scrape elements from a specified page
    Given I am on the specified web page
    Then I scrape all interactive elements
