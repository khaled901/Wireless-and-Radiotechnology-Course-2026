# Noise Addition and Removal Using MATLAB

## Objective

The objective of this experiment is to simulate the process of adding noise to a signal and removing it using a low-pass filter in MATLAB. This helps in understanding how noise affects signals and how filtering techniques can improve signal quality.

---

## Methodology

### 1. Signal Generation

A sinusoidal signal was generated using the following parameters:

* Sampling frequency: 1000 Hz
* Signal frequency: 5 Hz
* Amplitude: 1

The signal is defined as:

sin(2 * pi * f * t)

---

### 2. Adding Noise

Gaussian white noise was added to the original signal using MATLAB’s random function. The noise level was controlled using a parameter:

noise_level = 0.5

This resulted in a distorted version of the original signal.

---

### 3. Noise Removal

A low-pass Butterworth filter was applied to remove high-frequency noise.

* Filter type: Low-pass Butterworth
* Filter order: 4
* Cutoff frequency: 10 Hz

The filter was implemented using:

* butter() function for filter design
* filtfilt() function for zero-phase filtering

---

## Results

* The original signal appeared smooth and periodic
* The noisy signal showed significant distortion
* The filtered signal became smoother and closer to the original signal

The filtering process successfully reduced high-frequency noise.

---

## Observations

* Increasing the noise level increases signal distortion
* The low-pass filter effectively removes high-frequency noise
* Some smoothing occurs after filtering, causing slight loss of details
* The filtered signal is not identical to the original signal

---

## Conclusion

This experiment demonstrates the impact of noise on signals and the effectiveness of filtering techniques. While low-pass filters can significantly reduce noise, they may also slightly distort the signal. Therefore, there is always a trade-off between noise reduction and signal preservation.

---

## Experimentation

Different parameters can be modified to observe their effects:

* Increase or decrease noise_level
* Change cutoff_frequency
* Modify signal frequency

These changes help in understanding the behavior of filters in different scenarios.

---

## Files Included

* noise_signal_experiment.m → MATLAB script for the experiment
* README.md → Description and evaluation of the experiment

---

## Author

Khaled Ahmed
