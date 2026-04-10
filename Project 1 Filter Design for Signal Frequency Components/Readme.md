# Filter Design for Frequency Isolation

This project focuses on designing appropriate filters to isolate specific frequency components from a composite input signal.

## Input Signal

The input signal is composed of multiple sine waves:

Input Signal =
A1 sin(2π·100·t) + A2 sin(2π·200·t) + A3 sin(2π·300·t) + A4 sin(2π·400·t)

## Objective

To select suitable filter types (Low Pass, High Pass, Band Pass, Band Stop) and define cutoff frequencies to isolate desired frequency components.

## Filter Design Table

| Frequency Component        | Filter Type      | Cutoff Frequency/Frequencies |
| -------------------------- | ---------------- | ---------------------------- |
| 100 Hz                     | Low Pass Filter  | 150 Hz                       |
| 400 Hz                     | High Pass Filter | 350 Hz                       |
| 100 Hz and 200 Hz          | Low Pass Filter  | 250 Hz                       |
| 200 Hz                     | Band Pass Filter | 150 Hz to 250 Hz             |
| 300 Hz                     | Band Pass Filter | 250 Hz to 350 Hz             |
| 300 Hz and 400 Hz          | High Pass Filter | 250 Hz                       |
| 200 Hz and 300 Hz          | Band Pass Filter | 150 Hz to 350 Hz             |
| 200 Hz, 300 Hz, and 400 Hz | High Pass Filter | 150 Hz                       |
| 100 Hz and 400 Hz          | Band Stop Filter | 150 Hz to 350 Hz             |

## Notes

* Cutoff frequencies are chosen to separate the desired components from neighboring frequencies.
* Band Pass Filters are used to isolate specific frequency ranges.
* Band Stop Filters are used to remove unwanted frequency ranges.

## Author

Khaled Ahmed
