"""
Request a Charger
Database Code
David Anapolsky
"""

# Import the pandas module to create tables to manage the data
import pandas as pd

# Define the demo function for testing/demonstration purposes
def demo():
    # Store the filename of the student data in a variable
    studentDataFile = 'studentData.dat'

    # Create an instance of the StudentDatabase class
    database = StudentDatabase(studentDataFile)

    # Testing adding student data normally
    success = database.add_student('epresent@emeryweiner.org','ad334f', 1, 'USB-C', 1, database.get_timestamp())
    print('\nDatabase:', database, '\nSuccess:', success)

    # Testing trying to add a prexisting student
    success = database.add_student(email='epresent@emeryweiner.org', verifyCodeIn='agfdgf', chargerNum=2, chargerType='Dell', lockerNumIn=4, timeIn=pd.Timestamp.now())
    print('\nDatabase:', database, '\nSuccess:', success)

    # Testing editing student data normally
    success = database.edit_student('epresent@emeryweiner.org', verifyCodeOut='df4ert', lockerNumOut=5, timeOut=database.get_timestamp())
    print('\nDatabase:', database, '\nSuccess:', success)

    # Testing trying to edit a non-existent student
    success = database.edit_student('zsamuels@emeryweiner.org', verifyCodeOut='dhbgvc', lockerNumOut=3, timeOut=pd.Timestamp.now())
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


# Define the Database class to work with the student data
class StudentDatabase():


    # Initialize the database
    def __init__(self, filename):
        # Store the filename in a data attribute
        self.__filename = filename

        # Create a list with the data names
        self.__data_names = ['Verification Code In', 'Charger Number', 'Charger Type', 'Locker Number In', 'Timestamp In', 'Verification Code Out', 'Locker Number Out', 'Timestamp Out']
        
        # Store the index name in a data attribute
        self.__indexName = 'Email'

        # Set up the dataframe
        self.setup_dataframe()


    # Define the setup_dataframe method to set up the dataframe to store the student data
    def setup_dataframe(self):
        # Try to get the student data from the pickle file
        self.__studentFrame = self.data_pickle()

        # If the dataframe is empty, then set it up completely
        if self.__studentFrame.empty:
            
            # Call the reset_dataframe method to reset the dataframe
            self.reset_dataframe()


    # Define the reset_dataframe to set the student dataframe to an empty dataframe formatted
    def reset_dataframe(self):
        # Make a dataframe with the data names
        self.__studentFrame = pd.DataFrame(columns=self.__data_names)
        
        # Set the index label of the dataframe to the index name data attribute
        self.__studentFrame.rename_axis(self.__indexName, inplace=True)
    

    # Define the csv_to_dataframe method to open a csv file and store it as the dataframe
    def csv_to_dataframe(self, filename):
        # Read the csv file using pandas
        dataframe = pd.read_csv(filename, index_col=0)

        # Store the dataframe as the main dataframe
        self.__studentFrame = dataframe

        # Pickle the dataframe to its file
        self.data_pickle('w')


    # Define the data_pickle method to load from or dump to the data's pickle file
    def data_pickle(self, mode='r'):
            # If mode is equal to read, then read the contents of the data file
            if mode == 'r':

                # Try to unpickle the file
                try:

                    # Load the contents of the file into a pandas object
                    pandasObject = pd.read_pickle(self.__filename)
                
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
                self.__studentFrame.to_pickle(self.__filename)


    # Define the add_student method to add student data to the student data dataframe
    def add_student(self, email, verifyCodeIn=None, chargerNum=None, chargerType=None, lockerNumIn=None, timeIn=None, verifyCodeOut=None, lockerNumOut=None, timeOut=None):
        # If the email is in the index values, then edit the student's data
        if email not in self.__studentFrame.index:

            # Make a two dimensional list with all the values that should be added
            addValues = [keyValuePair for keyValuePair in zip(self.__data_names,
            (verifyCodeIn, chargerNum, chargerType, lockerNumIn, timeIn, verifyCodeOut, lockerNumOut, timeOut)) if keyValuePair[1] != None]

            # For column, data in the add values, add the student's data              # I realize this is inefficient = pandas can sometimes be annoying
            for column, data in addValues:

                # Add the student's data
                self.__studentFrame.loc[email, column] = data
            
            # Pickle the dataframe to its file
            self.data_pickle('w')
            
            # Return True
            return True
        
        # Else, return False
        else:

            return False
        
        '''
        # Get the current timestamp
        timestamp = pd.Timestamp.now()

        # Make a pandas series to store the new data
        newSeries = pd.Series(data={'Verification Code In': verifyCodeIn, 'Charger Number': chargerNum,
        'Charger Type': chargerType, 'Locker Number In': lockerNumIn, 'Timestamp In': timestamp}, name=email)

        # Try to update the student dataframe with the new series
        try:

            # Append the new series to the student dataframe
            self.__studentFrame = self.__studentFrame.append(newSeries, verify_integrity=True)
        
        # Catch a ValueError if there already is a entry for the student in the dataframe
        except ValueError:

            return False

        # Else, pickle the dataframe and return True
        else:

            # Pickle the dataframe to its file
            self.data_pickle('w')
            
            # Return True
            return True
        '''
    

    # Define the edit_student method to edit student data in the student data dataframe
    def edit_student(self, email, verifyCodeIn=None, chargerNum=None, chargerType=None, lockerNumIn=None, timeIn=None, verifyCodeOut=None, lockerNumOut=None, timeOut=None):
        # If the email is in the index values, then edit the student's data
        if email in self.__studentFrame.index:

            # Make a two dimensional list with all the values that should be changed
            changeValues = [keyValuePair for keyValuePair in zip(self.__data_names,
            (verifyCodeIn, chargerNum, chargerType, lockerNumIn, timeIn, verifyCodeOut, lockerNumOut, timeOut)) if keyValuePair[1] != None]

            # For column, data in the change values, update the student's data              # I realize this is inefficient = pandas can sometimes be annoying
            for column, data in changeValues:

                # Update the student's data
                self.__studentFrame.loc[email, column] = data

            # Pickle the dataframe to its file
            self.data_pickle('w')  
            
            # Return True
            return True
        
        # Else, return False
        else:

            return False

        '''
        # Get the pandas series associated with the student's data
        studentSeries = self.__studentFrame.loc[email]

        # Make a two dimensional list turned dictionary with all the values that should be changed
        changeValues = dict([keyValuePair for keyValuePair in zip(self.__data_names,
        (verifyCodeIn, chargerNum, chargerType, lockerNumIn, timeIn, verifyCodeOut, lockerNumOut, timeOut)) if keyValuePair[1] != None])

        # Update the pandas series
        studentSeries.update(changeValues)

        # Update the dataframe
        self.__studentFrame.update(studentSeries)

        #Or

        self.__studentFrame.loc[email].update(changeValues)
        '''


    # Define the remove_student method to remove student data from the student data dataframe
    def remove_student(self, email):
        # If the email is in the index values, then remove the student's data
        if email in self.__studentFrame.index:

            # Drop the student's data out of the dataframe in place
            self.__studentFrame.drop(index=email, inplace=True)

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
        if email in self.__studentFrame.index:

            # Get the series of data associate with the email
            studentSeries = self.__studentFrame.loc[email]

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


    # Define the get_timestamp method to get the current timestamp
    def get_timestamp(self):
        # Create a timestamp object for the current time with pandas
        timestamp = pd.Timestamp.now()

        # Return the timestamp
        return timestamp
    

    # Define the __str__ method to show the dataframe properly if an instance of the class is used as a string
    def __str__(self):

        # Return the student dataframe as a string
        return str(self.__studentFrame)


# When main is called
if __name__ == '__main__':

    # Call the demo function
    demo()
