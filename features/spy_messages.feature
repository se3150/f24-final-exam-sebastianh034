Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I input a new message
    Given I am on the home page
    When I clear the letters
    When I select the input prompt and input testing
    Then I hit translate
    Then text should be "Test"

Scenario: I input nothing
    Given I am on the home page
    When I clear the letters
    When I select the input and give nothing
    Then I hit translate
    Then it should only be "Message After Shift"
