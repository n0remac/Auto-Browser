from selenium import webdriver
from selenium.webdriver.common.by import By
from behave.runner import Context
from behave import *

import time

@given('I am on the data store site\'s removal page')
def step_impl(context: Context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://support.google.com/websearch/answer/9673730")
    time.sleep(2)

@when('I pause on a page for "{seconds}" seconds')
def step_impl(context, seconds):
    time.sleep(int(seconds))

@then('I click the "Start removal request" button')
def step_impl(context: Context):
    button = context.browser.find_element(By.LINK_TEXT, "Start removal request")
    button.click()

@when('I enter the name "{name}" and message "{message}"')
def step_impl(context, name, message):
    name_input = context.browser.find_element_by_id("name")
    message_input = context.browser.find_element_by_id("message")
    name_input.send_keys(name)
    message_input.send_keys(message)

@when('I submit the request')
def step_impl(context):
    submit_button = context.browser.find_element_by_id("submit")
    submit_button.click()

@then('I should see a confirmation message')
def step_impl(context):
    confirmation = context.browser.find_element_by_id("confirmation")
    assert "Your request has been received" in confirmation.text
    context.browser.quit()
