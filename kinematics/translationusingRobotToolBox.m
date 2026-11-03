% --- Parameters ---
% Original Point P
P = [2; 3; 4]; 

% Translation / Origin Shift vector d
d = [4; -1; 2]; 

% Calculate new position (P' = P + d)
P_new = P + d;

% --- Plotting Setup ---
figure('Name', 'Coordinate Transformation: Translation', 'Color', 'w');
hold on; grid on; axis equal;
view(3); % Set 3D view

% 1. Plot the Global Coordinate Frame (Origin at 0,0,0)
quiver3(0,0,0, 1,0,0, 'r', 'LineWidth', 2, 'MaxHeadSize', 0.5); % X-axis
quiver3(0,0,0, 0,1,0, 'g', 'LineWidth', 2, 'MaxHeadSize', 0.5); % Y-axis
quiver3(0,0,0, 0,0,1, 'b', 'LineWidth', 2, 'MaxHeadSize', 0.5); % Z-axis
text(1.2, 0, 0, 'X_{global}', 'Color', 'r', 'FontWeight', 'bold');
text(0, 1.2, 0, 'Y_{global}', 'Color', 'g', 'FontWeight', 'bold');
text(0, 0, 1.2, 'Z_{global}', 'Color', 'b', 'FontWeight', 'bold');

% 2. Plot Original Point P
plot3(P(1), P(2), P(3), 'ko', 'MarkerSize', 8, 'MarkerFaceColor', 'k');
text(P(1), P(2), P(3)+0.3, 'Original Point P', 'FontWeight', 'bold');

% 3. Plot Translation Vector d (from P to P_new)
% We draw it starting from P to show the shift
quiver3(P(1), P(2), P(3), d(1), d(2), d(3), 0, ...
    'Color', [0.5 0.5 0.5], 'LineWidth', 2, 'LineStyle', '--', 'MaxHeadSize', 0.3);
text(P(1)+d(1)/2, P(2)+d(2)/2, P(3)+d(3)/2, 'Translation Vector d', 'Color', [0.3 0.3 0.3]);

% 4. Plot New Point P'
plot3(P_new(1), P_new(2), P_new(3), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
text(P_new(1), P_new(2), P_new(3)+0.3, 'New Point P''', 'FontWeight', 'bold', 'Color', 'r');

% 5. Add a "ghost" frame at the new point to show it shifted
% (Optional: uncomment to visualize the frame shifting instead of the point)
% quiver3(P_new(1), P_new(2), P_new(3), 1,0,0, 'r', 'LineWidth', 1);
% quiver3(P_new(1), P_new(2), P_new(3), 0,1,0, 'g', 'LineWidth', 1);
% quiver3(P_new(1), P_new(2), P_new(3), 0,0,1, 'b', 'LineWidth', 1);

% Formatting
xlabel('X'); ylabel('Y'); zlabel('Z');
title('Visualization of Point Translation (P'' = P + d)');
legend('', '', '', 'Original Point', 'Translation Vector', 'New Point', 'Location', 'best');
xlim([-1 8]); ylim([-2 5]); zlim([-1 7]);
hold off;