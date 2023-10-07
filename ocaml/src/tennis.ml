type server =
  | P1
  | P2

type player = {
  sets : int;
  games : int;
  points : int;
}

type match_state = {
  p1 : player;
  p2 : player;
  server : server;
  set_scores : string list;
}

let () = Random.self_init ()

let initial_state =
  {
    p1 = { sets = 0; games = 0; points = 0 };
    p2 = { sets = 0; games = 0; points = 0 };
    server = P1;
    set_scores = [];
  }

let next state = function
  | P1 -> begin
      let unchecked_state =
        { state with p1 = { state.p1 with points = state.p1.points + 1 } }
      in
      match state.server with
      | P1 -> unchecked_state
      | P2 -> { state with server = P1 }
    end
  | P2 -> begin
      let unchecked_state =
        { state with p2 = { state.p2 with points = state.p2.points + 1 } }
      in
      match state.server with
      | P1 -> { state with server = P2 }
      | P2 -> unchecked_state
    end
