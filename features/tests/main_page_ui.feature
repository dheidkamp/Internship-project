# Created by dheid at 8/12/2023
Feature: Tests for main page UI

  Scenario: Verify that footer has correct amount of links
    Given Open Amazon page
    Then Verify footer has 35 links

  Scenario: Verify that footer has many links
    Given Open Amazon page
    Then Verify many links shown in the footer