
function plotRobot(X, Z, L, phi, kappa)

    figure('Color','w');

    % Plot Section 1
    plot(X(1:100), Z(1:100), ...
        'b','LineWidth',4);
    hold on;

    % Plot Section 2
    plot(X(100:end), Z(100:end), ...
        'r','LineWidth',4);

    % Base position
    plot(0,0,'ko','MarkerFaceColor','k', ...
        'MarkerSize',8);

    % End-effector
    plot(X(end),Z(end),'ro', ...
        'MarkerFaceColor','r','MarkerSize',9);

    % Section connection
    plot(X(100),Z(100),'ko', ...
        'MarkerFaceColor','y','MarkerSize',8);

    % Labels
    text(0,0,'  Base','FontSize',11);
    text(X(100),Z(100),'  Section 1/2', ...
        'FontSize',10);
    text(X(end),Z(end),'  End-effector', ...
        'FontSize',11);

    % Axis labels
    xlabel('X (mm)');
    ylabel('Z (mm)');

    title('Two-Section Planar Continuum Robot');

    axis equal;
    grid on;
    box on;

    legend('Section 1','Section 2', ...
        'Base','End-effector','Joint');

end
