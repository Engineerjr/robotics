
function [x, z, theta] = constantCurvature(L, phi, kappa, N)

    % Convert equilibrium angle to radians
    phi = deg2rad(phi);

    % Signed curvature
    k = kappa * cos(phi);

    % Bending angle
    theta = k * L;

    % Arc-length discretization
    s = linspace(0, L, N);

    % Calculate local coordinates
    if abs(k) < 1e-10

        % Straight section
        x = zeros(1, N);
        z = s;

    else

        x = (1 - cos(k*s)) / k;
        z = sin(k*s) / k;

    end

end
