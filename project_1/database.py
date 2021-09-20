"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""
import operator


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches

        self.mapping_neo_desingation = {}
        self.mapping_neo_name = {}
        for i, neo in enumerate(neos):
            self.mapping_neo_desingation[neo.designation] = i
            self.mapping_neo_name[neo.name] = i
            for approach in approaches:
                if neo.designation == approach._designation:
                    neo.approaches.append(approach)
                    approach.neo = neo

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        res = None
        index = self.mapping_neo_desingation.get(designation, None)
        if index is not None:
            res = self._neos[index]
        return res

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        res = None
        index = self.mapping_neo_name.get(name, None)
        if index is not None:
            res = self._neos[index]
        return res

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaningfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        if all([None is val for val in filters.values()]):
            for approach in self._approaches:
                yield approach
        else:
            output_subset = set()
            subset_date = set()
            subset_start_date = set()
            subset_end_date = set()
            subset_distance_min = set()
            subset_distance_max = set()
            subset_diameter_min = set()
            subset_diameter_max = set()
            subset_velocity_min = set()
            subset_velocity_max = set()
            subset_hazardous = set()

            def get_specific_approaches(approches, attributes_to_extract, value, op):
                """Get a set of filtered Approach objects.

                This function allows to extract specific attribute's value and compare it
                to the given value and return a set of unique Approach objects

                :param approches: itarable of Aproches objects
                :param attributes_to_extract: attributes that we want to extract
                :param value: value to which we compare
                :param op: operator for instance ==, =>, etc.
                :return: a set of unique Approach objects
                """
                output_set = set()
                for approach in approches:
                    obj_attr = approach
                    for att_name, att_type in attributes_to_extract:
                        if att_type == "attribute":
                            obj_attr = getattr(obj_attr, att_name)
                        else:
                            obj_attr = getattr(obj_attr, att_name)()
                    if op(obj_attr, value):
                        output_set.add(approach)
                return output_set

            for criteria, val in filters.items():
                if val is None:
                    continue
                if criteria == "date":
                    subset_date = get_specific_approaches(
                        self._approaches,
                        [("time", "attribute"), ("date", "method")],
                        val,
                        operator.eq,
                    )
                elif criteria == "start_date":
                    subset_start_date = get_specific_approaches(
                        self._approaches,
                        [("time", "attribute"), ("date", "method")],
                        val,
                        operator.ge,
                    )
                elif criteria == "end_date":
                    subset_end_date = get_specific_approaches(
                        self._approaches,
                        [("time", "attribute"), ("date", "method")],
                        val,
                        operator.le,
                    )
                elif criteria == "distance_min":
                    subset_distance_min = get_specific_approaches(
                        self._approaches, [("distance", "attribute")], val, operator.ge
                    )
                elif criteria == "distance_max":
                    subset_distance_max = get_specific_approaches(
                        self._approaches, [("distance", "attribute")], val, operator.le
                    )
                elif criteria == "velocity_min":
                    subset_velocity_min = get_specific_approaches(
                        self._approaches, [("velocity", "attribute")], val, operator.ge
                    )
                elif criteria == "velocity_max":
                    subset_velocity_max = get_specific_approaches(
                        self._approaches, [("velocity", "attribute")], val, operator.le
                    )
                elif criteria == "diameter_min":
                    subset_diameter_min = get_specific_approaches(
                        self._approaches,
                        [("neo", "attribute"), ("diameter", "attribute")],
                        val,
                        operator.ge,
                    )
                elif criteria == "diameter_max":
                    subset_diameter_max = get_specific_approaches(
                        self._approaches,
                        [("neo", "attribute"), ("diameter", "attribute")],
                        val,
                        operator.le,
                    )

                elif criteria == "hazardous":
                    subset_hazardous = get_specific_approaches(
                        self._approaches,
                        [("neo", "attribute"), ("hazardous", "attribute")],
                        val,
                        operator.eq,
                    )
            all_subsets = (
                subset_date,
                subset_start_date,
                subset_end_date,
                subset_distance_min,
                subset_distance_max,
                subset_diameter_min,
                subset_diameter_max,
                subset_velocity_min,
                subset_velocity_max,
                subset_hazardous,
            )
            non_empty_subsets = [subset for subset in all_subsets if len(subset) > 0]
            if len(non_empty_subsets) > 1:
                output_subset = non_empty_subsets[0].intersection(
                    *non_empty_subsets[1:]
                )
            else:
                output_subset = non_empty_subsets[0]
            for approach in output_subset:
                yield approach
