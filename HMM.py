states = ["Sunny", "Rainy", "Cloudy"]
observations = ["Umbrella", "No Umbrella", "Windy"]
start_prob = {"Sunny": 0.5, "Rainy": 0.3, "Cloudy": 0.2}
transition_prob = {
    "Sunny": {"Sunny": 0.6, "Rainy": 0.3, "Cloudy": 0.1},
    "Rainy": {"Sunny": 0.2, "Rainy": 0.5, "Cloudy": 0.3},
    "Cloudy": {"Sunny": 0.3, "Rainy": 0.4, "Cloudy": 0.3},
}
emission_prob = {
    "Sunny": {"Umbrella": 0.1, "No Umbrella": 0.7, "Windy": 0.2},
    "Rainy": {"Umbrella": 0.8, "No Umbrella": 0.1, "Windy": 0.1},
    "Cloudy": {"Umbrella": 0.3, "No Umbrella": 0.4, "Windy": 0.3},
}

# Viterbi Algorithm
def viterbi(obs, states, start_p, trans_p, emiss_p):
    V = [{}]
    path = {}

    # Initialize
    for state in states:
        V[0][state] = start_p[state] * emiss_p[state][obs[0]]
        path[state] = [state]

    # For t > 0
    for t in range(1, len(obs)):
        V.append({})
        new_path = {}

        for curr_state in states:
            max_prob, prev_state = max(
                (V[t-1][prev_state] * trans_p[prev_state][curr_state] * emiss_p[curr_state][obs[t]], prev_state)
                for prev_state in states
            )
            V[t][curr_state] = max_prob
            new_path[curr_state] = path[prev_state] + [curr_state]

        path = new_path


    # Most probable sequence
    max_prob, final_state = max((V[-1][state], state) for state in states)
    return path[final_state]




observation_sequence = ["Umbrella", "Windy", "No Umbrella", "Umbrella", "No Umbrella", "Windy", "Windy", "Windy", "Umbrella", "Windy", "No Umbrella", "No Umbrella"]

most_probable_path = viterbi(observation_sequence, states, start_prob, transition_prob, emission_prob)





print("Most likely path: " + str(most_probable_path))
