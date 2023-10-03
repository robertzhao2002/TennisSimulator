import random
import copy


def initial_state():
    return {
        "p1": {"sets": 0, "games": 0, "points": 0},
        "p2": {"sets": 0, "games": 0, "points": 0},
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": False,
    }


def reset(kind, current_state):
    current_state["p1"][kind] = 0
    current_state["p2"][kind] = 0


def get_set_score(winner, current_state):
    if current_state["tiebreak"]:
        if winner == "p1":
            return (
                str(current_state["p1"]["games"])
                + "-"
                + str(current_state["p2"]["games"])
                + "("
                + str(current_state["p2"]["points"])
                + ")"
            )
        return (
            str(current_state["p1"]["games"])
            + "("
            + str(current_state["p1"]["points"])
            + ")"
            + "-"
            + str(current_state["p2"]["games"])
        )
    else:
        return (
            str(current_state["p1"]["games"]) + "-" + str(current_state["p2"]["games"])
        )


def win_serve_probability(p1_service, p_win_on_serve):
    if p1_service:
        return p_win_on_serve
    return 1 - p_win_on_serve


def display_score(state, p1_name, p2_name):
    p1_points = state["p1"]["points"]
    p2_points = state["p2"]["points"]
    p1_games = state["p1"]["games"]
    p2_games = state["p2"]["games"]
    if not state["tiebreak"]:
        scores = ["0", "15", "30", "40", "Adv"]
        p1_points = scores[p1_points]
        p2_points = scores[p2_points]
    if state["p1_serving"]:
        print("*" + p1_name + ":", p1_points, p2_name + ":", p2_points)
    else:
        print(p1_name + ":", p1_points, "*" + p2_name + ":", p2_points)
    print("Games:", str(p1_games) + "-" + str(p2_games))
    if len(state["set_scores"]) > 0:
        print("Sets:", ", ".join(state["set_scores"]))


def next(state, winner):
    current_state = copy.deepcopy(state)
    current_state[winner]["points"] += 1

    if current_state["tiebreak"]:
        if current_state[winner]["points"] >= 7:
            if abs(current_state["p1"]["points"] - current_state["p2"]["points"]) >= 2:
                current_state[winner]["games"] += 1
                current_state["set_scores"].append(get_set_score(winner, current_state))
                current_state[winner]["sets"] += 1
                reset("games", current_state)
                reset("points", current_state)
                current_state["p1_serving"] = not current_state["p1_serving"]
                current_state["tiebreak"] = False
        if (current_state["p1"]["points"] + current_state["p2"]["points"]) % 2 == 1:
            current_state["p1_serving"] = not current_state["p1_serving"]
    else:
        if current_state[winner]["points"] >= 4:
            if abs(current_state["p1"]["points"] - current_state["p2"]["points"]) >= 2:
                reset("points", current_state)
                current_state[winner]["games"] += 1
                current_state["p1_serving"] = not current_state["p1_serving"]
            elif current_state["p1"]["points"] == current_state["p2"]["points"] == 4:
                current_state["p1"]["points"] = 3
                current_state["p2"]["points"] = 3
        if (
            abs(current_state["p1"]["games"] - current_state["p2"]["games"]) >= 2
            and current_state[winner]["games"] >= 6
        ):
            current_state[winner]["sets"] += 1
            current_state["set_scores"].append(get_set_score(winner, current_state))
            reset("games", current_state)
        if current_state["p1"]["games"] == current_state["p2"]["games"] == 6:
            current_state["tiebreak"] = True
    return current_state


def simulate(p1_name, p2_name):
    state = initial_state()
    while state["p1"]["sets"] < 3 and state["p2"]["sets"] < 3:
        display_score(state, p1_name, p2_name)
        input()
        point_winner = (
            "p1"
            if random.random() < win_serve_probability(state["p1_serving"], 0.7)
            else "p2"
        )
        state = next(state, point_winner)
    match_winner = p1_name if state["p1"]["sets"] > state["p2"]["sets"] else p2_name
    print(match_winner, "wins:", ", ".join(state["set_scores"]))


if __name__ == "__main__":
    simulate("P1", "P2")
