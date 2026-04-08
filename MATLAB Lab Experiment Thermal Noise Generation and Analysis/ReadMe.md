# Thermal Noise Simulation and Analysis using MATLAB

## Objective

The objective of this experiment is to simulate and analyze thermal noise using MATLAB and visualize its characteristics in both time and frequency domains.

---

## Methodology

### 1. Thermal Noise Generation

Thermal noise (also known as Johnson-Nyquist noise) was generated using the following formula:

Noise amplitude = sqrt(4 * k * T * R * B)

Where:

* k = Boltzmann constant (1.38 × 10⁻²³ J/K)
* T = Temperature (300 K)
* R = Resistance (100 Ohms)
* B = Bandwidth (1 MHz)

A random Gaussian signal was generated using randn() to simulate thermal noise.

---

### 2. Time Domain Analysis

The generated thermal noise was plotted against time.

Observation:

* The signal appears completely random
* No periodic pattern is observed
* Amplitude fluctuates around zero

---

### 3. Power Spectral Density (PSD) Analysis

The Power Spectral Density (PSD) was calculated using the pwelch() function.

The PSD was plotted using a logarithmic frequency scale.

Observation:

* Noise power is distributed across frequencies
* The plot indicates nearly uniform distribution
* This confirms the white noise behavior

---

## Results

* Thermal noise behaves as a random signal in the time domain
* The amplitude varies unpredictably
* PSD shows that noise energy is spread over a wide frequency range

---

## Observations

* Increasing temperature increases noise power
* Increasing resistance increases noise amplitude
* Increasing bandwidth increases total noise energy
* The noise has no deterministic pattern

---

## Conclusion

This experiment demonstrates the characteristics of thermal noise in both time and frequency domains. Thermal noise is random and unavoidable in electronic systems. The PSD analysis confirms that thermal noise behaves like white noise, with power distributed over a wide range of frequencies.

---

## Experimentation

The following parameters can be modified to observe different results:

* Temperature (T)
* Resistance (R)
* Bandwidth (B)

Changing these values helps understand how physical parameters affect noise behavior.

---

## Files Included

* thermal_noise_experiment.m → MATLAB script
* README.md → Experiment description and analysis

---

## Author

Khaled Ahmed
