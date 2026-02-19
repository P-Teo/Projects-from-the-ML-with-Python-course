# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        opponent_history.clear()
        play_order.clear()

    opponent_history.append(prev_play)
    prediction = "P"

    if len(opponent_history) > 3:
        last_three = "".join(opponent_history[-3:])

        potential_next_sequence = "".join(opponent_history[-4:])
        if potential_next_sequence in play_order:
            play_order[potential_next_sequence] += 1
        else:
            play_order[potential_next_sequence] = 1

        last_three = "".join(opponent_history[-3:])
        potential_plays = [
            last_three + "R",
            last_three + "P",
            last_three + "S",
        ]

        prediction = max(potential_plays, key=lambda key: play_order.get(key, 0))[-1]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    if prediction == '':
        return "R"

    return ideal_response[prediction]