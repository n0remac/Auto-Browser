# AutoBrowser

This is an example of how to use Behave with Selenium in order to write tests with Behavior-driven development (BDD) syntax. BDD syntax uses a given, when, then format that is easy to understand. It makes your tests look like this:  
```
  Scenario Outline: Submitting a personal data removal request
    Given I am on the data store site's removal page
    Then I click the "Start removal request" button
```

Behave provides the BDD while Selenium interacts with the browser. This is useful for writing integration tests or creating other automated workflows in the browser.

## Intallation for Mac

Create python env:  
`python3 -m venv venv`  

Active env:  
`source venv/bin/activate`  

Install requirements:  
`pip install -r requirements.txt`  

Run test:  
`behave`  

## Useful links

Selenium locator strategies:  
https://www.selenium.dev/documentation/webdriver/elements/locators/