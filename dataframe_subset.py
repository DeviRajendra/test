import pandas as pd

def collect_subset_with_same_distribution(df, column, subset_length):
    # Group the DataFrame by the specified column
    grouped = df.groupby(column)
    
    # Initialize an empty list to store sampled subsets
    subsets = []
    
    # Iterate over each group
    for _, group in grouped:
        # Sample subset_length records from each group
        subset = group.sample(min(len(group), subset_length))
        # Add the subset to the list
        subsets.append(subset)
    
    # Concatenate the sampled subsets to form the final subset DataFrame
    final_subset = pd.concat(subsets)
    
    return final_subset

# Example usage:
# Assuming df is your DataFrame and 'specific_column' is the column you want to maintain distribution for
# and subset_length is the desired length of the subset
final_subset = collect_subset_with_same_distribution(df, 'specific_column', subset_length)
