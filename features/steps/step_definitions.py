from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave.runner import Context
from behave import *

import time
import json

from openai import OpenAI
client = OpenAI()


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

BASE_URL = "https://support.google.com/websearch/answer/9673730"

def wait_for_element(context, element_locator, by=By.CSS_SELECTOR, timeout=10):
    """
    Wait for an element to become visible and interactable on the page.
    """
    WebDriverWait(context.browser, timeout).until(
        EC.visibility_of_element_located((by, element_locator))
    )

def send_html_to_chatgpt(html_content):
    """
    Sends HTML content to ChatGPT and returns IDs or instructions.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a web developer and you have been given a task to parse an HTML document and return new radio button IDs."},
            {"role": "user", "content": html_content}
        ]
    )

    return response.model_dump_json()

def update_radio_button_ids(file_path, new_ids):
    """
    Function to update radio button IDs from the response file.
    """
    with open(file_path, 'w') as file:
        json.dump(new_ids, file)

@then('I extract and send the HTML to ChatGPT')
def step_impl(context):
    html_content = context.browser.page_source
    response = send_html_to_chatgpt(html_content)
    # Assuming response contains new IDs
    context.new_ids = response['choices'][0]['text']

@then('I save the new radio IDs into a file')
def step_impl(context):
    update_radio_button_ids('new_radio_ids.json', context.new_ids)

@then('I return to the initial data removal page')
def step_impl(context):
    context.browser.get(BASE_URL)
    time.sleep(2)

@given('I am on the Google data store site\'s removal page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get(BASE_URL)

@when('I click the "Start removal request" link')
def step_impl(context):
    start_link = context.browser.find_element(By.LINK_TEXT, "Start removal request")
    start_link.click()

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
