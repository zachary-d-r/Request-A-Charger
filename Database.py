"""
Request a Charger
Database Code
David Anapolsky
"""

# Import the pandas module to create tables to manage the data
import pandas as pd

# Define the main function
def main():
    # Store the filename of the user data in a variable
    userDataFile = 'userData.dat'

    # Setup the user data dataframe
    userDataFrame = setup_user_data(userDataFile)

    #Temp test adding data
    userDataFrame = add_user_data(userDataFrame, 'epresent@emeryweiner.org','ad334f', 1, 'USB-C', 1)
    print(userDataFrame.head())

    userDataFrame = add_user_data(userDataFrame, 'epresent@emeryweiner.org','agfdgf', 2, 'USB-e', 4)
    print(userDataFrame)

    # Pickle the user data to its file
    #pandas_pickle(userDataFile, userDataFrame, 'w')

# Define the setup_user_data function to setup the user data dataframe
def setup_user_data(filename):
    # Try to get the user data from the pickle file
    userDataFrame = pandas_pickle(filename)

    # If the dataframe is empty, then set it up completely
    if userDataFrame.empty:

        # Create a list with the column names
        column_names = ['Verification Code In', 'Charger Number', 'Charger Type', 'Locker Number', 'Timestamp In', 'Verification Code Out', 'Timestamp Out']

        # Set the columns labels of the dataframe to the column names list
        #userDataFrame.columns = column_names

        # Make a dataframe with the column names and index name
        userDataFrame = pd.DataFrame(columns=column_names, dtype='object')

        # Create a variable with the index name
        indexName = 'Email'
        
        # Set the index label of the dataframe to the index name variable
        userDataFrame.rename_axis(indexName)

    # Return the user data frame
    return userDataFrame


# Define the add_user_data function to add user data to the user data dataframe
def add_user_data(userDataFrame, email, verifyCodeIn, chargerNum, chargerType, lockerNum):
    # Get the current timestamp
    timestamp = pd.Timestamp.now()

    # Make a pandas series to store the new data
    newSeries = pd.Series(data={'Verification Code In': verifyCodeIn, 'Charger Number': chargerNum, 'Charger Type': chargerType, 'Locker Number': lockerNum, 'Timestamp In': timestamp}, name=email)

    # Try to update the user dataframe with the newSeries
    try:

        # Append the the new series to the user dataframe
        userDataFrame = userDataFrame.append(newSeries, verify_integrity=True)
    
    # Catch a ValueError if there already is a entry for the student in the dataframe
    except ValueError:

        # Return False
        return False

    # Else, return True
    else:

        # Return the userDataFrame                      #Temp should be a data attribute in a class
        return userDataFrame


# Define the manual_get_dataframe method to manually open a csv file and store it in a dataframe
def manual_get_dataframe(filename):
    # Read the csv file using pandas
    dataframe = pd.read_csv(filename, index_col=0)

    # Return the dataframe
    return dataframe


# Define the pandas_pickle function to load from or dump to pickle files with panda objects
def pandas_pickle(filename, pandasObject='', mode='r'):
        # If mode is equal to read, then read the contents of the data file
        if mode == 'r':

            # Try to unpickle the file
            try:

                # Load the contents of the file into a pandas object
                pandasObject = pd.read_pickle(filename)
            
            # Catch an exception if the file does not exist
            except (OSError, IOError, EOFError):

                # Set the pandas object to an empty data frame
                pandasObject = pd.DataFrame(dtype='object')

            # Finally, return the pandas object
            finally:

                # Return the pandas object
                return pandasObject

        # Else if mode is equal to write and a pandas object argument was supplied, 
        # then dump the pandas object into the data file
        elif mode == 'w' and type(pandasObject) != str:

            # Dump the pandas object into the file
            pandasObject.to_pickle(filename)


# When main is called
if __name__ == '__main__':

    # Call the main() function
    main()
