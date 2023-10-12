# Created by dheid at 8/3/2023
Feature: Tests for amazon search

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for table
    Then Verify search result is "table"
#
#    Scenario: Verify that a user can search for a cup
#    Given Open Amazon page
#    When Search for cup
#    Then Verify search result is "cup"

  Scenario: Verify that clicking Orders takes to signin
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened

  Scenario Outline: Verify that a user can search for a cup
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search result is <search_result>
    Examples:
    |search_word    |search_result  |
    |cup            |"cup"          |
    |table          |"table"        |