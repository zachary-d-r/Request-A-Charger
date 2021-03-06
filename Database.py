"""
Request a Charger
Database Code
David Anapolsky
"""
# Import the pandas module to create tables to manage the data
from traceback import print_tb
from numpy import character
import pandas as pd

# Define the demo function for testing/demonstration purposes
def demo():
    # Store the filename of the student data in a variable
    studentDataFile = r'Databases\studentData.dat'

    # Create an instance of the StudentDatabase class
    database = StudentDatabase(studentDataFile)

    # Testing adding student data normally
    success = database.add_student('epresent@emeryweiner.org','ad334f', 1, 'USB-C', 1, database.get_timestamp())
    print('\nDatabase:', database, '\nSuccess:', success)

    # Testing trying to add a prexisting student
    success = database.add_student(email='epresent@emeryweiner.org', chargerType='Dell', timeIn=pd.Timestamp.now())
    print('\nDatabase:', database, '\nSuccess:', success)

    # Testing editing student data normally
    success = database.edit_student('epresent@emeryweiner.org')
    print('\nDatabase:', database, '\nSuccess:', success)

    # Testing trying to edit a non-existent student
    success = database.edit_student('zsamuels@emeryweiner.org')
    print('\nDatabase:', database, '\nSuccess:', success)

    # Testing getting a student's data normally
    data = database.get_student('epresent@emeryweiner.org')
    print('\nStudent Data:', data)

    # Testing getting a student's data converted to a different data type
    convertedData = database.get_student('epresent@emeryweiner.org', 'dict')
    print('\nConverted Student Data:', convertedData)

    # Testing trying to get a student's data converted to a non-supported data type
    notSupportedData = database.get_student('epresent@emeryweiner.org', 'hashMap')
    print('\nNot Supported Conversion Student Data:', notSupportedData)


# Define the Database class as the base class
class Database():
    # Initialize the database
    def __init__(self, filename, data_names, indexName):
        # Store the arguments in data attributes
        self.filename = filename
        self.data_names = data_names
        self.indexName = indexName

        # Set up the dataframe
        self.setup_dataframe()

    # Define the setup_dataframe method to set up the dataframe to store the data
    def setup_dataframe(self):
        # Try to get the data from the pickle file
        self.dataFrame = self.data_pickle()

        # If the dataframe is empty, then set it up completely
        if self.dataFrame.empty:
            
            # Call the reset_dataframe method to reset the dataframe
            self.reset_dataframe()


    # Define the reset_dataframe to set the dataframe to an empty dataframe formatted
    def reset_dataframe(self):
        # Make a dataframe with the data names
        self.dataFrame = pd.DataFrame(columns=self.data_names)
        
        # Set the index label of the dataframe to the index name data attribute
        self.dataFrame.rename_axis(self.indexName, inplace=True)
    

    # Define the csv_to_dataframe method to open a csv file and store it as the dataframe
    def csv_to_dataframe(self, filename):
        # Read the csv file using pandas and store the dataframe in the data attribute
        self.dataFrame = pd.read_csv(filename, index_col=0)

        # Pickle the dataframe to its file
        self.data_pickle('w')

    
    def delete(self, studentEmail):
        self.dataFrame.drop(str(studentEmail), inplace=True)
    

    # Define the data_pickle method to load from or dump to the data's pickle file
    def data_pickle(self, mode='r'):
            # If mode is equal to read, then read the contents of the data file
            if mode == 'r':

                # Try to unpickle the file
                try:

                    # Load the contents of the file into a pandas object
                    pandasObject = pd.read_pickle(self.filename)
                
                # Catch an exception if the file does not exist
                except (OSError, IOError, EOFError):

                    # Set the pandas object to an empty dataframe
                    pandasObject = pd.DataFrame()

                # Finally, return the pandas object
                finally:

                    # Return the pandas object
                    return pandasObject

            # Else if mode is equal to write, then dump the data into its data file
            elif mode == 'w':

                # Dump the pandas object into its file
                self.dataFrame.to_pickle(self.filename)


    # Define the get_timestamp method to get the current timestamp
    def get_timestamp(self):
        # Create a timestamp object for the current time with pandas
        timestamp = pd.Timestamp.now()

        # Return the timestamp
        return timestamp   

    # Define the __str__ method to show the dataframe properly if an instance of the class is used as a string
    def __str__(self):

        # Return the dataframe as a string
        return str(self.dataFrame)

    # To print the database and make it look nice in the console
    def print_database(self):
        with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
            print(self.dataFrame)


# Define the Student Database class to work with the student data
class StudentDatabase(Database):
    # Initialize the database
    def __init__(self, filename):
        # Create a list with the data names
        data_names = ['Charger Type', 'Timestamp In']
        
        # Store the index name in a data attribute
        indexName = 'Email'

        # Intialize the base class with the student settings
        super().__init__(filename, data_names, indexName)


    # Define the add_student method to add student data to the student data dataframe
    def add_student(self, email, chargerType=None, timeIn=None):
        # If the email is in the index values, then edit the student's data
        if email not in self.dataFrame.index:

            # Make a two dimensional list with all the values that should be added
            addValues = [keyValuePair for keyValuePair in zip(self.data_names,
            (chargerType, timeIn)) if keyValuePair[1] != None]

            # For column, data in the add values, add the student's data              # I realize this is inefficient = pandas can sometimes be annoying
            for column, data in addValues:

                # Add the student's data
                self.dataFrame.loc[email, column] = data
            
            # Pickle the dataframe to its file
            self.data_pickle('w')
            
            # Return True
            return True
        
        # Else, return False
        else:

            return False

    # Check if student is in database or not
    def check_existence(self, email):
        # If the email is in the database, then return True, else return False
        if email in self.dataFrame.index: return True
        else: return False

    # Define the edit_student method to edit student data in the student data dataframe
    def edit_student(self, email, chargerType=None, timeIn=None):
        # If the email is in the index values, then edit the student's data
        if email in self.dataFrame.index:

            # Make a two dimensional list with all the values that should be changed
            changeValues = [keyValuePair for keyValuePair in zip(self.data_names,
            (chargerType, timeIn)) if keyValuePair[1] != None]

            # For column, data in the change values, update the student's data              # I realize this is inefficient = pandas can sometimes be annoying
            for column, data in changeValues:

                # Update the student's data
                self.dataFrame.loc[email, column] = data

            # Pickle the dataframe to its file
            self.data_pickle('w')  
            
            # Return True
            return True
        
        # Else, return False
        else:

            return False


    # Define the remove_student method to remove student data from the student data dataframe
    def remove_student(self, email):
        # If the email is in the index values, then remove the student's data
        if email in self.dataFrame.index:

            # Drop the student's data out of the dataframe in place
            self.dataFrame.drop(index=email, inplace=True)

            # Pickle the dataframe to its file
            self.data_pickle('w')
            
            # Return True
            return True
        
        # Else, return False
        else:

            return False
        

    # Define the get_student method to get student data from the student data dataframe
    def get_student(self, email, type='series', **kwargs):
        # If the email is in the index values, then get the student's data
        if email in self.dataFrame.index:

            # Get the series of data associate with the email
            studentSeries = self.dataFrame.loc[email]

            # If the series has a to_'type' option, then return the series as that type of data
            if hasattr(studentSeries, f'to_{type}'):

                # Try to convert the series to the data type
                try:

                    # Get the method to convert the series and run it with the keyword arguments
                    data = getattr(studentSeries, f'to_{type}')(*kwargs)
                
                # Catch an exception if it failed to convert
                except:

                    # Return None at the end
                    pass
                
                # Else, return the data
                else:

                    # Return the data
                    return data
            
            # Else if the type is series, then return it as a normal series
            elif type == 'series':

                # Return the series
                return studentSeries
        
        # Return None if something did not work
        return None


# Define the Locker Database class to work with the locker data
class LockerDatabase(Database):
    # Initialize the database
    def __init__(self, filename):
        """
        Locker Key:
        0: no charger
        1: lightning
        2: magsafe
        3: surface
        4: usb-c
        """
        # Create a list with the data names
        data_names = ['Charger Type']
        
        # Store the index name in a data attribute
        indexName = 'Locker Number'

        # Intialize the base class with the student settings
        super().__init__(filename, data_names, indexName)
    
    # Define the setup_lockers method to set up the dataframe with the lockers' starting charger data
    def setup_lockers(self, locker_dictionary:dict):
        """
        Setup the initial charger data for the lockers
        """
        # For lockerNum in the keys of the dictionary, add the locker data              # I realize this is inefficient = pandas can sometimes be annoying
        for lockerNum in locker_dictionary:

            # Add the locker data
            self.dataFrame.loc[lockerNum, 'Charger Type'] = locker_dictionary[lockerNum]
        
        # Pickle the dataframe to its file
        self.data_pickle('w')
    
    # Define the edit_locker method to edit the charger type of a locker
    def edit_locker(self, lockerNumber:int, chargerType:int):
        """
        Edit the charger type of a locker
        (0: no charger, 1: lightning, 2: magsafe, 3: surface, 4: usb-c)
        """

        # Edit the locker data
        print('Charger Arg:', chargerType)
        print('Before:', self.dataFrame.loc[(lockerNumber), 'Charger Type'])
        self.dataFrame.loc[(lockerNumber), 'Charger Type'] = chargerType
        print('After:', self.dataFrame.loc[(lockerNumber), 'Charger Type'])
        #self.dataFrame[lockerNumber]['Charger Type'] = chargerType
        
        # Pickle the dataframe to its file
        self.data_pickle('w')

    # Define the find__locker method to find a locker with the requested charger and change its charger type
    def find_locker(self, find:int, replace:int):
        """
        Find a charger in the locker database and change its charger type
        (0: no charger, 1: lightning, 2: magsafe, 3: surface, 4: usb-c)
        Return 0 if there is no charger available of that type
        """

        """
        New: look = charger type, replace = 0
        Returning: look = 0, replace = charger type
        """

        print(f"\n\n{self.dataFrame}\n\n")
        
        # Iterate through the rows to find a locker with the requested charger
        for index, row in self.dataFrame.iterrows():
            if row['Charger Type'] == find:
                self.edit_locker(index, replace)
                return index
            """
            if find != chargerType and row['Charger Type'] == find:
                self.edit_locker(index, chargerType)
                return index
            elif find == chargerType and row['Charger Type'] == find:
                self.edit_locker(index, 0)
                return index
            """
        
        # Else, return 0 if no chargers of that type were found
        return 0



"""
print("D!")
lockerDatabase = LockerDatabase(r'Databases\lockerData.dat') # Create the locker database
print("De!")
lockerDatabase.setup_lockers({1:0,2:0,3:1,4:1,5:2,6:2,7:3,8:3,9:4,10:4,11:0})
print("Done!")
"""