import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def hyperelastic_torsion_analysis(
    outer_radius_mm=12.0,
    inner_radius_mm=4.0,
    length_mm=80.0,
    max_twist_deg=180.0,  # Max rotation angle to analyze
    # Yeoh Material Parameters for Silicone (e.g., Ecoflex or Dragon Skin)
    C10_MPa=0.15,  # Initial shear modulus ~ 2*C10 = 0.3 MPa
    C20_MPa=-0.005,  # Softening term at moderate strain
    C30_MPa=0.001,  # Strain-stiffening term at large strain
):
    # Convert inputs to SI units (meters, MPa to Pa)
    R_out = outer_radius_mm * 1e-3
    R_in = inner_radius_mm * 1e-3
    L = length_mm * 1e-3
    phi_max = np.radians(max_twist_deg) / L

    C10 = C10_MPa * 1e6
    C20 = C20_MPa * 1e6
    C30 = C30_MPa * 1e6

    # Function for Yeoh non-linear shear stress tau(gamma)
    def yeoh_shear_stress(gamma):
        # gamma is simple shear strain r * phi
        return 2 * gamma * (C10 + 2 * C20 * (gamma**2) + 3 * C30 * (gamma**4))

    # Array of twist per unit length (phi)
    phi_array = np.linspace(0.001, phi_max, 100)
    theta_deg = np.degrees(phi_array * L)

    # 1. Torque evaluation via numerical integration across the cross-section
    torque_hyperelastic = []
    torque_linear = []
    G_initial = 2 * C10  # Initial tangent shear modulus

    # Polar moment for linear comparison
    J = (np.pi / 2) * (R_out**4 - R_in**4)

    for phi in phi_array:

        # Integrand for Torque: tau(r * phi) * r^2 * 2 * pi
        def torque_integrand(r):
            gamma = r * phi
            return 2 * np.pi * yeoh_shear_stress(gamma) * (r**2)

        T_hyper, _ = quad(torque_integrand, R_in, R_out)
        torque_hyperelastic.append(T_hyper * 1e3)  # N*mm

        # Linear Hookean prediction for comparison
        T_lin = (G_initial * J * phi) * 1e3  # N*mm
        torque_linear.append(T_lin)

    torque_hyperelastic = np.array(torque_hyperelastic)
    torque_linear = np.array(torque_linear)

    # 2. Stress profile at maximum twist angle
    r_profile = np.linspace(R_in, R_out, 100)
    gamma_peak = r_profile * phi_max
    tau_peak_hyper = yeoh_shear_stress(gamma_peak) / 1e3  # kPa
    tau_peak_linear = (G_initial * gamma_peak) / 1e3  # kPa

    # --- Plotting ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Plot 1: Non-Linear Torque vs Twist
    ax1.plot(
        theta_deg,
        torque_hyperelastic,
        color="#1f77b4",
        linewidth=2.5,
        label="Yeoh Hyperelastic",
    )
    ax1.plot(
        theta_deg,
        torque_linear,
        color="gray",
        linestyle="--",
        linewidth=1.5,
        label="Linear Elastic (Hookean)",
    )
    ax1.set_title(
        "Torque vs. Twist Angle (Large Strain)", fontsize=12, fontweight="bold"
    )
    ax1.set_xlabel("Twist Angle $\\theta$ (degrees)", fontsize=10)
    ax1.set_ylabel("Applied Torque $T$ (N·mm)", fontsize=10)
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend()

    # Plot 2: Shear Stress Profile Across Wall Thickness
    ax2.plot(
        r_profile * 1e3,
        tau_peak_hyper,
        color="#d62728",
        linewidth=2.5,
        label=f"Yeoh at $\\theta$ = {max_twist_deg:.0f}°",
    )
    ax2.plot(
        r_profile * 1e3,
        tau_peak_linear,
        color="gray",
        linestyle="--",
        linewidth=1.5,
        label="Linear Model",
    )
    ax2.set_title(
        f"Radial Shear Stress Profile (at $\\theta = {max_twist_deg:.0f}^\circ$)",
        fontsize=12,
        fontweight="bold",
    )
    ax2.set_xlabel("Radial Distance $r$ (mm)", fontsize=10)
    ax2.set_ylabel("Shear Stress $\\tau$ (kPa)", fontsize=10)
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    hyperelastic_torsion_analysis(
        outer_radius_mm=12.0,
        inner_radius_mm=4.0,
        length_mm=80.0,
        max_twist_deg=180.0,
        C10_MPa=0.12,  # Initial shear stiffness
        C20_MPa=-0.002,  # Softening
        C30_MPa=0.0005,  # Stiffening
    )