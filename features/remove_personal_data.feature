Feature: Automated Data Removal Request Handling

  Background:
    Given I am on the Google data store site's removal page

  Scenario Outline: Dynamically navigate and capture data for different initial selections
    When I click the "Start removal request" link
    And I select the "<description>"
    And I click the "Next" button
    Then I extract and send the HTML to ChatGPT
    And I save the new radio IDs into a file
    And I return to the initial data removal page

    Examples:
      | description                          |
      | Content contains nudity or sexual material    |
      | Content contains your personal information    |
      | Content is on a site with exploitative removal practices |
      | Content shows a person under 18               |
