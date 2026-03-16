from random import randint
import matplotlib.pyplot as plt

def generate_birthdays(k) -> tuple:
    """generate a tuple of k random birthdays."""

    return tuple(randint(1, 365) for _ in range(k))

def search_for_pair(birthdays) -> bool:
    """Check if there are any duplicate birthdays (a pair)."""
    seen = set()
    for birthday in birthdays:
        if birthday in seen:
            return True
        seen.add(birthday)
    return False

def run_simulation(n, k) -> int:
    """Run n simulations of the birthday problem with k people and return the number of times a pair was found."""
    count = 0
    for _ in range(n):
        birthdays = generate_birthdays(k)
        if search_for_pair(birthdays):
            count += 1
    return count

def main() -> None:
    n_values = [10, 100, 1000]  # Number of simulations
    k_values = list(range(1, 100))  # Number of people per simulation

    # for n in n_values:
    #     probabilities = []

    #     for k in k_values:
    #         c = run_simulation(n, k)
    #         prob = c / n
    #         probabilities.append(prob)

    #     plt.plot(k_values, probabilities, marker='o', label=f'n={n}')

    # plt.xlabel('Number of people (k)')
    # plt.ylabel('Probability of at least one shared birthday (c/n)')
    # plt.title('Birthday Paradox Simulation')
    # plt.grid(True)
    # plt.legend()
    # plt.savefig('birthday_paradox_plot.png')
    # plt.show()

    fig, axes = plt.subplots(len(n_values), 1, figsize=(8, 10), sharex=True)
    for i, n in enumerate(n_values):
        probabilities = []
        for k in k_values:
            c = run_simulation(n, k)
            prob = c / n
            probabilities.append(prob)
        axes[i].plot(k_values, probabilities, marker='o')
        axes[i].set_ylabel(f'Probability (n={n})')
        axes[i].axvline(x=23, color='red', linestyle='--', alpha=0.7)
        axes[i].axhline(y=0.5, color='green', linestyle='--', alpha=0.7)
        axes[i].grid(True)
    axes[-1].set_xlabel('Number of people (k)')
    plt.suptitle('Birthday Paradox Simulation')
    plt.tight_layout()
    plt.savefig('birthday_paradox_plot.png')
    plt.show()
    plt.show()

if __name__ == "__main__":
    main() 