"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
import datetime


def write_to_csv(results, filename):
    """
    Write an iterable of `CloseApproach` objects to a CSV file.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        "datetime_utc",
        "distance_au",
        "velocity_km_s",
        "designation",
        "name",
        "diameter_km",
        "potentially_hazardous",
    )
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for close_app_obj in results:
            time = close_app_obj.time.strftime("%Y-%m-%d %H:%M")
            distance, velocity = close_app_obj.distance, close_app_obj.velocity
            neo_obj = close_app_obj.neo
            designation, name = neo_obj.designation, neo_obj.name
            diameter_km, potentially_hazardous = neo_obj.diameter, neo_obj.hazardous
            row = [
                time,
                distance,
                velocity,
                designation,
                name,
                diameter_km,
                potentially_hazardous,
            ]
            writer.writerow(row)


def write_to_json(results, filename):
    """
    Write an iterable of `CloseApproach` objects to a JSON file.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        "datetime_utc",
        "distance_au",
        "velocity_km_s",
        "designation",
        "name",
        "diameter_km",
        "potentially_hazardous",
    )
    data = []
    for close_app_obj in results:
        time = close_app_obj.time.strftime("%Y-%m-%d %H:%M")
        distance, velocity = close_app_obj.distance, close_app_obj.velocity
        neo_obj = close_app_obj.neo
        designation, name = neo_obj.designation, neo_obj.name
        diameter_km, potentially_hazardous = neo_obj.diameter, neo_obj.hazardous
        one_record = {
            "datetime_utc": time,
            "distance_au": distance,
            "velocity_km_s": velocity,
            "neo": {
                "designation": designation,
                "name": name,
                "diameter_km": diameter_km,
                "potentially_hazardous": potentially_hazardous,
            },
        }
        data.append(one_record)

    with open(filename, "w") as outfile:
        json.dump(data, outfile, indent=2)
