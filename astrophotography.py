# Imports
import sys
from configparser import ConfigParser
from pathlib import Path

# To specify a custom config file location, please use this format -
# Path("path", "to", "your", "config.cfg")
configLocation = Path("config.cfg")

# Variables, Arrays and Classes
pixelpitch = {
    "physical_width" : None,     # Millimetres
    "pixel_width" : None,        # Pixels
}

class Calculation:
    def __init__(self):
        self.aperture = ""       # Technically we can define aperture as having no unit, as it's a ratio.
        self.pixel_pitch = ""    # Microns
        self.focal_length = ""   # Millimetres
        self.shutter_speed = ""  # Seconds

config = ConfigParser()

# Functions
def main():             # Functionality -
    setup(config)       # Takes config data, sets into appropriate data structs.
    printVariables()    # Pretty Prints Variables to be used in calculation.
    npfMethod()         # Outputs final shutter speed value.
    sys.exit()          # Wraps-up and exits cleanly.

def setup(config):
    try:                                                                                                     # Wrapped config.read in a try-except block.  #
        config.read(configLocation)                                                                          # This was done to give the user some -       #
        Calculation.pixel_pitch = config.get('Pixel Pitch','PIXEL_PITCH')                                    # explanation as to why it failed to execute. #

        Calculation.focal_length = (float(config.get('Specific Camera Variables', 'FOCAL_LENGTH')))
        Calculation.aperture = float(config.get('Specific Camera Variables', 'APERTURE'))

        if not(Calculation.pixel_pitch):    # If pixel_pitch doesn't have a defined value
            pixelpitch["pixel_width"] = config.get('Pixel Pitch', 'PIXEL_WIDTH')
            pixelpitch["physical_width"] = config.get('Pixel Pitch', 'PHYSICAL_WIDTH')
            
            # ( ((Physical Width) / (Pixel Width)) x 1000) = Pixel Pitch    # ( Ratio = no unit)
            Calculation.pixel_pitch = ( ((float(pixelpitch["physical_width"])) / ( float(pixelpitch["pixel_width"])) ) * 1000 )

        else:   # If pixel_pitch does have a defined value
            pass

    except:
        raise Exception('Could not open config.cfg, this could be down to a permissions error - \nOr even simply that the file does not exist, please check.\n\nhttps://github.com/AxiomYT/NPF-Rule-Calculator-Python\n\nFor further clarification.\n')

def printVariables():
    # Important that the outputs are rounded, looks neater. 2x signifigant figures. except for aperture, which can only gain from the specificity.
    print('\033[95m' + "\nFocal Length  -", round(int(Calculation.focal_length), 2), " Millimetres" + '\033[0m')
    print('\033[94m' + "Pixel Pitch   -", round(float(Calculation.pixel_pitch), 2), "Millimetres" + '\033[0m')
    print('\033[96m' + "Aperture      -", Calculation.aperture, "\n" + '\033[0m')

def npfMethod():
    # ( ((35 x aperture) + (30 x pixel pitch)) ÷ focal length ) = Shutter speed in seconds.
    Calculation.shutter_speed = ( (( 35 * Calculation.aperture ) + ( 30 * float(Calculation.pixel_pitch) )) / (float(Calculation.focal_length)))
    print('\033[93m' + "Shutter Speed -", (round(Calculation.shutter_speed * 2.0) / 2.0), " Seconds\n" + '\033[0m')

# Main
if __name__ == "__main__":
    main()