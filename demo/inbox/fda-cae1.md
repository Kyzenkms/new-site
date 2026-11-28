> Units per official Raisoni FY NEP syllabus book (Foundation of Data Analytics).

# FDA — Foundation of Data Analytics (CAE-1 Notes)

**Units covered:** 1, 2, 3 (CAE-1 portion)

---

# Unit 1: Concepts and Statistical Analysis

## 1.1 Topics
- Buzzwords of data science
- Infographic representation of terminologies
- Analysis vs Analytics
- Types of data analytics (descriptive, diagnostic, predictive, prescriptive)
- Quantitative vs qualitative data
- Central tendency: mean, median, mode
- Measures of variation: quartiles, variance, range

## 1.2 Explanations & Key Definitions

### Buzzwords of data science
Common terms you should know and be able to define in one line:
- **Data**: raw facts and figures (unprocessed).
- **Information**: processed, meaningful data.
- **Knowledge**: insights derived from information.
- **Big Data**: data too large/fast/varied for traditional tools (the 3 Vs: Volume, Velocity, Variety).
- **Data Science**: field combining statistics, computing, and domain knowledge to extract insights from data.
- **Machine Learning**: algorithms that learn patterns from data to make predictions.
- **Data Mining**: discovering patterns in large datasets.

### Analysis vs Analytics
| Analysis | Analytics |
|---|---|
| Breaks data down into parts to **understand the past** | Uses data, stats, models to **predict and optimize the future** |
| Answers "what happened?" | Answers "why did it happen, what will happen, what should we do?" |
| One-time, backward-looking | Ongoing, forward-looking, often automated |
| E.g. dissecting last month's sales report | E.g. recommendation engine, fraud detection |

### Types of data analytics (learn the 4 D's + what question each answers)
| Type | Question | Example | Complexity |
|---|---|---|---|
| **Descriptive** | *What happened?* | Dashboard of monthly sales; average marks of a class | Low |
| **Diagnostic** | *Why did it happen?* | Sales dropped because of a price hike (drill-down, correlation) | Medium |
| **Predictive** | *What will happen?* | Next month's sales forecast using regression | High |
| **Prescriptive** | *What should we do?* | Optimal pricing recommendation, route optimisation | Highest |

Memory trick: **D-D-P-P** → Describe, Diagnose, Predict, Prescribe.

### Quantitative vs qualitative data
| Quantitative (numeric) | Qualitative (categorical) |
|---|---|
| Numbers, measurable, can do arithmetic | Categories, labels, descriptions |
| **Discrete**: countable (no. of students) | **Nominal**: no order (gender, blood group) |
| **Continuous**: any value in a range (height, temperature) | **Ordinal**: has order (rank: 1st/2nd/3rd, ratings: poor/good/excellent) |

### Central tendency
- **Mean (arithmetic mean)** — average of all values.
$$\bar{x} = \frac{\sum x_i}{n}$$
- **Median** — middle value of the **sorted** data.
  - n odd: median = middle value; n even: average of the two middle values.
- **Mode** — value occurring most frequently (a dataset can have more than one mode, or none).

**Empirical relation (approx, for near-symmetric data):** Mean − Mode ≈ 3(Mean − Median)

**When to use which:** mean is affected by outliers (use median for skewed data like income); mode is used for categorical data (most popular product).

### Measures of variation (spread/dispersion)
- **Range** = max − min. Simple but sensitive to outliers.
- **Quartiles** — divide sorted data into 4 equal parts: Q1 (25th percentile), Q2 = median (50th), Q3 (75th percentile).
  - Position of Q1 = (n+1)/4, Q3 = 3(n+1)/4 (using the common position formula; values in between use interpolation).
- **Interquartile range (IQR)** = Q3 − Q1 — spread of the middle 50%; robust to outliers.
- **Population variance**: $$\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$$
- **Sample variance**: $$s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$$ (note: divide by **n−1** for a sample!)
- **Standard deviation**: $$\sigma = \sqrt{\sigma^2},\quad s = \sqrt{s^2}$$ — spread in the same units as the data.

## 1.3 Worked Examples

**Ex 1 — Mean, median, mode.** Data: 5, 2, 9, 5, 7 (marks).
- Mean = (5+2+9+5+7)/5 = 28/5 = **5.6**
- Sorted: 2, 5, 5, 7, 9 → n = 5 (odd) → median = **5**
- Mode = **5** (appears twice, most frequent)

**Ex 2 — Sample variance & std dev.** Data: 10, 12, 14, 16, 18.
- Mean = 70/5 = 14
- Deviations: −4, −2, 0, 2, 4 → squares: 16, 4, 0, 4, 16 → sum = 40
- Sample variance s² = 40/(5−1) = **10**; sample std dev s = √10 ≈ **3.16**
- Range = 18 − 10 = **8**

**Ex 3 — Quartiles & IQR.** Data: 3, 7, 8, 5, 12, 14, 21, 15, 18, 14 (n = 10).
- Sorted: 3, 5, 7, 8, 12, 14, 14, 15, 18, 21
- Q2 (median) = (12+14)/2 = 13
- Q1 position = (10+1)/4 = 2.75 → value = 5 + 0.75×(7−5) = **6.5**
- Q3 position = 3×(10+1)/4 = 8.25 → value = 15 + 0.25×(18−15) = **15.75**
- IQR = 15.75 − 6.5 = **9.25**

## 1.4 Likely CAE-1 Questions (with model answers)

1. **Differentiate between analysis and analytics.** → Analysis breaks data down to understand *what happened* (backward-looking, one-time); analytics applies statistics and models to data to *predict and prescribe actions* (forward-looking, ongoing, often automated).
2. **Explain the four types of data analytics with one example each.** → Descriptive (what happened — sales dashboard), diagnostic (why — drill-down showed price-hike caused drop), predictive (what will happen — sales forecast), prescriptive (what to do — recommended pricing).
3. **Distinguish between quantitative and qualitative data with examples.** → Quantitative is numeric (discrete: no. of students; continuous: height); qualitative is categorical (nominal: blood group; ordinal: satisfaction rating).
4. **Define mean, median, mode. When is median preferred over mean?** → Definitions as above; median is preferred when data are skewed or contain outliers (e.g. income), since it isn't pulled by extreme values.
5. **What are quartiles? Define IQR.** → Q1, Q2 (median), Q3 split sorted data into quarters; IQR = Q3 − Q1 measures spread of the middle 50%, robust to outliers.
6. **Write the formulas for population variance and sample variance. Why n−1 in the sample formula?** → σ² = Σ(x−μ)²/N; s² = Σ(x−x̄)²/(n−1). Dividing by n−1 corrects bias (Bessel's correction) because the sample mean is estimated from the same data, making s² an unbiased estimator of σ².
7. **A dataset has mean 50 and mode 44. Estimate the median using the empirical relation.** → Mean − Mode ≈ 3(Mean − Median) → 50 − 44 = 3(50 − M) → 6 = 150 − 3M → 3M = 144 → **Median = 48**.

## 1.5 Unit 1 Quick Revision
- 4 analytics types: **D-D-P-P** (Describe/Diagnose/Predict/Prescribe).
- Data types: discrete vs continuous; nominal vs ordinal.
- Mean = Σx/n; median = middle of sorted data; mode = most frequent.
- Mean − Mode ≈ 3(Mean − Median).
- Range = max − min; IQR = Q3 − Q1; s² = Σ(x−x̄)²/(n−1); s = √s².

---

# Unit 2: Data Preparation & Identification of Trends

## 2.1 Topics
- Data preparation (importing data: CSV, Excel, spreadsheets, website tables, database tables)
- Duplicate data
- Extracting values from a string using text functions: LEFT, RIGHT, LEN, MID, FIND
- Identifying trends in data

## 2.2 Explanations & Key Definitions

### Data preparation
The process of **cleaning, transforming, and structuring raw data** so it is fit for analysis. Often called the most time-consuming step (~60–80% of an analyst's time). Typical steps:
1. **Collect/import** data from sources.
2. **Clean**: remove/fix duplicates, handle missing values, correct data types.
3. **Transform**: standardise formats, derive new columns, merge datasets.
4. **Validate**: check ranges, consistency, and outliers.

### Importing data (common sources)
| Source | How (Excel/sheets) |
|---|---|
| CSV file | Data → From Text/CSV |
| Excel workbook | Data → From File → From Workbook |
| Spreadsheets (Google Sheets) | Import / IMPORTRANGE |
| Website tables (HTML tables) | Data → From Web (paste URL) |
| Database tables | Data → From Database (SQL connector / ODBC) |

Key file note: **CSV = Comma-Separated Values** — plain text, values separated by commas, one record per line.

### Duplicate data
Rows that are **exact or near-exact copies** of another row. They inflate counts, distort means and totals, and must be removed (Excel: Data → Remove Duplicates). Causes: data entry errors, merging datasets, system glitches.

### Text functions (Excel/sheets) — learn signatures + one example each
| Function | Syntax | What it does | Example |
|---|---|---|---|
| LEFT | `=LEFT(text, n)` | First n characters | `=LEFT("Hello",3)` → "Hel" |
| RIGHT | `=RIGHT(text, n)` | Last n characters | `=RIGHT("Hello",2)` → "lo" |
| LEN | `=LEN(text)` | Number of characters | `=LEN("Data")` → 4 |
| MID | `=MID(text, start, n)` | n characters starting at position `start` | `=MID("Hello",2,3)` → "ell" |
| FIND | `=FIND(find_text, text)` | Position where `find_text` starts (1-based) | `=FIND("l","Hello")` → 3 |

Combined use: extract the part after a delimiter, e.g. from "Amit-Kumar", `=RIGHT(A1, LEN(A1)-FIND("-",A1))` → "Kumar".

### Identifying trends in data
A **trend** is a long-term directional movement in data (increasing, decreasing, flat). Methods:
- **Line/time-series chart**: plot values over time; visually inspect slope.
- **Moving average**: smooth short-term noise to reveal underlying direction.
- **Trendline (regression)**: fit a line; positive slope = upward trend, negative = downward, ~zero = no trend.
- **Sparkline / conditional formatting**: quick visual cues in tables.
- Compare **period-over-period growth %** = (new − old)/old × 100.

**Types of patterns:** trend (long-term direction), seasonality (repeating fixed-period cycles), noise/random fluctuation.

## 2.3 Worked Examples

**Ex 1 — Text functions.** Cell A1 = "2024-India".
- `=LEFT(A1,4)` → **"2024"**
- `=RIGHT(A1,5)` → **"India"**
- `=LEN(A1)` → **10**
- `=MID(A1,6,5)` → **"India"**
- `=FIND("-",A1)` → **5**

**Ex 2 — Extract domain from email.** A1 = "user@example.com".
- `=MID(A1, FIND("@",A1)+1, LEN(A1))` → starts after "@" → **"example.com"**
- Explanation: FIND("@",A1) = 5, so MID starts at 6 and takes enough characters (LEN = 16) → "example.com".

**Ex 3 — Trend.** Monthly sales (₹000): 120, 135, 128, 150, 165, 180.
- Growth from month 1 to 6: (180−120)/120 × 100 = **50% increase** → clear **upward trend** (month 3 dips but the overall direction is up).
- 3-month moving average of last 3 values: (150+165+180)/3 = **165**.

## 2.4 Likely CAE-1 Questions (with model answers)

1. **What is data preparation? List its main steps.** → Cleaning, transforming, and structuring raw data for analysis; steps: import/collect, clean (duplicates, missing values), transform (formats, derived columns), validate (ranges, consistency).
2. **Name five sources from which data can be imported, and how.** → CSV (Data→From Text/CSV), Excel workbook (From File), spreadsheets (Import/IMPORTRANGE), website tables (From Web with URL), database tables (SQL/ODBC connector).
3. **Why should duplicate data be removed? How?** → Duplicates inflate counts and distort statistics (mean, totals); remove via Data → Remove Duplicates in Excel.
4. **Explain the Excel functions LEFT, RIGHT, LEN, MID, FIND with one example each.** → Table from 2.2: e.g. LEFT("Hello",3)="Hel"; RIGHT("Hello",2)="lo"; LEN("Data")=4; MID("Hello",2,3)="ell"; FIND("l","Hello")=3.
5. **Write a formula to extract the domain from "user@example.com" in cell A1.** → `=MID(A1, FIND("@",A1)+1, LEN(A1))` → "example.com".
6. **What is a trend? Name three ways to identify trends in data.** → Long-term directional movement (up/down/flat); identified via time-series line charts, moving averages, and fitted trendlines (regression slope).
7. **Distinguish between trend and seasonality.** → Trend = long-term directional change over the whole period; seasonality = regular repeating cycles of fixed period (e.g. higher sales every December).

## 2.5 Unit 2 Quick Revision
- Data prep steps: import → clean → transform → validate.
- Sources: CSV, Excel, spreadsheets, web tables, database tables.
- Duplicates inflate counts — remove them.
- LEFT(text,n) / RIGHT(text,n) / LEN(text) / MID(text,start,n) / FIND(find,text).
- Trend = long-term direction; tools: line chart, moving average, trendline; growth % = (new−old)/old × 100.

---

# Unit 3: Inferential Statistics & Regression

## 3.1 Topics
- Distributions; normal distribution; standard normal distribution
- Central Limit Theorem; standard error
- Estimators and estimates; confidence interval
- Student's t-distribution; margin of error
- Linear regression: simple & multiple linear regression
- Correlation vs regression
- SST, SSR, SSE; R-square, adjusted R-square; significance of p-value

## 3.2 Explanations & Key Definitions

### Distributions
A **probability distribution** describes how values of a random variable are spread — which values are likely. Examples: uniform, binomial, normal.

### Normal distribution
The bell-shaped, symmetric distribution. Completely described by mean μ and std dev σ. Properties:
- Symmetric about μ; mean = median = mode.
- **Empirical (68-95-99.7) rule**: ≈68% of data within μ ± σ; ≈95% within μ ± 2σ; ≈99.7% within μ ± 3σ.
- PDF: $$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

### Standard normal distribution
Normal distribution with **μ = 0, σ = 1**. Any normal X converts via the **z-score**:
$$z = \frac{x - \mu}{\sigma}$$
Areas under the standard normal curve give probabilities (z-table).

### Central Limit Theorem (CLT)
If samples of size n are drawn from **any** population with mean μ and std dev σ, then the **sampling distribution of the sample mean** is approximately normal with mean μ and std dev σ/√n, for large n (rule of thumb: n ≥ 30). This is why we can use normal-based inference even when the population isn't normal.

### Standard error (of the mean)
$$SE = \frac{\sigma}{\sqrt{n}}$$ (use sample s if σ unknown). Measures how much the sample mean is expected to vary from sample to sample. Larger n → smaller SE.

### Estimators and estimates
- **Estimator**: a rule/formula for guessing a population parameter (e.g. sample mean x̄ is an estimator of μ).
- **Estimate**: the actual number produced by the estimator on your sample (e.g. x̄ = 52.3).
- **Unbiased estimator**: its expected value equals the true parameter.

### Confidence interval (CI)
A range of values that likely contains the true population parameter, with a stated confidence level.
$$\text{CI} = \bar{x} \pm \underbrace{z_{\alpha/2}\times SE}_{\text{margin of error}}$$
where SE = σ/√n (use **t** critical value instead of z when n < 30 and σ unknown). Interpretation: "We are 95% confident the true mean lies between L and U." It is **not** the probability that the mean is inside one specific computed interval.

Common critical values: 90% → z = 1.645; 95% → z = 1.96; 99% → z = 2.576.

### Student's t-distribution
Used instead of the normal when the sample is **small (n < 30)** and population σ is **unknown** (estimate σ with sample s). Heavier tails than normal; approaches the normal as n grows. Degrees of freedom **df = n − 1**. CI with t: x̄ ± t_{α/2, n−1} × (s/√n).

### Margin of error (ME)
Half the width of the CI: $$ME = z_{\alpha/2}\times SE = z_{\alpha/2}\times\frac{\sigma}{\sqrt{n}}$$
Ways to reduce ME: larger sample n, smaller σ, or lower confidence level.

### Simple vs multiple linear regression
- **Simple linear regression**: one predictor. $$\hat{y} = b_0 + b_1 x$$
- **Multiple linear regression**: two or more predictors. $$\hat{y} = b_0 + b_1 x_1 + b_2 x_2 + \cdots + b_k x_k$$
- **Least squares** chooses coefficients to minimise Σ(yᵢ − ŷᵢ)².
- Simple regression slope: $$b_1 = r\frac{s_y}{s_x},\qquad b_0 = \bar{y} - b_1\bar{x}$$

### Correlation vs regression
| Correlation | Regression |
|---|---|
| Measures **strength & direction** of linear relationship | Models relationship to **predict** Y from X |
| Single number r (−1 to +1), symmetric (r_xy = r_yx) | Equation ŷ = b₀ + b₁x, direction matters (X predicts Y) |
| No causation implied | Used for prediction; causation still not proven |
| E.g. r = 0.85 → strong positive link | E.g. ŷ = 2 + 3x → each unit of x adds 3 to predicted y |

### SST, SSR, SSE
- **SST (Total Sum of Squares)** = Σ(yᵢ − ȳ)² — total variation in Y.
- **SSR (Regression Sum of Squares)** = Σ(ŷᵢ − ȳ)² — variation **explained** by the model.
- **SSE (Error Sum of Squares)** = Σ(yᵢ − ŷᵢ)² — variation **unexplained** (residuals).
- **SST = SSR + SSE** ← always true.

### R-square and adjusted R-square
$$R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}$$
- Fraction of Y's variation explained by the model (0 to 1; e.g. R² = 0.81 → 81% explained).
- **Adjusted R²** penalises adding useless predictors: $$R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-k-1}$$ where k = number of predictors. Use it to compare models with different numbers of variables; unlike R² it can decrease when a variable is added.

### Significance of p-value
- The **p-value** = probability of seeing results this extreme **if the null hypothesis were true**.
- Decision rule: if p < α (usually α = 0.05), **reject H₀** — the result is statistically significant.
- In regression output, a predictor's p-value < 0.05 means it significantly contributes to the model.
- p-value is **not** the probability that H₀ is true — it assumes H₀ is true.

## 3.3 Worked Examples

**Ex 1 — z-score & empirical rule.** Exam scores: μ = 60, σ = 10.
- z for x = 75: z = (75−60)/10 = **1.5**.
- Within μ ± 2σ (40 to 80): ≈ **95%** of students score between 40 and 80.

**Ex 2 — 95% confidence interval.** n = 36, x̄ = 50, σ = 12.
- SE = 12/√36 = 12/6 = 2
- ME = 1.96 × 2 = 3.92
- CI = 50 ± 3.92 = **(46.08, 53.92)** → "We are 95% confident the true mean lies between 46.08 and 53.92."

**Ex 3 — Regression quantities.** Given SSR = 180, SSE = 20, n = 30, k = 2 predictors.
- SST = SSR + SSE = 180 + 20 = **200**
- R² = SSR/SST = 180/200 = **0.90** → 90% of variation explained
- Adjusted R² = 1 − (1−0.9)(30−1)/(30−2−1) = 1 − (0.1×29/27) = 1 − 0.1074 = **0.893**

## 3.4 Likely CAE-1 Questions (with model answers)

1. **State and explain the Central Limit Theorem.** → For samples of size n from any population (mean μ, std dev σ), the sampling distribution of x̄ is approximately normal with mean μ and std dev σ/√n when n is large (n ≥ 30). It justifies normal-based inference on non-normal populations.
2. **What is a z-score? Convert x = 75 to a z-score given μ = 60, σ = 10.** → z = (x−μ)/σ = number of std devs above/below the mean; z = (75−60)/10 = 1.5.
3. **Define standard error and margin of error. How can ME be reduced?** → SE = σ/√n (sample-to-sample variation of x̄); ME = z×SE (half the CI width). Reduce ME by increasing n, reducing σ, or lowering the confidence level.
4. **Explain a 95% confidence interval and write its formula.** → CI = x̄ ± z(α/2)·σ/√n; "we are 95% confident the true population mean lies in the interval" — it does not mean 95% probability for a specific computed interval.
5. **When do we use Student's t-distribution instead of the normal?** → Small samples (n < 30) with unknown population σ (using sample s); df = n − 1; heavier tails than normal, approaches normal as n grows.
6. **Differentiate between correlation and regression.** → Correlation (r, −1 to +1) measures strength/direction of linear relationship, symmetric; regression (ŷ = b₀ + b₁x) models and predicts Y from X. Neither proves causation.
7. **Define SST, SSR, SSE and state their relationship. Calculate R² given SSR = 180, SSE = 20.** → SST = total variation = SSR + SSE = 200; R² = SSR/SST = 0.90 → 90% of Y's variation explained by the model.
8. **What is adjusted R² and why is it better than R² for comparing models?** → R²_adj = 1 − (1−R²)(n−1)/(n−k−1); it penalises extra predictors, so it can fall when a useless variable is added, making it fair for comparing models with different numbers of predictors.
9. **Explain the significance of the p-value with the 0.05 rule.** → p = probability of such extreme results if H₀ were true; if p < 0.05, reject H₀ (statistically significant). In regression, a predictor with p < 0.05 significantly contributes to the model.

## 3.5 Unit 3 Quick Revision
- z = (x−μ)/σ; 68-95-99.7 rule for ±1, ±2, ±3σ.
- CLT: x̄ ~ N(μ, σ/√n) for n ≥ 30, whatever the population shape.
- SE = σ/√n; CI = x̄ ± z×SE; ME = z×SE; 95% → z = 1.96.
- Small n, σ unknown → t-distribution, df = n−1.
- ŷ = b₀ + b₁x; b₁ = r·s_y/s_x; b₀ = ȳ − b₁x̄.
- SST = SSR + SSE; R² = SSR/SST = 1 − SSE/SST; R²_adj = 1 − (1−R²)(n−1)/(n−k−1).
- p < 0.05 → reject H₀ (significant).

---

# Master Quick-Revision Checklist (All 3 Units)

**Definitions to memorise**
- [ ] Analysis (what happened) vs Analytics (predict + prescribe)
- [ ] 4 analytics types: D-D-P-P with one example each
- [ ] Quantitative (discrete/continuous) vs qualitative (nominal/ordinal)
- [ ] Mean, median, mode + when median beats mean
- [ ] Range, quartiles, IQR = Q3 − Q1
- [ ] Data preparation steps: import → clean → transform → validate
- [ ] CSV = comma-separated plain text
- [ ] LEFT/RIGHT/LEN/MID/FIND signatures
- [ ] Trend vs seasonality
- [ ] CLT, standard error, estimator vs estimate
- [ ] Confidence interval interpretation
- [ ] Correlation vs regression
- [ ] SST = SSR + SSE
- [ ] p < 0.05 → significant

**Formulas to memorise**
- [ ] x̄ = Σx/n
- [ ] Mean − Mode ≈ 3(Mean − Median)
- [ ] s² = Σ(x−x̄)²/(n−1); s = √s²
- [ ] z = (x−μ)/σ
- [ ] SE = σ/√n
- [ ] CI = x̄ ± z(α/2)·SE; ME = z(α/2)·SE
- [ ] 90% → 1.645; 95% → 1.96; 99% → 2.576
- [ ] t: df = n−1, used when n < 30 and σ unknown
- [ ] ŷ = b₀ + b₁x; b₁ = r·s_y/s_x; b₀ = ȳ − b₁x̄
- [ ] R² = SSR/SST = 1 − SSE/SST
- [ ] R²_adj = 1 − (1−R²)(n−1)/(n−k−1)
- [ ] Growth % = (new−old)/old × 100
