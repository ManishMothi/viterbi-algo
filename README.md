# Hidden Markov Model (HMM) - Solving with Viterbi's Algorithm

This repository demonstrates using Viterbi's algorithm to solve a Hidden Markov Model (HMM) involving weather conditions.

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
