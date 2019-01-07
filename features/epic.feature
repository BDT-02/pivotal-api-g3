Feature: showing off behave

  Scenario: Update epic
    Given I update an epic
        | name | First Project|
    Then I verify epic creation status is 200
    And I verify epic schema