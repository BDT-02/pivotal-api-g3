Feature: showing off behave

  Scenario: Create new workspace
    Given I create workspaces

        | name |
    Then I verify workspaces creation status is 200
    And I verify workspaces schema