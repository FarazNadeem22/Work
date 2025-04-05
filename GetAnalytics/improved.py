import os
import pandas as pd

def change_file_extensions(path, from_ext='xlsx', to_ext='csv'):
    """
    Rename all files in the directory from one extension to another.

    Args:
        path (str): The directory containing the files.
        from_ext (str): Original file extension (default is 'xlsx').
        to_ext (str): Desired file extension (default is 'csv').
    """
    original_path = os.getcwd()
    os.chdir(path)

    for file in os.listdir():
        if file.endswith(f'.{from_ext}'):
            base = os.path.splitext(file)[0]
            new_name = f"{base}.{to_ext}"
            os.rename(file, new_name)
            print(f"Renamed: {file} → {new_name}")

    os.chdir(original_path)


def prompt_user_to_clear_directory(path):
    """
    Prompt the user to confirm whether to clear the non-empty directory.

    Args:
        path (str): Directory path

    Returns:
        bool: True if directory should be cleared, False otherwise
    """
    while True:
        choice = input(f"Output directory '{path}' is not empty. Empty it? (Y/n): ").strip().upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print("Please enter Y or N.")


def clear_directory(path):
    """
    Delete all files in the specified directory.

    Args:
        path (str): Path to directory to clear
    """
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        try:
            os.remove(file_path)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")


def prepare_output_directory(path):
    """
    Prepare the output directory: create if missing, and empty if user confirms.

    Args:
        path (str): Parent directory where the 'output' folder should be

    Returns:
        bool: True if ready to proceed, False if user declined to clear the folder
    """
    output_path = os.path.join(path, 'output')

    if not os.path.exists(output_path):
        os.mkdir(output_path)
        print(f"Created directory: {output_path}")
        return True

    if not os.listdir(output_path):
        print("Output folder exists and is empty.")
        return True

    if prompt_user_to_clear_directory(output_path):
        clear_directory(output_path)
        return True
    else:
        print(f"Please clear {output_path} manually.")
        return False


def get_files(path):
    """
    Process CSV and Excel files in the given directory and save analytics to 'output'.

    Args:
        path (str): The directory to process files from.
    """
    original_path = os.getcwd()
    os.chdir(path)

    if not prepare_output_directory(path):
        os.chdir(original_path)
        return

    output_path = os.path.join(path, 'output')

    for i, file in enumerate(os.listdir()):
        file_path = os.path.join(path, file)

        if file.endswith('.csv'):
            print(f"[{i}] Found CSV: {file}")
            try:
                df = pd.read_csv(file, encoding='latin-1')
                df_summary = get_analytics(df)
                out_file = os.path.join(output_path, file.replace('.csv', '_processed.csv'))
                df_summary.to_csv(out_file)
            except Exception as e:
                print(f"Failed to process {file}: {e}")

        elif file.endswith('.xlsx'):
            print(f"[{i}] Found XLSX: {file}")
            try:
                df = pd.read_excel(file)
                df_summary = get_analytics(df)
                out_file = os.path.join(output_path, file.replace('.xlsx', '_processed.csv'))
                df_summary.to_csv(out_file)
            except Exception as e:
                print(f"Failed to process {file}: {e}")

    os.chdir(original_path)


def get_analytics(df):
    """
    Generate a summary of basic statistics for each column in the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: A summary DataFrame with unique values, total rows, nulls, min, and max per column.
    """
    summary = {}

    for col in df.columns:
        try:
            unique_values = df[col].nunique()
        except Exception:
            unique_values = 'N/A'

        try:
            total = len(df[col])
        except Exception:
            total = 'N/A'

        try:
            nulls = df[col].isnull().sum()
        except Exception:
            nulls = 'N/A'

        try:
            min_val = df[col].min()
        except Exception:
            min_val = 'N/A'

        try:
            max_val = df[col].max()
        except Exception:
            max_val = 'N/A'

        summary[col] = [unique_values, total, nulls, min_val, max_val]

    summary_df = pd.DataFrame.from_dict(
        summary, orient='index',
        columns=['Unique Values', 'Total', 'Null', 'Min', 'Max']
    )

    return summary_df


# driver
if __name__ == '__main__':
    path = 'C:\\Users\\muhammad.faraz\\Desktop\\Fa****s\\fa****s_contextual\\'
    # change_file_extensions(path)  # Optional: Rename .xlsx to .csv
    get_files(path)
