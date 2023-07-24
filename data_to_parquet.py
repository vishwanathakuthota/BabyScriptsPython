import pandas as pd

def convert_to_parquet(input_file, output_file):
    # Assuming the data is in CSV format, you can change the read method if needed
    data = pd.read_csv(input_file)

    # Convert the data to Parquet format
    data.to_parquet(output_file)

if __name__ == "__main__":
    input_file = "input_data.csv"   # Replace with the path to your input data file
    output_file = "output_data.parquet"   # Replace with the desired output file name
    
    convert_to_parquet(input_file, output_file)
