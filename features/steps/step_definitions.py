from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave.runner import Context
from behave import *

import time


# Dictionary mapping descriptions to element IDs
radio_button_ids = {
    # User selection descriptions
    "Content contains nudity or sexual material": "user_select--explicit_content",
    "Content contains your personal information": "user_select--nonexplicit_personal_pii",
    "Content is on a site with exploitative removal practices": "user_select--predatory_removals",
    "Content shows a person under 18": "user_select--nonexplicit_minor",
    # PII field descriptions
    "Address, phone number, and/or e-mail address": "pii_field--contact",
    "Confidential government identification numbers": "pii_field--govt",
    "Bank account or credit card number": "pii_field--bank",
    "Images of a handwritten signature or an ID doc": "pii_field--signature",
    "Highly personal, restricted, and official records": "pii_field--medical",
    "Confidential login credentials": "pii_field--login"
}

def wait_for_element(context, element_locator, by=By.CSS_SELECTOR, timeout=10):
    """
    Wait for an element to become visible and interactable on the page.
    """
    WebDriverWait(context.browser, timeout).until(
        EC.visibility_of_element_located((by, element_locator))
    )

@given('I am on the data store site\'s removal page')
def step_impl(context: Context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://support.google.com/websearch/answer/9673730")

@then('I click the "Start removal request" link')
def step_impl(context: Context):
    button = context.browser.find_element(By.LINK_TEXT, "Start removal request")
    button.click()

@then('I click the "Next" button')
def step_impl(context):
    next_button = context.browser.find_element(By.XPATH, "//button[contains(@class, 'next-button') and text()='Next']")
    next_button.click()

@then('I select "{description}"')
def step_impl(context, description):
    radio_id = radio_button_ids[description]  # Get the id from the description
    wait_for_element(context, f"label[for='{radio_id}']")
    radio_label = context.browser.find_element(By.CSS_SELECTOR, f"label[for='{radio_id}']")
    radio_label.click()

@then('I pause on a page for "{seconds}" seconds')
def step_impl(context, seconds):
    time.sleep(int(seconds))
