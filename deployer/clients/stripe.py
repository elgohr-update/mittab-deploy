import os

import stripe

__publishable_key = os.environ['STRIPE_PUBLISHABLE_KEY']
__secret_key = os.environ['STRIPE_SECRET_KEY']

stripe.api_key = __secret_key

DAILY_COST_TEST_TOURNAMENT = 100
DAILY_COST                 = 100

def get_publishable_key():
    return __publishable_key

def charge(email, stripe_token, amount):
    try:
        customer = stripe.Customer.create(
            email=email,
            source=stripe_token
        )

        stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='usd',
            description='MIT-Tab Server',
            receipt_email=email
        )
        return True
    except stripe.error.StripeError as e:
        print("Got error %s" % e)
        import traceback; traceback.print_exc()
        return False
