import csv
import json

import argparse


def build_parser():
    """Create a parser to parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Find flight paths between two airlines")
    parser.add_argument('source', help="The source airport's IATA (3-letter) code.")
    parser.add_argument('dest', help="The destination airport's IATA (3-letter) code.")
    parser.add_argument('--max-segments', dest='max_segments', type=int, default=2,
                        help="The maximum number of segments in a valid path.")
    return parser


def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines


def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    airports = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]
    return airports


def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = {}  # Map from code -> name
    with open(filename) as f:
        reader = csv.reader(f)
        for line in reader:
            source, destination = line[2], line[4]
            if source not in routes:
                routes[source] = []
            routes[source].append(destination)
    return routes


def find_paths(routes, source, dest, max_segments):
    # Run the BFS search
    frontier = {source}
    seen = {source: {(source, )}}
    for steps in range(max_segments):
        next_frontier = set()
        for airport in frontier:
            for target in routes.get(airport, ()):
                if target not in seen:
                    next_frontier.add(target)
                    seen[target] = set()
                for path in seen[airport]:
                    if len(path) != steps + 1:
                        continue
                    seen[target].add(path + (target, ))
        frontier = next_frontier
    return seen[dest]

def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Again, could use a collections.defaultdict(list) here.
    for path in paths:
        segments = len(path) - 1
        if segments not in output:
            output[segments] = []
        output[segments].append(rename_path(path, airports))

    with open(f"{source}->{dest} (max {max_segments}).json", 'w') as f:
        json.dump(output, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    # parser = helper.build_parser()
    # args = parser.parse_args()
    #
    # main(args.source, args.dest, args.max_segments)
    main("SFO", "BOS", 2)