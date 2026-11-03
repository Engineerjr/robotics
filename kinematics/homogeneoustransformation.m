% Clear workspace and command window
clear; clc;

%% 1. Define Rotation and Translation
% Define a rotation angle of 45 degrees around the Z-axis
theta = deg2rad(45);

% 3x3 Rotation matrix around the Z-axis
R_z = [cos(theta), -sin(theta), 0;
       sin(theta),  cos(theta), 0;
       0,           0,          1];

% Translation vector [x, y, z] in meters
d = [2; 3; 1];

%% 2. Construct the 4x4 Homogeneous Transformation Matrix
% T = [ R    d ]
%     [ 0 0 0 1 ]
T = [R_z, d; 
     0, 0, 0, 1];

disp('--- Homogeneous Transformation Matrix (T) ---');
disp(T);

%% 3. Transform a Point from Local Frame to Global Frame
% Define a point in the local/robot tool coordinate frame (homogeneous coordinates)
P_local = [1; 0; 0; 1]; % [x; y; z; 1]

% Apply the transformation to find the coordinates in the global/base frame
P_global = T * P_local;

disp('--- Point Coordinates ---');
fprintf('Point in Local Frame:  [%.2f, %.2f, %.2f]\n', P_local(1:3));
fprintf('Point in Global Frame: [%.2f, %.2f, %.2f]\n', P_global(1:3));

%% 4. Alternative: Using Robotics System Toolbox (if installed)
% If you have the Robotics System Toolbox, you can also use built-in functions:
% tform = trvec2tform([2, 3, 1]) * axang2tform([0, 0, 1, theta]);
% disp(tform);