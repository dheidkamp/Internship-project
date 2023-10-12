from behave import given, when, then


@then('Verify Sign in page opened')
def verify_signin_opened_step(context):
    context.app.signin_page.verify_signin_opened()

