from django.http import HttpResponse


def create_report(ingredients):
    shopping_cart = ['Список покупок:\n--------------']
    for position, ingredient in enumerate(ingredients, start=1):
        shopping_cart.append(
            f'\n{position}. {ingredient["ingredient__name"]}:'
            f' {ingredient["amount"]}'
            f'({ingredient["ingredient__measurement_unit"]})'
        )
        response = HttpResponse(shopping_cart, content_type='text')
        response['Content-Disposition'] = (
            'attachment;filename=shopping_cart.pdf'
        )
    return response
