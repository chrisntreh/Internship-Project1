# Created by chris at 7/16/2025
Feature: # Access main page
  # User can filter deals wants to buy

#  Scenario: User can filter the Secondary deals by “want to buy” option
#    Given the user Open Relly main page
#    When user signs in
#    When user Click on the Secondary to the left
#    When verify the right page opens
#    When user click on filters
#    Then filter the products by want_to_buy
#    When user click on apply filter
#    Then Verify all cards have a want_to_buy tag

  Scenario: User can filter the Secondary deals by “want to buy” option - Mobile
    Given the user Open Relly main page
    When user signs in
    When user Click off_plan on bottom left
    When user Click on the Secondary to the left
    When verify the right page opens
    When user click on filters
    Then filter the products by want_to_buy
    When user click on apply filter
    Then Verify all cards have a want_to_buy tag






