Feature: showing off behave

  @delete_project @delete_epics
  Scenario: Create new epic
    Given I create a project
      | name          |
      | New Project for New Epic Scenario |
    When I create a epic
      | label      |
      | New Epic Created |
    Then I verify epic created status is 200
    And I verify epic schema


  @delete_project @delete_epics
  Scenario: Update the epic
    Given I create a project
      | name          |
      | New Project for Update Epic Scenario |
    And I create a epic
      | label      |
      | New Epic For update scenario |
    When I update a epic
      | label             |
      | Epic Updated |
    Then I verify epic updated status is 200
    And I verify epic schema

  @delete_project
  Scenario: Delete the epic
    Given I create a project
      | name          |
      | New Project for Delete Scenario |
    And I create a epic
      | label      |
      | New Epic for delete |
    When I delete the epic
    Then I verify epic updated status is 204