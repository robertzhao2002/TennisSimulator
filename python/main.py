import random
import copy


def win_serve_probability(p1_service):
    if p1_service:
        return 0.7
    return 0.3


def display_score(state):
    p1_points = state["p1"]["points"]
    p2_points = state["p2"]["points"]
    p1_games = state["p1"]["games"]
    p2_games = state["p2"]["games"]
    if not state["tiebreak"]:
        scores = ["0", "15", "30", "40", "Adv"]
        p1_points = scores[p1_points]
        p2_points = scores[p2_points]
    if state["p1_serving"]:
        print("*P1:", p1_points, "P2:", p2_points)
    else:
        print("P1:", p1_points, "*P2:", p2_points)
    print("Games:", str(p1_games) + "-" + str(p2_games))
    if len(state["set_scores"]) > 0:
        print("Sets:", ", ".join(state["set_scores"]))


def next(state, winner):
    current_state = copy.deepcopy(state)
    current_state[winner]["points"] += 1
    if current_state["tiebreak"]:
        if current_state["p1"]["points"] >= 6 and current_state["p2"]["points"] >= 6:
            if abs(current_state["p1"]["points"] - current_state["p2"]["points"]) == 2:
                current_state[winner]["games"] += 1
                set_score = (
                    str(current_state["p1"]["games"])
                    + "("
                    + str(current_state["p1"]["points"])
                    + ")"
                    + "-"
                    + str(current_state["p2"]["games"])
                )
                if winner == "p1":
                    set_score = (
                        str(current_state["p1"]["games"])
                        + "-"
                        + str(current_state["p2"]["games"])
                        + "("
                        + str(current_state["p2"]["points"])
                        + ")"
                    )
                current_state["set_scores"].append(set_score)
                current_state[winner]["sets"] += 1
                current_state["p1"]["games"] = 0
                current_state["p2"]["games"] = 0
                current_state["p1"]["points"] = 0
                current_state["p2"]["points"] = 0
                current_state["p1_serving"] = not current_state["p1_serving"]
                current_state["tiebreak"] = False
        elif current_state["p1"]["points"] == 7 or current_state["p2"]["points"] == 7:
            current_state[winner]["games"] += 1
            set_score = (
                str(current_state["p1"]["games"])
                + "("
                + str(current_state["p1"]["points"])
                + ")"
                + "-"
                + str(current_state["p2"]["games"])
            )
            if winner == "p1":
                set_score = (
                    str(current_state["p1"]["games"])
                    + "-"
                    + str(current_state["p2"]["games"])
                    + "("
                    + str(current_state["p2"]["points"])
                    + ")"
                )
            current_state["set_scores"].append(set_score)
            current_state[winner]["sets"] += 1
            current_state["p1"]["games"] = 0
            current_state["p2"]["games"] = 0
            current_state["p1"]["points"] = 0
            current_state["p2"]["points"] = 0
            current_state["p1_serving"] = not current_state["p1_serving"]
            current_state["tiebreak"] = False
        if (current_state["p1"]["points"] + current_state["p2"]["points"]) % 2 == 1:
            current_state["p1_serving"] = not current_state["p1_serving"]
    else:
        if current_state["p1"]["points"] >= 3 and current_state["p2"]["points"] >= 3:
            if current_state["p1"]["points"] == current_state["p2"]["points"] == 4:
                current_state["p1"]["points"] = 3
                current_state["p2"]["points"] = 3
            if current_state["p1"]["points"] == 5 or current_state["p2"]["points"] == 5:
                current_state["p1"]["points"] = 0
                current_state["p2"]["points"] = 0
                current_state[winner]["games"] += 1
                current_state["p1_serving"] = not current_state["p1_serving"]
        elif current_state["p1"]["points"] == 4 or current_state["p2"]["points"] == 4:
            current_state["p1"]["points"] = 0
            current_state["p2"]["points"] = 0
            current_state[winner]["games"] += 1
            current_state["p1_serving"] = not current_state["p1_serving"]
        if (
            abs(current_state["p1"]["games"] - current_state["p2"]["games"]) >= 2
            and current_state[winner]["games"] >= 6
        ):
            current_state[winner]["sets"] += 1
            current_state["set_scores"].append(
                str(current_state["p1"]["games"])
                + "-"
                + str(current_state["p2"]["games"])
            )
            current_state["p1"]["games"] = 0
            current_state["p2"]["games"] = 0
        if current_state["p1"]["games"] == current_state["p2"]["games"] == 6:
            current_state["tiebreak"] = True
    return current_state


def simulate():
    p1 = {"sets": 0, "games": 0, "points": 0}
    p2 = {"sets": 0, "games": 0, "points": 0}
    state = {
        "p1": p1,
        "p2": p2,
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": False,
    }
    while state["p1"]["sets"] < 3 and state["p2"]["sets"] < 3:
        display_score(state)
        input()
        point_winner = (
            "p1"
            if random.random() < win_serve_probability(state["p1_serving"])
            else "p2"
        )
        state = next(state, point_winner)


if __name__ == "__main__":
    simulate()
