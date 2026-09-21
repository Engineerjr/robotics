import matplotlib.pyplot as plt
import numpy as np


def torsional_analysis(
    outer_radius_mm=10.0,  # Outer radius in mm
    inner_radius_mm=0.0,  # Inner radius in mm (0 for solid, >0 for hollow/soft tube)
    length_mm=100.0,  # Length of actuator/rod in mm
    shear_modulus_MPa=1.5,  # Shear modulus G (e.g., ~1.5 MPa for soft silicone/elastomer)
    max_torque_Nmm=50.0,  # Maximum applied torque in N·mm
):
    # Convert dimensions to meters
    R_out = outer_radius_mm * 1e-3
    R_in = inner_radius_mm * 1e-3
    L = length_mm * 1e-3
    G = shear_modulus_MPa * 1e6
    T_max = max_torque_Nmm * 1e-3

    # Polar Moment of Inertia (J) for solid or hollow cylinder
    J = (np.pi / 2) * (R_out**4 - R_in**4)

    # Torque array
    torque_array = np.linspace(0, T_max, 100)

    # 1. Calculate Angle of Twist vs Torque: theta = (T * L) / (G * J)
    theta_rad = (torque_array * L) / (G * J)
    theta_deg = np.degrees(theta_rad)

    # 2. Calculate Shear Stress Distribution across Radius at Peak Torque: tau = (T * r) / J
    r_profile = np.linspace(R_in, R_out, 100)
    shear_stress_peak_kPa = ((T_max * r_profile) / J) / 1e3  # Convert to kPa

    # --- Plotting ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Plot 1: Torque vs Twist Angle
    ax1.plot(torque_array * 1e3, theta_deg, color="#1f77b4", linewidth=2)
    ax1.set_title("Torque vs. Twist Angle", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Applied Torque $T$ (N·mm)", fontsize=10)
    ax1.set_ylabel("Twist Angle $\\theta$ (degrees)", fontsize=10)
    ax1.grid(True, linestyle="--", alpha=0.6)

    # Plot 2: Shear Stress Profile
    ax2.plot(
        r_profile * 1e3, shear_stress_peak_kPa, color="#d62728", linewidth=2
    )
    ax2.set_title(
        f"Radial Shear Stress Profile (at T = {max_torque_Nmm:.1f} N·mm)",
        fontsize=12,
        fontweight="bold",
    )
    ax2.set_xlabel("Radial Distance $r$ (mm)", fontsize=10)
    ax2.set_ylabel("Shear Stress $\\tau$ (kPa)", fontsize=10)
    ax2.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.show()

    # Print summary metrics
    torsional_rigidity = G * J
    max_shear_stress_kPa = shear_stress_peak_kPa[-1]
    max_twist_deg = theta_deg[-1]

    print("=== TORSIONAL ANALYSIS SUMMARY ===")
    print(f"Polar Moment of Inertia (J): {J:.4e} m^4")
    print(f"Torsional Rigidity (G*J):    {torsional_rigidity:.4f} N·m²")
    print(
        f"Max Twist Angle at Peak T:   {max_twist_deg:.2f}° ({theta_rad[-1]:.3f} rad)"
    )
    print(f"Max Outer Shear Stress:      {max_shear_stress_kPa:.2f} kPa")


if __name__ == "__main__":
    # Example parameter run (customizable for soft silicone tubes or solid rods)
    torsional_analysis(
        outer_radius_mm=12.0,
        inner_radius_mm=4.0,  # Hollow core typical in soft pneumatic actuators
        length_mm=80.0,
        shear_modulus_MPa=0.8,  # Typical G for flexible elastomers (~0.5 - 2 MPa)
        max_torque_Nmm=30.0,
    )