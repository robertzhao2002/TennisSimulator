import unittest
from main import next


class TennisSimulatorTests(unittest.TestCase):
    initial_state = {
        "p1": {"sets": 0, "games": 0, "points": 0},
        "p2": {"sets": 0, "games": 0, "points": 0},
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": False,
    }

    game_point = {
        "p1": {"sets": 0, "games": 0, "points": 3},
        "p2": {"sets": 0, "games": 0, "points": 1},
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": False,
    }

    deuce_state = {
        "p1": {"sets": 0, "games": 0, "points": 3},
        "p2": {"sets": 0, "games": 0, "points": 3},
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": False,
    }

    adv_state = {
        "p1": {"sets": 0, "games": 0, "points": 3},
        "p2": {"sets": 0, "games": 0, "points": 4},
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": False,
    }

    almost_tiebreak = {
        "p1": {"sets": 0, "games": 6, "points": 3},
        "p2": {"sets": 0, "games": 5, "points": 4},
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": False,
    }

    set_point_normal = {
        "p1": {"sets": 0, "games": 6, "points": 3},
        "p2": {"sets": 0, "games": 5, "points": 0},
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": False,
    }

    set_point_tiebreaker = {
        "p1": {"sets": 0, "games": 6, "points": 5},
        "p2": {"sets": 0, "games": 6, "points": 6},
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": True,
    }

    extra_points_tiebreaker = {
        "p1": {"sets": 0, "games": 6, "points": 6},
        "p2": {"sets": 0, "games": 6, "points": 6},
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": True,
    }

    continue_tiebreaker = {
        "p1": {"sets": 0, "games": 6, "points": 6},
        "p2": {"sets": 0, "games": 6, "points": 7},
        "set_scores": [],
        "p1_serving": False,
        "tiebreak": True,
    }

    p1_lead_tiebreaker = {
        "p1": {"sets": 0, "games": 6, "points": 7},
        "p2": {"sets": 0, "games": 6, "points": 7},
        "set_scores": [],
        "p1_serving": False,
        "tiebreak": True,
    }

    p1_win_tiebreaker = {
        "p1": {"sets": 0, "games": 6, "points": 8},
        "p2": {"sets": 0, "games": 6, "points": 7},
        "set_scores": [],
        "p1_serving": True,
        "tiebreak": True,
    }

    def test_basic(self):
        result = next(self.initial_state, "p1")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 0, "points": 1},
                "p2": {"sets": 0, "games": 0, "points": 0},
                "set_scores": [],
                "p1_serving": True,
                "tiebreak": False,
            },
        )

    def test_game_point(self):
        result = next(self.game_point, "p1")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 1, "points": 0},
                "p2": {"sets": 0, "games": 0, "points": 0},
                "set_scores": [],
                "p1_serving": False,
                "tiebreak": False,
            },
        )

    def test_deuce(self):
        result = next(self.deuce_state, "p1")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 0, "points": 4},
                "p2": {"sets": 0, "games": 0, "points": 3},
                "set_scores": [],
                "p1_serving": True,
                "tiebreak": False,
            },
        )
        result = next(self.deuce_state, "p2")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 0, "points": 3},
                "p2": {"sets": 0, "games": 0, "points": 4},
                "set_scores": [],
                "p1_serving": True,
                "tiebreak": False,
            },
        )

    def test_ad(self):
        result = next(self.adv_state, "p1")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 0, "points": 3},
                "p2": {"sets": 0, "games": 0, "points": 3},
                "set_scores": [],
                "p1_serving": True,
                "tiebreak": False,
            },
        )

    def test_ad_game(self):
        result = next(self.adv_state, "p2")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 0, "points": 0},
                "p2": {"sets": 0, "games": 1, "points": 0},
                "set_scores": [],
                "p1_serving": False,
                "tiebreak": False,
            },
        )

    def test_almost_tiebreak(self):
        result = next(self.almost_tiebreak, "p2")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 6, "points": 0},
                "p2": {"sets": 0, "games": 6, "points": 0},
                "set_scores": [],
                "p1_serving": False,
                "tiebreak": True,
            },
        )

    def test_set_point(self):
        result = next(self.set_point_normal, "p1")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 1, "games": 0, "points": 0},
                "p2": {"sets": 0, "games": 0, "points": 0},
                "set_scores": ["7-5"],
                "p1_serving": False,
                "tiebreak": False,
            },
        )

    def test_set_point_tiebreaker(self):
        result = next(self.set_point_tiebreaker, "p2")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 0, "points": 0},
                "p2": {"sets": 1, "games": 0, "points": 0},
                "set_scores": ["6(5)-7"],
                "p1_serving": False,
                "tiebreak": False,
            },
        )

    def test_extra_points_tiebreaker(self):
        result = next(self.extra_points_tiebreaker, "p2")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 6, "points": 6},
                "p2": {"sets": 0, "games": 6, "points": 7},
                "set_scores": [],
                "p1_serving": False,
                "tiebreak": True,
            },
        )

    def test_continue_tiebreaker(self):
        result = next(self.continue_tiebreaker, "p1")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 6, "points": 7},
                "p2": {"sets": 0, "games": 6, "points": 7},
                "set_scores": [],
                "p1_serving": False,
                "tiebreak": True,
            },
        )

    def test_p1_lead_tiebreaker(self):
        result = next(self.p1_lead_tiebreaker, "p1")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 0, "games": 6, "points": 8},
                "p2": {"sets": 0, "games": 6, "points": 7},
                "set_scores": [],
                "p1_serving": True,
                "tiebreak": True,
            },
        )

    def test_p1_win_tiebreaker(self):
        result = next(self.p1_win_tiebreaker, "p1")
        self.assertEqual(
            result,
            {
                "p1": {"sets": 1, "games": 0, "points": 0},
                "p2": {"sets": 0, "games": 0, "points": 0},
                "set_scores": ["7-6(7)"],
                "p1_serving": False,
                "tiebreak": False,
            },
        )


if __name__ == "__main__":
    unittest.main()
