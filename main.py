TITLES = [
    'Tournaments',
    'ABI',
    'Profit',
    'Ability',
    'TOT ROI',
    'AV ROI',
    'Early Finish',
    'Late Finish',
    'Games/Day',
    'ITM %',
    'AV Entrants',
    'AV Profit',
    'Turbo %',
    'Entries',
]


def get_data():
    data_str = input('Enter the data: ')
    while '\t' in data_str:
        data_str = data_str.replace('\t', ' ')
    data_str = data_str.rstrip()
    data_str = data_str.lstrip()
    while '  ' in data_str:
        data_str = data_str.replace('  ', ' ')
    data_list = data_str.split(' ')
    return data_list


def show_sorted_data():
    data = get_data()
    sorted_data = zip(TITLES, data)
    return list(sorted_data)


def main():
    sorted_data = show_sorted_data()
    print(f'\nSorted data:\n')
    for i in range(len(sorted_data)):
        print(f'{sorted_data[i][0]}: {sorted_data[i][1]}', end=' ')


if __name__ == '__main__':
    main()
