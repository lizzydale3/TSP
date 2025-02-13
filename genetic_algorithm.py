import random

class GeneticAlgorithm:
    def __init__(self, city_map, pop_size=20, mutation_rate=0.1, generations=100):
        """Manages population, evolution, and optimization."""
        self.city_map = city_map  # Reference to CityMap
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.population = self._generate_initial_population()

    def _generate_initial_population(self):
        """Generates an initial population where A is fixed at start & end."""
        population = []
        other_cities = self.city_map.cities[1:]  # Exclude "A"
        for _ in range(self.pop_size):
            shuffled_cities = random.sample(other_cities, len(other_cities))
            tour = ["A"] + shuffled_cities + ["A"]
            population.append(tour)
        return population

    def _fitness(self, tour):
        """Computes the total distance of a tour."""
        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += self.city_map.distance_matrix[tour[i]][tour[i+1]]
        return total_distance

    def _tournament_selection(self, k=3):
        """Selects parents using tournament selection."""
        selected_parents = []
        while len(selected_parents) < self.pop_size:
            tournament = random.sample(self.population, k)
            best_tour = min(tournament, key=self._fitness)
            selected_parents.append(best_tour)
        return selected_parents

    def _crossover(self, parent1, parent2):
        """Order Crossover (OX) while keeping A fixed at start and end."""
        size = len(parent1)
        start, end = sorted(random.sample(range(1, size - 1), 2))

        child = ["-"] * size
        child[0], child[-1] = "A", "A"
        child[start:end] = parent1[start:end]

        p2_remaining = [city for city in parent2 if city not in child]
        index = 1
        for city in p2_remaining:
            while child[index] != "-":
                index += 1
            child[index] = city
        return child

    def _mutate(self, tour):
        """Performs swap mutation while ensuring A stays fixed."""
        if random.random() < self.mutation_rate:
            idx1, idx2 = random.sample(range(1, len(tour) - 1), 2)
            tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
        return tour
    
    def _evolve(self):
        """Runs the Genetic Algorithm evolution for multiple generations."""
        best_tour = None
        best_distance = float("inf")

        for generation in range(self.generations):
            # Step 1: Selection - Choose the best parents
            selected_parents = self._tournament_selection()

            # Step 2: Crossover - Generate new children
            new_population = []
            for i in range(0, self.pop_size, 2):
                parent1 = selected_parents[i]
                parent2 = selected_parents[(i + 1) % self.pop_size]  # Wrap around

                # Create two children
                child1 = self._crossover(parent1, parent2)
                child2 = self._crossover(parent2, parent1)

                new_population.extend([child1, child2])

            # Step 3: Mutation - Randomly swap elements in tours
            new_population = [self._mutate(tour) for tour in new_population]

            # Step 4: Replacement - The new generation replaces the old population
            self.population = new_population

            # Step 5: Track the best tour
            current_best = min(self.population, key=self._fitness)
            current_best_distance = self._fitness(current_best)

            if current_best_distance < best_distance:
                best_tour = current_best
                best_distance = current_best_distance

        return best_tour, best_distance
    
    def run(self):
            """Runs the GA and saves the best result to a file."""
            best_tour, best_distance = self._evolve()
            formatted_tour = " -> ".join(best_tour)
            result = f"Shortest distance: {best_distance:.2f} miles\nSequence: {formatted_tour}"

            print(result)

            try:
                with open("tsp_results.txt", "w") as file:
                    file.write(result)
                print("Results saved to tsp_results.txt")
            except IOError:
                print("Could not save results.")