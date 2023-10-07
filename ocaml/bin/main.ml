let state_as_string (s : Tennis.match_state) =
  match s.server with
  | Tennis.P1 -> "P1"
  | _ -> raise Not_found

let () = print_endline (state_as_string Tennis.initial_state)
