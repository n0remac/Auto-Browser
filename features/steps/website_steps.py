from behave import *
import json
# import ElementHandle


# Define your interactable elements list
INTERACTABLE_ELEMENTS = [
    "input"
]
MAIN_PAGE="https://support.google.com/websearch/answer/9673730"
@given('I am on the specified web page')
def step_impl(context):
    context.page.goto("https://support.google.com/websearch/contact/content_removal_form?sjid=11390557912768293651-NC")

@then('I scrape all interactive elements')
def step_impl(context):
    elements_data = {}
    for tag in INTERACTABLE_ELEMENTS:
        elements = context.page.query_selector_all(tag)
        elements_data[tag] = [element.get_attribute('id') for element in elements]

    with open("start_removeal.json", 'w') as f:
        json.dump(elements_data, f, indent=4)
