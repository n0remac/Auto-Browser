from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave.runner import Context
from behave import *

import time


def wait_for_element(context, element_locator, by=By.CSS_SELECTOR, timeout=10):
    """
    Wait for an element to become visible and interactable on the page.
    """
    WebDriverWait(context.browser, timeout).until(
        EC.visibility_of_element_located((by, element_locator))
    )

# User navigates to the data store site's removal page

@given('I am on the data store site\'s removal page')
def step_impl(context: Context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://support.google.com/websearch/answer/9673730")

@then('I pause on a page for "{seconds}" seconds')
def step_impl(context, seconds):
    time.sleep(int(seconds))

@then('I click the "Start removal request" button')
def step_impl(context: Context):
    button = context.browser.find_element(By.LINK_TEXT, "Start removal request")
    button.click()

# User selects the type of content they want to remove

@then('I select "Content contains nudity or sexual material"')
def step_impl(context):
    wait_for_element(context, "label[for='user_select--explicit_content']")
    label_for_explicit_content = context.browser.find_element(By.CSS_SELECTOR, "label[for='user_select--explicit_content']")
    label_for_explicit_content.click()

@then('I select "Content contains your personal information"')
def step_impl(context):
    wait_for_element(context, "label[for='user_select--nonexplicit_personal_pii']")
    label_for_personal_info = context.browser.find_element(By.CSS_SELECTOR, "label[for='user_select--nonexplicit_personal_pii']")
    label_for_personal_info.click()

@then('I select "Content is on a site with exploitative removal practices"')
def step_impl(context):
    wait_for_element(context, "label[for='user_select--predatory_removals']")
    label_for_exploitative_practices = context.browser.find_element(By.CSS_SELECTOR, "label[for='user_select--predatory_removals']")
    label_for_exploitative_practices.click()

@then('I select "Content shows a person under 18"')
def step_impl(context):
    wait_for_element(context, "label[for='user_select--nonexplicit_minor']")
    label_for_minor_content = context.browser.find_element(By.CSS_SELECTOR, "label[for='user_select--nonexplicit_minor']")
    label_for_minor_content.click()

@then('I click the "Next" button')
def step_impl(context):
    next_button = context.browser.find_element(By.XPATH, "//button[contains(@class, 'next-button') and text()='Next']")
    next_button.click()

# User selects the type of personal information they want to remove

@then('I select "Address, phone number, and/or e-mail address"')
def step_impl(context):
    wait_for_element(context, "label[for='pii_field--contact']")
    label = context.browser.find_element(By.CSS_SELECTOR, "label[for='pii_field--contact']")
    label.click()

@then('I select "Confidential government identification numbers"')
def step_impl(context):
    wait_for_element(context, "label[for='pii_field--govt']")
    label = context.browser.find_element(By.CSS_SELECTOR, "label[for='pii_field--govt']")
    label.click()

@then('I select "Bank account or credit card number"')
def step_impl(context):
    wait_for_element(context, "label[for='pii_field--bank']")
    label = context.browser.find_element(By.CSS_SELECTOR, "label[for='pii_field--bank']")
    label.click()

@then('I select "Images of a handwritten signature or an ID doc"')
def step_impl(context):
    wait_for_element(context, "label[for='pii_field--signature']")
    label = context.browser.find_element(By.CSS_SELECTOR, "label[for='pii_field--signature']")
    label.click()

@then('I select "Highly personal, restricted, and official records"')
def step_impl(context):
    wait_for_element(context, "label[for='pii_field--official']")
    label = context.browser.find_element(By.CSS_SELECTOR, "label[for='pii_field--medical']")
    label.click()

@then('I select "Confidential login credentials"')
def step_impl(context):
    wait_for_element(context, "label[for='pii_field--login']")
    label = context.browser.find_element(By.CSS_SELECTOR, "label[for='pii_field--login']")
    label.click()
