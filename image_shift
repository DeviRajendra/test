import cv2
import numpy as np

def shift_image(image, shift_amount):
    rows, cols, _ = image.shape
    M = np.float32([[1, 0, 0], [0, 1, shift_amount]])
    shifted_image = cv2.warpAffine(image, M, (cols, rows))
    return shifted_image

def adjust_waypoints(waypoints, shift_amount, y_scale):
    adjusted_waypoints = []
    for waypoint in waypoints:
        x, y = waypoint
        adjusted_y = int(y + shift_amount * y_scale)
        adjusted_waypoints.append((x, adjusted_y))
    return adjusted_waypoints

# Load the image
image = cv2.imread('road_image.jpg')  # Replace 'road_image.jpg' with your image file path

# Define parameters
shift_amount = 50  # Define how much to shift the image along the y-axis (in pixels)
y_scale = 0.5  # Scale factor for adjusting future waypoints based on image shift

# Shift the image
shifted_image = shift_image(image, shift_amount)

# Display the shifted image
cv2.imshow('Shifted Image', shifted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load waypoints (example waypoints)
waypoints = [(100, 200), (150, 250), (200, 300), (250, 350), (300, 400), 
             (350, 450), (400, 500), (450, 550), (500, 600), (550, 650)]

# Adjust waypoints based on image shift
adjusted_waypoints = adjust_waypoints(waypoints, shift_amount, y_scale)

# Print adjusted waypoints
print("Original Waypoints:", waypoints)
print("Adjusted Waypoints:", adjusted_waypoints)
