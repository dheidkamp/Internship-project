# Created by dheid at 8/7/2023
Feature: Test for Amazon Sign In

  Scenario: Verify that logged out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When Click on Orders
#    Then Verify Sign in page opened, Sign in header is visible, and email input field is present

  Scenario: Verify that Amazon cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify Amazon cart is empty
