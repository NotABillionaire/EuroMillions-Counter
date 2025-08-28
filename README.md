🎲 EuroMillions Statistical Anomaly Detector

This project investigates the statistical fairness of the EuroMillions lottery by analyzing historical draw data and comparing it with simulated “perfect randomness.” The central aim is to identify potential biases, irregularities, or anomalies that might arise from:

Mechanical imperfections in draw machines

Human error in ball handling and recording

Deviations from theoretical probability distributions

By applying principles from probability theory, statistics, and simulation, we test whether real-world lottery results conform to the Law of Large Numbers and expected uniform distributions.

📂 Project Files

euromillions_counter.py
Counts how many times each EuroMillions number has been drawn historically.

Parses euro_millions_past_results.txt (full draw history).

Uses Counter to tally number frequencies.

Plots actual frequencies across balls 1–50 and stars 1–12.

fake_euromillions.py
Simulates a large number of “ideal” EuroMillions draws using Python’s RNG.

Generates 9,345 random draws (matching dataset size).

Tallies and plots simulated frequencies.

Provides a benchmark to compare against real-world draws.

📊 Theoretical Background
1. Law of Large Numbers (LLN)

As the number of draws → ∞, the frequency of each ball approaches equal probability:

𝑃
(
main ball
)
=
5
50
=
0.1
P(main ball)=
50
5
	​

=0.1
𝑃
(
lucky star
)
=
2
12
≈
0.1667
P(lucky star)=
12
2
	​

≈0.1667

For ~9,300 draws, the expected occurrences are:

Each main number ≈ 
9
,
300
×
0.1
=
930
9,300×0.1=930 appearances.

Each lucky star ≈ 
9
,
300
×
0.1667
≈
1550
9,300×0.1667≈1550 appearances.

2. Chi-Square Test for Uniformity

We measure whether observed frequencies differ significantly from expected frequencies:

𝜒
2
=
∑
(
𝑂
𝑖
−
𝐸
𝑖
)
2
𝐸
𝑖
χ
2
=∑
E
i
	​

(O
i
	​

−E
i
	​

)
2
	​


𝑂
𝑖
O
i
	​

 = observed count of ball 
𝑖
i

𝐸
𝑖
E
i
	​

 = expected count of ball 
𝑖
i

If 
𝜒
2
χ
2
 exceeds critical values, distribution may not be random.

3. Monte Carlo Simulation

The script fake_euromillions.py simulates thousands of draws.

Provides a “control” dataset.

Helps estimate the range of natural fluctuations in random systems.

Real results outside this range may indicate systematic bias.

4. Potential Sources of Bias

Even though lotteries are designed to be random, physical or human factors can introduce irregularities:

Slight differences in ball weight or wear.

Uneven airflow or mechanics in draw machines.

Loading procedures or operational errors.

Recording or publishing mistakes.

🚀 Workflow

Load real historical results from euro_millions_past_results.txt.

Count frequencies of each ball and star.

Run simulations to establish expected uniform distributions.

Compare observed vs expected with statistical tests and visualizations.

Flag anomalies that deviate beyond random variance.

📈 Example Outputs

Frequency plots of numbers 1–50.

Comparison bar charts: real vs simulated.

Chi-square statistics and p-values.

🎯 Goal

This project does not aim to predict future lottery results (which are theoretically random).
Instead, it seeks to:

Detect systematic biases or statistical anomalies.

Investigate whether mechanical or human imperfections skew outcomes.

Provide a reproducible methodology for lottery forensics.

🔧 Future Work

Extend analysis to Lucky Stars.

Apply Kolmogorov–Smirnov (KS) tests for distribution comparison.

Build anomaly heatmaps over time (yearly drift).

Automate with APIs to update after every draw.
