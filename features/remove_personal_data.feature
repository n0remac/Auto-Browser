Feature: Personal Data Removal Request
  As a user, I want to submit a request to remove an individual's personal data from the site.

  Scenario Outline: Submitting a personal data removal request
    Given I am on the data store site's removal page
    Then I click the "Start removal request" link
    Then I select the radio button with id "user_select--nonexplicit_personal_pii"
    Then I click the "Next" button
    Then I select the radio button with id "pii_field--bank"
    Then I pause on a page for "<seconds>" seconds

    Examples:
      | seconds |
      | 5       |
