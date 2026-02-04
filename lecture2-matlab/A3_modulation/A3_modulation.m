% A3: Basic modulation by multiplication
% Student: Khaled Ahmed
% Student ID: 2314454

clear; close all; clc;

%% 1) Time vector
Fs = 20000;        % sampling frequency
T  = 0.1;          % duration (100 ms)
t  = 0:1/Fs:T-1/Fs;

%% 2) Baseband and carrier
fm = 100;          % message frequency (Hz)
fc = 2000;         % carrier frequency (Hz)

m = sin(2*pi*fm*t);    % baseband signal
c = cos(2*pi*fc*t);    % carrier signal

%% 3) Modulated signal
s = m .* c;            % modulation (multiplication)

%% 4) Plot baseband time domain
figure;
plot(t*1000, m);
grid on;
xlabel('Time [ms]');
ylabel('Amplitude');
title('A3: Baseband m(t)');
exportgraphics(gcf, 'A3_baseband_time.png', 'Resolution', 200);

%% 5) Plot passband time domain (first 5 ms)
index = (t <= 0.005);
figure;
plot(t(index)*1000, s(index));
grid on;
xlabel('Time [ms]');
ylabel('Amplitude');
title('A3: Passband s(t)');
exportgraphics(gcf, 'A3_passband_time.png', 'Resolution', 200);

%% 6) FFT of baseband
N = length(m);
M = fft(m);
f = (0:N-1)*(Fs/N);

halfN = floor(N/2);
f_half = f(1:halfN);

figure;
plot(f_half, abs(M(1:halfN)));
grid on;
xlabel('Frequency [Hz]');
ylabel('Magnitude');
title('A3: Spectrum of Baseband');
xlim([0 1000]);
exportgraphics(gcf, 'A3_baseband_spectrum.png', 'Resolution', 200);

%% 7) FFT of modulated signal
S = fft(s);

figure;
plot(f_half, abs(S(1:halfN)));
grid on;
xlabel('Frequency [Hz]');
ylabel('Magnitude');
title('A3: Spectrum of Modulated Signal');
xlim([0 5000]);
exportgraphics(gcf, 'A3_passband_spectrum.png', 'Resolution', 200);
