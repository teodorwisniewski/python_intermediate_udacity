import json
from pprint import pprint
import helper


def load_nobel_prizes(filename='prize.json'):
    with open(filename, 'r') as f:
        content = json.load(f)
    return content['prizes']


def main(year, category):
    data = load_nobel_prizes()
    # Add more here!
    if year is None and category is None:
        pprint(data)
    elif category is None:
        for prize in data:
            if prize['year'] == str(year):
                pprint(prize)
    else:
        category = category.lower()
        for prize in data:
            if prize['year'] == str(year) and prize['category'] == category:
                pprint(prize)
                break


if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)
    # main(None, None)
    # main(2020, None)
    # main(1980, 'physics')

