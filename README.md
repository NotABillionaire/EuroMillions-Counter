
# EuroMillions Statistical Anomaly Detector

This project investigates the statistical fairness of the EuroMillions lottery by analyzing historical draw data and comparing it with simulated random draws. The goal is to identify potential biases, irregularities, or anomalies that may result from human or mechanical error in the drawing process.

It is not a prediction tool, but a framework for testing randomness and applying statistical forensics to large-scale lottery data.

---

## Disclaimer

This software is intended for research and educational purposes only. It demonstrates practical applications of probability theory and statistics in detecting anomalies in data that should, by design, be random.

* No guarantee of prediction or financial gain is implied.
* The project is not affiliated with EuroMillions or any lottery operator.
* Users are expected to apply the software responsibly, legally, and ethically.
* We are not responsible for end-user actions, misuse, or gambling behavior.

By using this software, you acknowledge these terms and commit to using it for responsible research or educational purposes.

---

## Features

* Frequency analysis of historical EuroMillions results
* Simulation of large-scale random draws for benchmarking
* Chi-Square test for statistical fairness
* Monte Carlo simulation to evaluate variance in truly random systems
* Visualization of real vs simulated results
* Identification of underperforming and overperforming numbers relative to expectation

---

## Theoretical Background

**Law of Large Numbers (LLN)**
As the number of draws increases, the frequency of each ball approaches its theoretical probability. For EuroMillions:

* Main numbers: 5 selections from 50 → expected probability per ball = `5/50 = 0.1`
* Lucky Stars: 2 selections from 12 → expected probability per star ≈ `2/12 = 0.1667`

**Chi-Square Test**
A statistical test to measure deviation from expected uniformity:

```
χ² = Σ ( (Oi - Ei)² / Ei )
```

Where:

* `Oi` = observed frequency of number i
* `Ei` = expected frequency of number i

**Monte Carlo Simulation**
Simulated draws provide a control dataset representing ideal randomness. Comparing real data against simulated results highlights potential irregularities.

**Sources of Bias**
Even though lottery draws are designed to be random, biases can emerge from:

* Manufacturing tolerances of balls (weight, size, wear)
* Mechanical quirks of machines (airflow, turbulence, paddles)
* Human error in ball loading or recording
* Procedural inconsistencies or oversight

---

## Installation

Clone the repository:

```bash
git clone https://github.com/NotABillionaire/EuroMillions-Counter.git
cd euromillions-anomaly-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run analysis on historical EuroMillions results:

```bash
python euromillions_counter.py
```

Simulate random draws to establish a baseline:

```bash
python fake_euromillions.py
```

Results include frequency counts, plots, and statistical metrics.

---

## Example Outputs

* Frequency distribution of each ball (1–50) and Lucky Star (1–12)
* Side-by-side comparisons of real vs simulated data
* Identification of statistically significant deviations
* Chi-square statistics with p-values
* Plots showing “hot” and “cold” numbers relative to expectation

---

## Roadmap

* Extend analysis to Lucky Stars in more depth
* Add yearly drift and anomaly trend plots
* Implement Kolmogorov–Smirnov (KS) tests for distribution distance
* Automate data ingestion from APIs for live updates
* Generate anomaly reports in real time


