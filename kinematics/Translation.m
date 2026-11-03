% Clear workspace and figure
clear; clc; clf;

%% 1. Define Parameters
% Position of the point in the original (base) coordinate frame
P_old = [5; 4; 3]; 

% Origin shift (translation vector d) of the new coordinate system
d = [2; 1; 1]; 

% Calculate the position of the point in the new shifted coordinate system
P_new = P_old - d;

%% 2. 3D Visualization
figure('Color', 'white');
hold on;
grid on;
axis equal;
view(3);

% --- Plot Original Coordinate Frame (Old Origin at [0,0,0]) ---
quiver3(0,0,0, 2,0,0, 'r', 'LineWidth', 2, 'MaxHeadSize', 0.5); 
quiver3(0,0,0, 0,2,0, 'g', 'LineWidth', 2, 'MaxHeadSize', 0.5); 
quiver3(0,0,0, 0,0,2, 'b', 'LineWidth', 2, 'MaxHeadSize', 0.5); 
text(2.2, 0, 0, 'X_{old}', 'Color', 'r', 'FontSize', 11, 'FontWeight', 'bold');
text(0, 2.2, 0, 'Y_{old}', 'Color', 'g', 'FontSize', 11, 'FontWeight', 'bold');
text(0, 0, 2.2, 'Z_{old}', 'Color', 'b', 'FontSize', 11, 'FontWeight', 'bold');

% --- Plot Shifted Coordinate Frame (New Origin at d) ---
quiver3(d(1),d(2),d(3), 2,0,0, 'r--', 'LineWidth', 1.5, 'MaxHeadSize', 0.5);
quiver3(d(1),d(2),d(3), 0,2,0, 'g--', 'LineWidth', 1.5, 'MaxHeadSize', 0.5);
quiver3(d(1),d(2),d(3), 0,0,2, 'b--', 'LineWidth', 1.5, 'MaxHeadSize', 0.5);
text(d(1)+2.2, d(2), d(3), 'X_{new}', 'Color', 'r', 'FontSize', 11);
text(d(1), d(2)+2.2, d(3), 'Y_{new}', 'Color', 'g', 'FontSize', 11);
text(d(1), d(2), d(3)+2.2, 'Z_{new}', 'Color', 'b', 'FontSize', 11);

% --- Plot the Origin Shift Vector (d) ---
quiver3(0, 0, 0, d(1), d(2), d(3), 0, 'k:', 'LineWidth', 1.5);
text(d(1)/2, d(2)/2, d(3)/2, '  Shift (d)', 'FontSize', 10, 'Color', 'k', 'FontWeight', 'bold');

% --- Plot the Point P ---
plot3(P_old(1), P_old(2), P_old(3), 'ko', 'MarkerSize', 8, 'MarkerFaceColor', 'magenta');
point_label = sprintf('  Point P\n  Old: [%.1f, %.1f, %.1f]\n  New: [%.1f, %.1f, %.1f]', ...
    P_old(1), P_old(2), P_old(3), P_new(1), P_new(2), P_new(3));
text(P_old(1), P_old(2), P_old(3), point_label, 'FontSize', 10, 'FontWeight', 'bold');

% --- Plot configuration ---
xlabel('X Axis'); ylabel('Y Axis'); zlabel('Z Axis');
title('Coordinate System Origin Shift and Point Transformation', 'FontSize', 12);
xlim([-1, 7]); ylim([-1, 6]); zlim([-1, 5]);
view(45, 30);