import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

FILE_PATH = r"elections_data.csv"

def check_file_exists(file_path):

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Error: File not found at {file_path}")
    else:
        print("File Exist")
    return True

def read_election_data(file_path):

    try:
        df = pd.read_csv(file_path)
        print("\nFirst few rows of the data:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

def calculate_seat_percentages(df):

    try:
        # Calculate total seats per state
        total_seats_per_state = df.groupby('State')['Seats'].sum()
        
        # Calculate percentage for each party in each state
        df['Seats_Percentage'] = df.apply(
            lambda row: (row['Seats'] / total_seats_per_state[row['State']]) * 100, 
            axis=1
        )
        
        # Round to 2 decimal places
        df['Seats_Percentage'] = df['Seats_Percentage'].round(2)
        
        return df
    except Exception as e:
        print(f"Error calculating seat percentages: {e}")
        return None

def get_highest_seats_by_state(df):
    """Find party with highest seats in each state"""
    try:
        highest_seats = df.loc[df.groupby('State')['Seats'].idxmax()]
        highest_seats = highest_seats.sort_values('Seats', ascending=False)
        return highest_seats
    except Exception as e:
        print(f"Error finding highest seats by state: {e}")
        return None

def create_seat_distribution_plot(df):
    """Create bar chart for seat distribution"""
    try:
        plt.figure(figsize=(15, 8))
        sns.barplot(data=df, x='State', y='Seats', hue='Party')
        plt.title('Seat Distribution by Party Across States')
        plt.xlabel('State')
        plt.ylabel('Number of Seats')
        plt.xticks(rotation=45, ha='right')
        plt.legend(title='Party', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        
        # Save plot in the same directory as the input file
        output_path = Path(FILE_PATH).parent / 'seat_distribution.png'
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.close()
        print(f"\nBar chart has been saved as: {output_path}")
    except Exception as e:
        print(f"Error creating visualization: {e}")

def main():
    try:
        # Check if file exists
        check_file_exists(FILE_PATH)
        
        # Read the data
        df = read_election_data(FILE_PATH)
        if df is None:
            return
        
        # Calculate seat percentages
        df = calculate_seat_percentages(df)
        if df is None:
            return
            
        print("\nData with calculated seat percentages:")
        print(df.to_string())
        
        # Get parties with highest seats in each state
        highest_seats = get_highest_seats_by_state(df)
        if highest_seats is not None:
            print("\nParties with highest seats in each state:")
            print(highest_seats[['State', 'Party', 'Seats', 'Seats_Percentage']].to_string())
        
        # Create visualization
        create_seat_distribution_plot(df)
        
    except FileNotFoundError as e:
        print(e)
        print("File Is Not Found")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()