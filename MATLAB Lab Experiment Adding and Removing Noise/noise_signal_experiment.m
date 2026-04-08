clc;
clear;
close all;

% Parameters
fs = 1000;              % Sampling frequency in Hz
t = 0:1/fs:1;           % Time vector
f_signal = 5;           % Frequency of the sinusoidal signal in Hz
amplitude = 1;          % Amplitude of the sinusoidal signal

% Generate original sinusoidal signal
original_signal = amplitude * sin(2 * pi * f_signal * t);

% Plot original signal
figure;
plot(t, original_signal, 'b', 'LineWidth', 1.5);
title('Original Sinusoidal Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

% Add Gaussian white noise
noise_level = 0.5;      % Noise level
noise = noise_level * randn(size(t));
noisy_signal = original_signal + noise;

% Plot original and noisy signals
figure;
plot(t, original_signal, 'b', 'LineWidth', 1.5);
hold on;
plot(t, noisy_signal, 'r');
title('Original vs Noisy Signal');
xlabel('Time (s)');
ylabel('Amplitude');
legend('Original Signal', 'Noisy Signal');
grid on;

% Remove noise using a low-pass Butterworth filter
cutoff_frequency = 10;      % Cutoff frequency in Hz
filter_order = 4;           % Filter order

[b, a] = butter(filter_order, cutoff_frequency / (fs / 2), 'low');
filtered_signal = filtfilt(b, a, noisy_signal);

% Plot original, noisy, and filtered signals
figure;
plot(t, original_signal, 'b', 'LineWidth', 1.5);
hold on;
plot(t, noisy_signal, 'r');
plot(t, filtered_signal, 'g', 'LineWidth', 1.5);

title('Original, Noisy, and Filtered Signals');
xlabel('Time (s)');
ylabel('Amplitude');

legend('Original Signal', 'Noisy Signal', 'Filtered Signal');
grid on;