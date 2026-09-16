# Winterberry Paper Co. Meta Checkout Endpoint

Small Django web service for receiving Meta Commerce checkout parameters.

## Routes

- `/` — health/status response
- `/checkout/` — receives Meta's `products` and optional `coupon` query parameters

Example:

`/checkout/?products=4533278555:2,4533072418:1&coupon=SAVE10`

## Render settings

- Language: Python 3
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn meta_checkout.wsgi:application --bind 0.0.0.0:$PORT`

No external database is required for this endpoint.
