Feature: Personal Data Removal Request
  As a user, I want to submit a request to remove an individual's personal data from the site.

  Scenario Outline: Submitting a personal data removal request
    Given I am on the data store site's removal page
    Then I click the "Start removal request" button
    When I pause on a page for "<seconds>" seconds

    Examples:
      | seconds |
      | 5       |
      
    # When I enter the name "<name>" and message "<message>"
    # And I submit the request
    # Then I should see a confirmation message

    # Examples:
    #   | name     | message                        |
    #   | John Doe | Please remove my personal data |