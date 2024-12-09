from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, When, Then


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
    
@Then('text should be "{expected_text}"')
def step_impl(context, expected_text):
    slogan = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Test']"))
    )
    actual_text = slogan.text
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
    
#-------------
@Then('I select a diffrent shift ammount')
def step_impl(context):
    select_element = context.driver.find_element(By.ID, "shift-amount")
    select = Select(select_element)
    select.select_by_value("5") 
    
    
@Then('result should be "{expected_text}"')
def step_impl(context, expected_text):
    slogan = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Yjxy']"))
    )
    actual_text = slogan.text
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
    
@Then('I select a diffrent encoding')
def step_impl(context):
    select_element = context.driver.find_element(By.ID, "decoder-setting")
    select = Select(select_element)
    select.select_by_value("D")
    
@Then('output should be "{expected_text}"')
def step_impl(context, expected_text):
    slogan = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='Ozno']"))
    )
    actual_text = slogan.text
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
     
     
@When("I select the input prompt and input 1234")
def step_impl(context):
    prompt = context.driver.find_element(By.ID, "letters")
    prompt.click()
    prompt.send_keys("1234")
    
@Then('the number output be "{expected_text}"')
def step_impl(context, expected_text):
    slogan = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='1234']"))
    )
    actual_text = slogan.text
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
     
    
    
