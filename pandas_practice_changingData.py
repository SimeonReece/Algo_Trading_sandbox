import pandas as pd
import os

class CSVProcessor:
    """
    A class for processing CSV files, including cleaning and replacing them.
    This class is designed to handle the data format shown in the provided image,
    renaming 'Price' to 'Date' and removing the row with NaN values.
    """

    def clean_data(self, df):
        """
        Cleans the data by renaming 'Price' to 'Date' (if 'Price' exists),
        removing the row with NaN values, and removing the 'Ticker' column.
        This function is designed to handle the data format shown in the provided image.

        Args:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The cleaned DataFrame.
        """
        # 1. Rename 'Price' to 'Date' if 'Price' column exists
        if 'Price' in df.columns:
            df = df.rename(columns={'Price': 'Date'})

        # 2. Drop the first row (Ticker)
        df = df.drop([0])

        # 3. Drop the row with NaN values (index 1 after dropping the first row)
        df = df.drop([1])

        # 4. Reset the index after dropping rows
        df = df.reset_index(drop=True)

        # 5. Handle the 'Ticker' column (assuming you want to remove it)
        if 'Ticker' in df.columns:
            df = df.drop('Ticker', axis=1)  # Remove the 'Ticker' column

        return df

    def replace_csv_with_dataframe(self, df, filepath):
        """
        Replaces the contents of a CSV file with the data from a Pandas DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame to write to the CSV file.
            filepath (str): The path to the CSV file.
        """
        try:
            df.to_csv(filepath, index=False)  # Write the DataFrame to the CSV, overwriting it
            print(f"File '{filepath}' has been successfully replaced.")
        except Exception as e:
            print(f"Error replacing file '{filepath}': {e}")

    def process_csv(self, filepath):
        """
        Reads a CSV file, cleans the data, replaces the original file with the cleaned data,
        and displays the cleaned DataFrame.

        Args:
            filepath (str): The path to the CSV file.
        """
        try:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(filepath)

            # Example change: Add a new column (e.g., a simple index column)
            if 'index_col' not in df.columns:  # Check if 'index_col' already exists
                df['index_col'] = range(len(df))

            # Example change: convert a column to a different data type.
            # Assuming there is a column named 'Close' you can convert it to float
            if 'Close' in df.columns:
                df['Close'] = pd.to_numeric(df['Close'], errors='coerce')  # coerce will change any non-numeric values to NaN

            # Clean the data using the clean_data method
            df = self.clean_data(df)

            # Replace the original CSV file with the cleaned DataFrame
            self.replace_csv_with_dataframe(df, filepath)

            # Display the cleaned DataFrame in the console
            print(df)

        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
        except pd.errors.EmptyDataError:
            print(f"Error: File '{filepath}' is empty.")
        except pd.errors.ParserError:
            print(f"Error: Failed to parse CSV file '{filepath}'. Check the file format.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example Usage (within the same file or in another file after importing):
if __name__ == "__main__":
    processor = CSVProcessor()
    processor.process_csv("TSLA.csv")