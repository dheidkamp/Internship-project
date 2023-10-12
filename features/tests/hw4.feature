# Created by dheid at 8/13/2023
Feature: Homework #4

  Scenario: Verify there are 5 links on Amazon BestSellers page
    Given Open Bestsellers page
    Then Verify there are 5 links

  Scenario: Verify product added to cart
  Given Open Amazon page
  When Search for notebook
  When Add item to cart
  Then Verify product added to cart
