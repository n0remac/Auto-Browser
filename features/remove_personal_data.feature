Feature: Personal Data Removal Request
  As a user, I want to submit a request to remove an individual's personal data from the site.

  Scenario Outline: Submitting a personal data removal request
    Given I am on the data store site's removal page
    Then I click the "Start removal request" button
    Then I select "Content contains your personal information"
    Then I click the "Next" button
    Then I select "Bank account or credit card number"
    Then I pause on a page for "<seconds>" seconds

    Examples:
      | seconds |
      | 5     |
