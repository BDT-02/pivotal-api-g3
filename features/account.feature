Feature: showing off behave

  Scenario: Create new account
    Given I create an account
        | name |
        | APIIIIIII|

    Then I verify account creation status is 200
    And I verify account schema