"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    output = []
    with open(neo_csv_path) as f:
        reader = csv.reader(f)
        headers = next(reader)
        index_pdes = headers.index("pdes")
        index_name = headers.index("name")
        index_pha = headers.index("pha")
        index_diameter = headers.index("diameter")

        for line in reader:
            args = (
                line[index_pdes],
                line[index_name],
                line[index_pha],
                line[index_diameter],
            )
            neo_obj = NearEarthObject(*args)
            output.append(neo_obj)

    return output


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    output_collection = []
    with open(cad_json_path) as f:
        data = json.load(f)
        headers = data["fields"]
        index_des = headers.index("des")
        index_cd = headers.index("cd")
        index_dist = headers.index("dist")
        index_v_rel = headers.index("v_rel")
        for line in data["data"]:
            args = line[index_des], line[index_cd], line[index_dist], line[index_v_rel]
            approach_obj = CloseApproach(*args)
            output_collection.append(approach_obj)

    return output_collection
