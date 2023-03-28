from django.db.models import Max
# from .models import Title

SEPARATOR = ' | '


def transfigurate(input_data, titles):
    data_str = input_data
    titles = titles
    while '\t' in data_str:
        data_str = data_str.replace('\t', ' ')
    data_str = data_str.rstrip()
    data_str = data_str.lstrip()
    while '  ' in data_str:
        data_str = data_str.replace('  ', ' ')
    data_list = data_str.split(' ')
    output_data = zip(titles, data_list)
    return list(output_data)


def set_default_priority(model):
    titles = model.objects.filter(priority__gte=1)
    if titles:
        title_lowest_priority = titles.aggregate(Max('priority'))
        lowest_priority = title_lowest_priority['priority__max']
        default_priority = lowest_priority + 1
    else:
        default_priority = 1
    return default_priority
