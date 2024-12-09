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

Scenario: I select a shift ammount
    Given I am on the home page
    When I clear the letters
    Then I select a diffrent shift ammount
    When I select the input prompt and input testing
    Then I hit translate
    Then result should be "Yjxy"

Scenario: I decode a message
    Given I am on the home page
    Then I select a diffrent encoding
    When I clear the letters
    Then I select a diffrent shift ammount
    When I select the input prompt and input testing
    Then I hit translate
    Then output should be "Ozno"

Scenario: I input numbers
    Given I am on the home page
    When I clear the letters
    Then I select a diffrent shift ammount
    When I select the input prompt and input 1234
    Then I hit translate
    Then the number output be "1234"




