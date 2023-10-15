# Created by dheid at 10/13/2023
Feature: Tests for Registration Page


  Scenario: The user can enter information into the input fields on the registration page
    Given Open the registration page
    When Enter some test information in the input fields
    Then Verify the right information is present