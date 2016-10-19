import math
import argparse

DELTA_DIAGONAL_ROD = 300.0 
DELTA_SMOOTH_ROD_OFFSET = 212.357
DELTA_EFFECTOR_OFFSET = 30.0
DELTA_CARRIAGE_OFFSET = 30.0
DELTA_RADIUS = (DELTA_SMOOTH_ROD_OFFSET-DELTA_EFFECTOR_OFFSET-DELTA_CARRIAGE_OFFSET)
DELTA_PRINTABLE_RADIUS = 127.0

SIN_60 = math.sin(math.pi/3)
COS_60 = 0.5
DELTA_TOWER1_X = -SIN_60*DELTA_RADIUS
DELTA_TOWER1_Y = -COS_60*DELTA_RADIUS
DELTA_TOWER2_X = SIN_60*DELTA_RADIUS
DELTA_TOWER2_Y = -COS_60*DELTA_RADIUS
DELTA_TOWER3_X = 0.0
DELTA_TOWER3_Y = DELTA_RADIUS
DELTA_DIAGONAL_ROD_2  = (DELTA_DIAGONAL_ROD*DELTA_DIAGONAL_ROD)
Z_MAX_POS = 280.67

X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2

delta= [0.0,0.0,0.0];
current_pos = [0.0,0.0,0.0]
difference = delta

parser = argparse.ArgumentParser(description='Provide Cartesian coordinates.')
parser.add_argument('source', nargs=3, type=float,
                    help='Cartesian values for starting position.')
parser.add_argument('destination', nargs=3, type=float,
                    help='Cartesian values for ending position.')
args = parser.parse_args()

def sq(d):
  return d * d;

def calculate_delta(cartesian):
  delta[X_AXIS] = math.sqrt(DELTA_DIAGONAL_ROD_2
                       - sq(DELTA_TOWER1_X-cartesian[X_AXIS])
                       - sq(DELTA_TOWER1_Y-cartesian[Y_AXIS])
                       ) + cartesian[Z_AXIS];
  delta[Y_AXIS] = math.sqrt(DELTA_DIAGONAL_ROD_2
                       - sq(DELTA_TOWER2_X-cartesian[X_AXIS])
                       - sq(DELTA_TOWER2_Y-cartesian[Y_AXIS])
                       ) + cartesian[Z_AXIS];
  delta[Z_AXIS] = math.sqrt(DELTA_DIAGONAL_ROD_2
                       - sq(DELTA_TOWER3_X-cartesian[X_AXIS])
                       - sq(DELTA_TOWER3_Y-cartesian[Y_AXIS])
                       ) + cartesian[Z_AXIS];
  print "  Cartesian =", cartesian, "\n  Delta =", delta
  
print "Delta kinematics conversion simulation:"
print "From:"
calculate_delta(args.source)
current_pos[X_AXIS] = delta[X_AXIS]
current_pos[Y_AXIS] = delta[Y_AXIS]
current_pos[Z_AXIS] = delta[Z_AXIS]
print "To:"
calculate_delta(args.destination)
difference[X_AXIS] = delta[X_AXIS] - current_pos[X_AXIS]
difference[Y_AXIS] = delta[Y_AXIS] - current_pos[Y_AXIS]
difference[Z_AXIS] = delta[Z_AXIS] - current_pos[Z_AXIS] 
print "Difference:"
print "  X Tower:", difference[X_AXIS]
print "  Y Tower:", difference[Y_AXIS]
print "  Z Tower:", difference[Z_AXIS]

