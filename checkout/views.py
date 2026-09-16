from django.http import JsonResponse
from django.views import View


class HealthView(View):
    def get(self, request):
        return JsonResponse({
            "status": "ok",
            "service": "Winterberry Paper Co. Meta Checkout"
        })


class CheckoutView(View):
    def get(self, request):
        products_param = request.GET.get("products", "")
        coupon = request.GET.get("coupon")

        product_quantities = {}

        if products_param:
            for entry in products_param.split(","):
                try:
                    product_id, quantity = entry.split(":", 1)
                    quantity = int(quantity)

                    if product_id and quantity > 0:
                        product_quantities[product_id] = quantity
                except (ValueError, TypeError):
                    continue

        return JsonResponse({
            "products": product_quantities,
            "coupon": coupon if coupon else "No coupon applied",
        })
