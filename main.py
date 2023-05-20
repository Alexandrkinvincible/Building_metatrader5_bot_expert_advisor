import json
import os
import mt5_interface
import pandas as pd # import the 'pandas' module for displaying data obtained in the tabular form

# Function to import settings from settings.json
def get_project_settings(importFilepath):
    # Test the filepath to sure it exists
    if os.path.exists(importFilepath):
        # Open the file
        f = open(importFilepath, "r")
        # Get the information from file
        project_settings = json.load(f)
        # Close the file
        f.close()
        # Return project settings to program
        return project_settings
    else:
        return ImportError



# Main function
if __name__ == '__main__':
    import_filepath = "settings.json"
    project_settings = get_project_settings(import_filepath)
    mt5_interface.start_mt5(project_settings["username"], project_settings["password"], project_settings["server"], project_settings["mt5Pathway"])
    mt5_interface.tick_extraction(project_settings["symbols"])