clc;
clear;
close all;

% Parameters
B = 1e6;          % Bandwidth (1 MHz)
R = 100;          % Resistance (Ohms)
T = 300;          % Temperature (Kelvin)
k = 1.38e-23;     % Boltzmann constant

n_samples = 10000;

% Time vector
time = 0 : 1/B : (n_samples-1) / B;

% Generate Thermal Noise
thermal_noise = sqrt(4 * k * T * R * B) * randn(1, n_samples);

% Plot in time domain
figure;
plot(time, thermal_noise);
title('Thermal Noise in Time Domain');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

% Power Spectral Density (PSD)
[psd, freq] = pwelch(thermal_noise, [], [], [], B);

% Plot PSD
figure;
semilogx(freq, 10*log10(psd));
title('Power Spectral Density of Thermal Noise');
xlabel('Frequency (Hz)');
ylabel('Power/Frequency (dB/Hz)');
grid on;