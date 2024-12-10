# Hidden Markov Model (HMM) - Solving with Viterbi's Algorithm

This repository demonstrates using Viterbi's algorithm to solve a Hidden Markov Model (HMM) involving weather conditions.

## Project Overview

### Purpose
This project implements the Viterbi algorithm to solve a Hidden Markov Model (HMM) that predicts weather states based on observable conditions. The goal is to demonstrate how probabilistic modeling can be used to infer hidden states from a sequence of observations.

### Modeling Approach
The HMM is constructed with three weather states:
- Sunny
- Rainy
- Cloudy

And three observable conditions:
- Umbrella
- No Umbrella
- Windy

### Key Assumptions
1. Weather states transition with predefined probabilities (e.g., a sunny day is more likely to remain sunny).
2. Each weather state has a specific probability of generating certain observations.
3. The initial state probabilities are known and fixed.

### Probabilistic Model Components
- **Start Probabilities**: Define the likelihood of starting in each weather state
- **Transition Probabilities**: Represent how likely one weather state is to change to another
- **Emission Probabilities**: Describe the likelihood of observing specific conditions in each weather state

### Viterbi Algorithm
The Viterbi algorithm is used to:
- Compute the most probable sequence of hidden states
- Handle the complexity of probabilistic state transitions
- Efficiently track the most likely path through the model

### Results
Given an observation sequence, the algorithm returns the most probable underlying weather state sequence, demonstrating how hidden states can be inferred from observable data.

### Mathematical Foundation
Based on dynamic programming and probability theory, specifically:
- Markov chain principles
- Maximum likelihood estimation
- Probabilistic state inference

## Requirements

### Python

Ensure Python is installed on your system.

#### macOS:

```
brew install python
```

### File: `HMM.py`

This script includes the following:

- **Environment Setup**:
  - Defines state probabilities and observation probabilities.
- **Viterbi Algorithm**:
  - Implements the algorithm to calculate the most likely sequence of states based on given observations.
- **Output**:

  - Returns the most probable sequence of observations. Provided example:

    ```
    ["Umbrella", "Windy", "No Umbrella", "Umbrella", "No Umbrella", "Windy", "Windy", "Windy", "Umbrella", "Windy", "No Umbrella", "No Umbrella"]

    Output should be:

    Most likely path: ['Rainy', 'Cloudy', 'Sunny', 'Rainy', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Rainy', 'Cloudy', 'Sunny', 'Sunny']
    ```

## Usage
Run the `HMM.py` script to see the Viterbi algorithm in action with a predefined observation sequence.
