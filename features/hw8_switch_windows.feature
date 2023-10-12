# Created by dheid at 9/27/2023
Feature: Test for switching windows


 Scenario: User can open and close Amazon Privacy Notice
  Given Open Amazon T&C page
  And Store original windows
  When Click on Amazon Privacy Notice link
  And Switch to the newly opened window
  Then Verify Amazon Privacy Notice page is opened
  And User can close new window
  Then User can switch back to original window





