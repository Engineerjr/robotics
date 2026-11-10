
clear;
clc;
close all;

%% TWO-SECTION PLANAR CONTINUUM ROBOT

% Section parameters
L = [20, 10];                 % Arc lengths (mm)
phi = [0, 180];                % Equilibrium angles (degrees)
kappa = [0.05, 0.1];           % Curvatures (1/mm)

% Number of points used to draw each section
N = 100;

%% Initialize global coordinates

base = [0; 0];                % Initial position [x; z]
alpha = 0;                    % Initial orientation

X = [];
Z = [];

%% Calculate each robot section

for i = 1:2

    % Module 1: Constant curvature geometry
    [xLocal, zLocal, theta] = ...
        constantCurvature(L(i), phi(i), kappa(i), N);

    % Module 2: Coordinate transformation
    [xGlobal, zGlobal] = ...
        transformSection(xLocal, zLocal, base, alpha);

    % Store coordinates
    X = [X, xGlobal];
    Z = [Z, zGlobal];

    % Update base position for next section
    base = [xGlobal(end); zGlobal(end)];

    % Update orientation
    alpha = alpha + theta;

    fprintf('Section %d:\n', i);
    fprintf('  Arc length = %.2f mm\n', L(i));
    fprintf('  Curvature = %.3f 1/mm\n', kappa(i));
    fprintf('  Bending angle = %.3f rad\n', theta);
    fprintf('  Bending angle = %.2f degrees\n\n', ...
        rad2deg(theta));

end

%% Module 3: Robot visualization

plotRobot(X, Z, L, phi, kappa);

%% Display end-effector position

fprintf('End-effector position:\n');
fprintf('X = %.3f mm\n', base(1));
fprintf('Z = %.3f mm\n', base(2));
