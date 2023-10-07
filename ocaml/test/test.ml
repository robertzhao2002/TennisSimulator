open OUnit2

let test_next name current_state winner expected_state =
  name >:: fun _ -> Tennis.next current_state winner |> assert_equal expected_state

let tests =
  "test suite for tennis"
  >::: [
         test_next "basic"
           {
             p1 = { sets = 0; games = 0; points = 0 };
             p2 = { sets = 0; games = 0; points = 0 };
             server = P1;
             set_scores = [];
           }
           Tennis.P1
           {
             p1 = { sets = 0; games = 0; points = 1 };
             p2 = { sets = 0; games = 0; points = 0 };
             server = P1;
             set_scores = [];
           };
       ]

let _ = run_test_tt_main tests
