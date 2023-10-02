type server = P1 | P2

type player = {sets : int; games : int; points : int}

type tennis_match = {p1 : player; p2: player; server: server; set_scores: string list}

let () = Random.self_init ()

let initial_state = {
  p1 = {
    sets = 0;
    games = 0;
    points = 0
  };
  p2 = {
    sets = 0;
    games = 0;
    points = 0
  };
  server = P1;
  set_scores = []
}

let next state = match state.server with 
| P1 -> { state with server = P2}
| P2 -> { state with server = P1}
