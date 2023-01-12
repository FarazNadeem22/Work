import pandas as pd 
import numpy as np 
import os

def change_file_name(path):
    """
    This function will change files with xlsx extension to csv 
    Args {path}: The path where the files exist 
    """
    # Save the original path 
    original_path = os.getcwd()
    
    # Change path to the path passed in to the function. This is where the function will expect the files to be
    os.chdir(path)
    
    # Loop over all files in the directory 
    for file in os.listdir():       
        
        # If the file is an excel file
        if file[-4:] == 'xlsx':          
        
            # Change the extension to csv 
            os.rename(file, file[:-4]+'csv')
    
    # Change the current working  directory back to the original path
    os.chdir(original_path)

def get_files(path):
    """
    This function will loop over the files in the given path 
    """
    # Save the original path 
    original_path = os.getcwd()
    
    # Change path to the path passed in to the function. This is where the function will expect the files to be
    os.chdir(path)

    # Check if output folder exists
    isExist = os.path.exists(path+'output')
    if isExist:
        print("Output folder exists")
        if len(os.listdir(path+'output')) == 0:
            print(".")
        else:
            condition = True
            while condition:
                try:
                    choice = str(input("Output directory is not empty. Empty directory? Y/n"))
                    choice = choice.upper()

                    if choice == 'Y':
                        print(f"Deleting directory {path+'output'}")
                        # Empty Directory
                        for file in os.listdir(path+'output\\'):
                            print(f"Attempting to delete {file}")    
                            os.remove(os.path.join(path+'output\\' ,file))
                        condition = False 

                    elif choice == 'N':
                        print(f"Please clear {path+'output'}")
                        condition = False
                        return 
                    else:
                        print("Please enter Y or n")
                except:
                    print("Please enter Y or n")
    else:
        print(f"Creating directory {path+'output'}")
        os.mkdir(path+'output')


    # Loop over all files in the directory 
    for i, file in enumerate(os.listdir()):

        print(i,file)   
        if file[-4:] == '.csv':
            
            # Convert to pd.DataFrame
            print(f"Catch CSV {file}")
            df = pd.read_csv(file, encoding='latin-1')

            # Check to see if output directory exists 
            pass

            # Check to make sure that output directory is empty 
            pass

            # Get analytics 
            df = get_analytics(df= df)

            # Write file to output directory   
            df.to_csv(path+'output\\'+file[:-4]+'processed.csv')
        
        elif file[-4:] == 'xlsx':
            
            # Convert to pd.DataFrame
            print(f"Catch XLSX {file}")
            df = pd.read_excel(file)
            
            # Get analytics 
            df = get_analytics(df= df)

            # Write file to output directory   
            df.to_csv(path+'output\\'+file[:-5]+'processed.csv')

    # Change the current working  directory back to the original path
    os.chdir(original_path)

def get_analytics(df):
    """
    This function will take a df and return its basic analytics 
    """
    dict_ = {}
    col_names = []
    total = []

    for i, col in enumerate(df.keys()):
        try:
            Unique_Values = len(pd.unique(df[col]))
        except:
            Unique_Values = "Not Available"

        try:
            Total = len(df[col])
        except:
            Total = "Not Available"
        
        try:
            NaN = df[col].isnull().sum()
        except:
            NaN = "Not Available"

        try:
            Min = df[col].min()
        except:
            Min = "Not Available"
        
        try:
            Max = df[col].max()
        except:
            Max = "Not Available"
        
        
        #print(i, Unique_Values, Total,NaN, Min, Max)
        dict_[col] = [Unique_Values, Total,NaN, Min, Max]
        total.append(Total)
        col_names.append(col)
        
    df_return = pd.DataFrame(dict_, columns=col_names, index=["Unique Values", "Total","Null","Min", "Max"])
    return df_return.T


path = 'C:\\Users\\muhammad.faraz\\Desktop\\Farmers\\farmers_contextual\\'
# change_file_name(path)
get_files(path)
