
from classes.beam import Beam
from classes.bearing import Bearing
from classes.force import Force
from classes.moment import Moment
from random import uniform

def main():
    try:
        # Create a rectangular beam with specific dimensions
        length = 10.0  # Length of the beam in meters
        
        beam = Beam(length)

        # Add two bearings, one at each end of the beam
        beam.add_bearing(pos_x=0, fz=True, fx=True)  # Bearing at the start
        beam.add_bearing(pos_x=length, fz=True)  # Bearing at the end

        # Add a random force to the beam
        force_magnitude = 1000  # Force in newtons
        force_position = uniform(0, length)  # Random position along the beam's length
        beam.add_force(F=force_magnitude, pos_x=force_position, angle = 45)

        # Calculate reactions at the bearings
        beam.calculate_reactions()
        

        # Output the positions and reactions at the bearings for verification
        print(f"Applied Force of {force_magnitude} at position {force_position}")
        for idx, bearing in enumerate(beam.bearings):
            print(f"Bearing {idx+1}: Position = {bearing.pos_x} m, Vertical Reaction = {bearing.Fz} N , Horizontal Reaction = { bearing.Fx}")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()