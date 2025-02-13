import csv
from city_map import CityMap
from genetic_algorithm import GeneticAlgorithm

def run_single_experiment():
    """Runs the GA once and saves the best result to `tsp_results.txt`."""
    cities_dict = {
        "A": (100, 300),
        "B": (200, 130),
        "C": (300, 500),
        "D": (500, 390),
        "E": (700, 300),
        "F": (900, 600),
        "G": (800, 950),
        "H": (600, 560),
        "I": (350, 550),
        "J": (270, 350)
    }

    city_map = CityMap(cities_dict)

    # Default parameters for submission
    mutation_rate = 0.1
    pop_size = 50
    generations = 100

    ga = GeneticAlgorithm(city_map, pop_size=pop_size, generations=generations, mutation_rate=mutation_rate)
    best_tour, best_distance = ga._evolve()
    formatted_tour = " -> ".join(best_tour)
    result = f"Shortest distance: {best_distance:.2f} miles\nSequence: {formatted_tour}\n"

    # Print result for verification
    print(result)

    # Save to text file (for submission)
    with open("tsp_results.txt", "w") as file:
        file.write(result)

    print("Best result saved to tsp_results.txt (for submission).")

def run_multiple_experiments():
    """Runs multiple experiments with different GA parameters for comparison."""
    cities_dict = {
        "A": (100, 300),
        "B": (200, 130),
        "C": (300, 500),
        "D": (500, 390),
        "E": (700, 300),
        "F": (900, 600),
        "G": (800, 950),
        "H": (600, 560),
        "I": (350, 550),
        "J": (270, 350)
    }

    city_map = CityMap(cities_dict)

    # Experiment variations: (mutation_rate, pop_size, generations)
    experiments = [
        (0.05, 50, 100),
        (0.1, 50, 100),
        (0.3, 50, 100),
        (0.1, 100, 100),
        (0.1, 50, 500),
    ]

    results = []

    print("\n Running multiple experiments...")
    
    for mutation_rate, pop_size, generations in experiments:
        ga = GeneticAlgorithm(city_map, pop_size=pop_size, generations=generations, mutation_rate=mutation_rate)
        best_tour, best_distance = ga._evolve()
        formatted_tour = " -> ".join(best_tour)

        results.append([mutation_rate, pop_size, generations, best_distance, formatted_tour])
        print(f"Mutation: {mutation_rate}, Pop: {pop_size}, Gen: {generations} → {best_distance:.2f} miles")

    # Save results to CSV for easy review
    with open("tsp_experiment_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Mutation Rate", "Population Size", "Generations", "Best Distance", "Best Tour"])
        writer.writerows(results)

    print("All results saved to tsp_experiment_results.csv.")

if __name__ == "__main__":
    print("\nChoose an option:")
    print("1️ Run single experiment (for class submission - saves to tsp_results.txt)")
    print("2️ Run multiple experiments (compare different parameters)")
    
    choice = input("\nEnter 1 or 2: ")

    if choice == "1":
        run_single_experiment()
    elif choice == "2":
        run_multiple_experiments()
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")
