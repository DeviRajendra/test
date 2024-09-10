import os

# Paths for two different repositories
REPO_1_SCENARIO_RUNNER = "/path/to/repo1/scenario_runner"
REPO_1_LEADERBOARD = "/path/to/repo1/leaderboard"

REPO_2_SCENARIO_RUNNER = "/path/to/repo2/scenario_runner"
REPO_2_LEADERBOARD = "/path/to/repo2/leaderboard"

# Function to dynamically print export commands for the selected repository
def print_export_commands(scenario_runner_path, leaderboard_path):
    print(f'export SCENARIO_RUNNER_PATH={scenario_runner_path}')
    print(f'export LEADERBOARD_PATH={leaderboard_path}')

# Function to switch between repositories
def switch_repo(repo_number):
    if repo_number == 1:
        print_export_commands(REPO_1_SCENARIO_RUNNER, REPO_1_LEADERBOARD)
    elif repo_number == 2:
        print_export_commands(REPO_2_SCENARIO_RUNNER, REPO_2_LEADERBOARD)
    else:
        print("Invalid repository number. Please choose 1 or 2.")

if __name__ == "__main__":
    repo_number = int(input("Enter repository number (1 or 2): "))
    switch_repo(repo_number)

#To run
source <(python switch_paths.py)


To 
