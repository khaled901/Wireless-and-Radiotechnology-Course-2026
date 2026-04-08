clc;
clear;
close all;

% Parameters
fs = 1000;                  % Sampling frequency in Hz
t = 0:1/fs:1;               % Time vector
f_c = 50;                   % Carrier frequency in Hz

SNR_value_1 = 10;           % SNR value in dB
SNR_value_2 = 5;            % SNR value in dB
SNR_value_3 = 0;            % SNR value in dB
SNR_value_4 = -5;           % SNR value in dB

snr_values = [SNR_value_1 SNR_value_2 SNR_value_3 SNR_value_4];

% Generate binary message signal
message_signal = randi([0 1], 1, length(t));

% Carrier signal
carrier = sin(2 * pi * f_c * t);

% ASK Modulation
modulated_signal = message_signal .* carrier;

% Plot original message and modulated signal
figure;
subplot(2,1,1);
plot(t, message_signal, 'LineWidth', 1.5);
title('Binary Message Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

subplot(2,1,2);
plot(t, modulated_signal, 'LineWidth', 1.5);
title('ASK Modulated Signal');
xlabel('Time (s)');
ylabel('Amplitude');
grid on;

% Loop for different SNR values
for i = 1:length(snr_values)
    current_snr = snr_values(i);
    
    % Add Gaussian white noise
    received_signal = awgn(modulated_signal, current_snr, 'measured');
    
    % Coherent demodulation
    demodulated_temp = received_signal .* carrier;
    
    % Low-pass filter
    cutoff_frequency = 20;
    filter_order = 4;
    [b, a] = butter(filter_order, cutoff_frequency/(fs/2), 'low');
    demodulated_filtered = filtfilt(b, a, demodulated_temp);
    
    % Threshold detection
    demodulated_signal = demodulated_filtered > 0.1;
    
    % Plot received and demodulated signals
    figure;
    
    subplot(2,1,1);
    plot(t, received_signal);
    title(['Received Signal at SNR = ' num2str(current_snr) ' dB']);
    xlabel('Time (s)');
    ylabel('Amplitude');
    grid on;
    
    subplot(2,1,2);
    plot(t, demodulated_signal, 'LineWidth', 1.5);
    title(['Demodulated Signal at SNR = ' num2str(current_snr) ' dB']);
    xlabel('Time (s)');
    ylabel('Amplitude');
    ylim([-0.2 1.2]);
    grid on;
end