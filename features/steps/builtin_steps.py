from behave_webdriver.steps import * # ignore
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on the home page')
def step_impl(context):
    context.driver.get("https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder")
    
@When("I clear the letters")
def step_impl(context):
    reset = context.driver.find_element(By.ID, "reset")
    reset.click()
    
@When("I select the input prompt and input testing")
def step_impl(context):
    prompt = context.driver.find_element(By.ID, "letters")
    prompt.click()
    prompt.send_keys("Test")
    
@Then("I hit translate")
def step_impl(context):
    Button = context.driver.find_element(By.ID, "submit")
    Button.click()
    
@then('text should be "{expected_text}"')
def step_impl(context, expected_text):
    slogan = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Test']"))
    )
    actual_text = slogan.text
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
    
    
@When("I select the input and give nothing")
def step_impl(context):
    prompt = context.driver.find_element(By.ID, "letters")
    prompt.click()
    prompt.send_keys(" ")
    
@then('it should only be "{expected_text}"')
def step_impl(context, expected_text):
    slogan = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Message After Shift']"))
    )
    actual_text = slogan.text
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
    