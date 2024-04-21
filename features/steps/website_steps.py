from behave import *
import json

# Define your interactable elements list
INTERACTABLE_ELEMENTS = [
    "button", "a", "input", "select", "option", "datalist", 
    "label", "fieldset", "legend", "map", "area", "output", "progress", 
    "meter", "summary", "details", "form"
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
        visible_elements = [element for element in elements if element.is_visible()]
        elements_data[tag] = [element.inner_html() for element in visible_elements]


    with open("start_removeal.json", 'w') as f:
        json.dump(elements_data, f, indent=4)
