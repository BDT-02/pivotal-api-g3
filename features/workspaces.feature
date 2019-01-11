Feature: showing off behave

  Scenario: Create new workspace
    Given I create workspaces

        | name |
    Then I verify workspaces creation status is 200
    And I verify workspaces schema


    Scenario: Get workspace
    Given I create a workspace
      | name            |
      | Test Workspace
    When I get a workspace
#    Then I verify workspace get status is 200
    And I verify workspace schema


  Scenario: Update the workspace
    Given I create a workspace
    | name          |
     | First workspace |
    When I update the workspace
     | name           |
    | Update workspace |
    Then I verify workspace updated status is 200
    And I verify workspace schema

  Scenario: Delete the workspace
   Given I create a workspace
    | name          |
    | First workspace |
    When I delete the workspace
    Then I verify workspace deleted status is 204