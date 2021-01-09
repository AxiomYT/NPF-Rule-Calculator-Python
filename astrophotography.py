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

class calculation:
    def __init__(self):
        self.aperture = ""       # F/Stop No.
        self.pixel_pitch = ""    # Microns
        self.focal_length = ""   # Millimetres
        self.shutter_speed = ""  # Seconds

sys.path
config = ConfigParser()

# Functions
def main():
    configRead(config)
    setup(config)
    npfMethod()
    sys.exit()

def configRead(config):
    try:
        config.read(configLocation)
        calculation.pixel_pitch = config.get('Pixel Pitch','PIXEL_PITCH')
        
        print(calculation.pixel_pitch)

        if not(calculation.pixel_pitch):
            pixelpitch["pixel_width"] = config.get('Pixel Pitch', 'PIXEL_WIDTH')
            pixelpitch["physical_width"] = config.get('Pixel Pitch', 'PHYSICAL_WIDTH')
            
            calculation.pixel_pitch = ( ( float(pixelpitch["physical_width"]) / ( float(pixelpitch["pixel_width"])) ) * 1000 )

        else:
            pass

    except:
        raise Exception('Could not open config.cfg, this could be down to a permissions error - \nOr even simply that the file does not exist, please check.\n\nhttps://github.com/AxiomYT/NPF-Rule-Calculator-Python\n\nFor further clarification.\n')

def setup(config):
    calculation.focal_length = (float(config.get('Specific Camera Variables', 'FOCAL_LENGTH')))
    calculation.aperture = float(config.get('Specific Camera Variables', 'APERTURE'))
    
    print('\033[95m' + "\nFocal Length  -", int(calculation.focal_length), " Millimetres" + '\033[0m')
    print('\033[94m' + "Pixel Pitch   -", round(float(calculation.pixel_pitch), 2), "Millimetres" + '\033[0m')  # Important that the output is rounded, round(calculation.pixel_pitch, 2)
    print('\033[96m' + "Aperture      -", calculation.aperture, "\n" + '\033[0m')

def npfMethod():
    # ( ((35 x aperture) + (30 x pixel pitch)) ÷ focal length ) = Shutter speed in seconds.
    calculation.shutter_speed = ( (( 35 * calculation.aperture ) + ( 30 * float(calculation.pixel_pitch) )) / (float(calculation.focal_length)))
    print('\033[93m' + "Shutter Speed -", (round(calculation.shutter_speed * 2.0) / 2.0), " Seconds\n" + '\033[0m')

# Main
if __name__ == "__main__":
    main()
