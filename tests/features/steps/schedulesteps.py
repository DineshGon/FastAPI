# from behave import given, when, then, step
# import requests
import pytest
from pytest_bdd import scenarios, given, when, then, parser


scenarios('./features/schedule.feature')

@given("with the {int} is starting at {string} and {string} is entered")
def step_impl(context, appointmentId, startTime, endTime):
    pass


@when("the appointment is scheduled")
def when_impls():
    pass


@then("Success is reported ")
def then_succ():
    pass
