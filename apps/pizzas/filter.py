from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.pizzas.models import PizzaModel


def filter_pizzas(query: QueryDict) -> QueryDict:
    qs = PizzaModel.objects.all()

    # sort
    sort_param = query.get('sort')
    print(sort_param)
    if sort_param:
        sort_fields = sort_param.split(',')
        qs = qs.order_by(*sort_fields)

    for k, v in query.items():
        if k == 'sort':
            continue # Skip the 'sort' parameter since we've already processed it
        match k:
            # price
            case 'price__gt':
                qs = qs.filter(price__gt=v)
            case 'price__lt':
                qs = qs.filter(price__lt=v)
            case 'price__gte':
                qs = qs.filter(price__gte=v)
            case 'price__lte':
                qs = qs.filter(price__lte=v)
            # weight
            case 'weight__lt':
                qs = qs.filter(weight__lt=v)
            case 'weight__gt':
                qs = qs.filter(weight__gt=v)
            case 'weight__gte':
                qs = qs.filter(weight__gte=v)
            case 'weight__lte':
                qs = qs.filter(weight__lte=v)
            # description
            case 'description__iendswith':
                qs = qs.filter(description__iendswith=v)
            case 'description__istartswith':
                qs = qs.filter(description__istartswith=v)
            case 'description__icontains':
                qs = qs.filter(description__icontains=v)
            # name
            case 'name__iendswith':
                qs = qs.filter(name__iendswith=v)
            case 'name__istartswith':
                qs = qs.filter(name__istartswith=v)
            case 'name__icontains':
                qs = qs.filter(name__icontains=v)
            case _:
                raise ValidationError(f'{k} not allowed')

    return qs
