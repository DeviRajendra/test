import pandas as pd
import numpy as np

def prepare_future_waypoints(df):
    # Create a new column to store future waypoints
    df['future_waypoints'] = np.nan

    # Function to find future waypoints based on given conditions
    def find_future_waypoints(index, speed, gps_coords):
        if speed == 0:
            return [gps_coords] * 10
        else:
            waypoints = []
            count = 0
            i = index + 7
            last_valid_coords = gps_coords
            while count < 10 and i < len(df):
                # Skip rows with speed 0
                while i < len(df) and df.at[i, 'speed'] == 0:
                    i += 1
                if i < len(df):
                    last_valid_coords = df.at[i, 'gps_coords']
                    waypoints.append(last_valid_coords)
                    count += 1
                i += 7
            if count < 10:
                waypoints.extend([last_valid_coords] * (10 - count))
            return waypoints

    # Apply the function to each row
    for index, row in df.iterrows():
        gps_coords = row['gps_coords']
        df.at[index, 'future_waypoints'] = find_future_waypoints(index, row['speed'], gps_coords)
    
    return df

# Generate example DataFrame with 100 rows
data = {
    'image_name': ['image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10', 'image11', 'image12', 'image13', 'image14', 'image15', 'image16', 'image17', 'image18', 'image19', 'image20', 'image21', 'image22', 'image23', 'image24', 'image25', 'image26', 'image27', 'image28', 'image29', 'image30', 'image31', 'image32', 'image33', 'image34', 'image35', 'image36', 'image37', 'image38', 'image39', 'image40', 'image41', 'image42', 'image43', 'image44', 'image45', 'image46', 'image47', 'image48', 'image49', 'image50', 'image51', 'image52', 'image53', 'image54', 'image55', 'image56', 'image57', 'image58', 'image59', 'image60', 'image61', 'image62', 'image63', 'image64', 'image65', 'image66', 'image67', 'image68', 'image69', 'image70', 'image71', 'image72', 'image73', 'image74', 'image75', 'image76', 'image77', 'image78', 'image79', 'image80', 'image81', 'image82', 'image83', 'image84', 'image85', 'image86', 'image87', 'image88', 'image89', 'image90', 'image91', 'image92', 'image93', 'image94', 'image95', 'image96', 'image97', 'image98', 'image99', 'image100'],
    'speed': ([2, 2, 2, 0, 0, 0, 2, 2, 0, 2, 0, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2,
       0, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0,
       2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2,
       2, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2,
       2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2]),
    'gps_coords': [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6), (7, 7, 7), (8, 8, 8), (9, 9, 9), (10, 10, 10), (11, 11, 11), (12, 12, 12), (13, 13, 13), (14, 14, 14), (15, 15, 15), (16, 16, 16), (17, 17, 17), (18, 18, 18), (19, 19, 19), (20, 20, 20), (21, 21, 21), (22, 22, 22), (23, 23, 23), (24, 24, 24), (25, 25, 25), (26, 26, 26), (27, 27, 27), (28, 28, 28), (29, 29, 29), (30, 30, 30), (31, 31, 31), (32, 32, 32), (33, 33, 33), (34, 34, 34), (35, 35, 35), (36, 36, 36), (37, 37, 37), (38, 38, 38), (39, 39, 39), (40, 40, 40), (41, 41, 41), (42, 42, 42), (43, 43, 43), (44, 44, 44), (45, 45, 45), (46, 46, 46), (47, 47, 47), (48, 48, 48), (49, 49, 49), (50, 50, 50), (51, 51, 51), (52, 52, 52), (53, 53, 53), (54, 54, 54), (55, 55, 55), (56, 56, 56), (57, 57, 57), (58, 58, 58), (59, 59, 59), (60, 60, 60), (61, 61, 61), (62, 62, 62), (63, 63, 63), (64, 64, 64), (65, 65, 65), (66, 66, 66), (67, 67, 67), (68, 68, 68), (69, 69, 69), (70, 70, 70), (71, 71, 71), (72, 72, 72), (73, 73, 73), (74, 74, 74), (75, 75, 75), (76, 76, 76), (77, 77, 77), (78, 78, 78), (79, 79, 79), (80, 80, 80), (81, 81, 81), (82, 82, 82), (83, 83, 83), (84, 84, 84), (85, 85, 85), (86, 86, 86), (87, 87, 87), (88, 88, 88), (89, 89, 89), (90, 90, 90), (91, 91, 91), (92, 92, 92), (93, 93, 93), (94, 94, 94), (95, 95, 95), (96, 96, 96), (97, 97, 97), (98, 98, 98), (99, 99, 99), (100, 100, 100)]
}

df = pd.DataFrame(data)
df = prepare_future_waypoints(df)

# Display the DataFrame with future waypoints
print(df[['image_name', 'speed', 'gps_coords', 'future_waypoints']])
