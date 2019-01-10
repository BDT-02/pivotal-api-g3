Feature: showing off behave
  @delete_project
  Scenario: Create new project
    Given I create a project
        | name |
  First Project|
    Then I verify project creation status is 200
    And I verify project schema

      @delete_project
  Scenario: Update the project
    Given I create a project
      | name          |
      | First Project |
    When I update the project
      | name           |
      | Update Project |
    Then I verify project updated status is 200
    And I verify project schema


  Scenario: Delete the project
    Given I create a project
      | name          |
      | First Project |
    When I delete the project
    Then I verify project deleted status is 204