
function [X, Z] = transformSection(x, z, base, alpha)

    % Rotation matrix in the XZ plane
    R = [ cos(alpha),  sin(alpha);
         -sin(alpha),  cos(alpha)];

    % Local coordinates
    P = [x; z];

    % Transform to global coordinates
    P_global = R * P;

    % Add the starting position
    P_global = P_global + base;

    % Extract global coordinates
    X = P_global(1,:);
    Z = P_global(2,:);

end
