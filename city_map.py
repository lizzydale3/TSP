import math

class CityMap:
    """Represents the map of cities and precomputes their distances."""

    def __init__(self, cities_dict):
        """
        Initializes the city map with:
        - `cities_dict`: Dictionary of city names and coordinates.
        - Precomputed distance matrix for quick lookup.
        """
        self.cities_dict = cities_dict
        self.cities = list(cities_dict.keys())  # Ordered list of city names
        self.distance_matrix = self._create_distance_matrix()  # Precomputed distances

    def _create_distance_matrix(self):
        """
        Computes the Euclidean distance between all city pairs.
        - Uses a dictionary of dictionaries for fast access.
        - Cities are treated as points in a 2D plane.
        """
        matrix = {}
        for city1 in self.cities:
            matrix[city1] = {}
            for city2 in self.cities:
                if city1 == city2:
                    matrix[city1][city2] = 0  # Distance to itself is 0
                else:
                    matrix[city1][city2] = self._euclidean_dist(city1, city2)
        return matrix

    def _euclidean_dist(self, city1, city2):
        """
        Calculates the Euclidean distance (straight-line distance) between two cities.
        - Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
        """
        x1, y1 = self.cities_dict[city1]
        x2, y2 = self.cities_dict[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
