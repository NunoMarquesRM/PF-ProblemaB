type tree =
| Leaf of int
| Node of tree * tree * tree * tree




let rec print x =
  match x with
  | Leaf x -> print_int x
  | Node ( x1, x2, x3, x4 ) ->
    print x1;
    print x2;
    print x3;
    print x4




let rec build x =
  if x == 1 then ( Leaf ( -1 ) )
  else ( Node ( build (x / 4), build (x / 4), build (x / 4), build (x / 4) ) )

let rec height x =
  match x with
  | Leaf _ -> 1
  | Node ( x, _, _, _ ) -> 1 + height x

let rec nodes x =
  match x with
  | Leaf _ -> 1
  | Node ( x1, x2, x3, x4 ) ->
    nodes x1 + nodes x2 + nodes x3 + nodes x4




let rec pop tr x y xmin xmax ymin ymax v =
    match tr with
    | Leaf _ -> Leaf v
    | Node ( x1, x2, x3, x4 ) ->
      if x >= (xmin + xmax) / 2 then
        if y < (ymin + ymax) / 2
        then
          Node (
            pop x1 x y (xmin +(xmax+1-xmin)/2) xmax ymin (ymax-(ymax+1-ymin)/2) v,
            x2,
            x3,
            x4
          )
        else
          Node (
            x1,
            x2,
            x3,
            pop x4 x y (xmin+(xmax+1-xmin)/2) xmax (ymin+(ymax+1-ymin)/2) ymax v
          )
      else
        if y < (ymin + ymax) / 2
        then
          Node(
            x1,
            pop x2 x y xmin (xmax-(xmax+1-xmin)/2) ymin (ymax-(ymax+1-ymin)/2) v,
            x3,
            x4
          )
        else
          Node(
            x1,
            x2,
            pop x3 x y xmin (xmax-(xmax+1-xmin)/2) (ymin+(ymax+1-ymin)/2) ymax v,
            x4
          )

let rec populate tr x y l =
  if y == l then tr else
  if x >= l then populate tr 0 ( y + 1 ) l else
    let i = Scanf.scanf " %d" (fun x -> x ) in
    print_int i; print_string " "; print_int x; print_string " "; print_int y; print_endline " ";
    populate ( pop tr x y 0 l 0 l i ) ( x + 1 ) y l




let rec printt tr x y xmin xmax ymin ymax =
    match tr with
    | Leaf x -> print_int x
    | Node ( x1, x2, x3, x4 ) ->
      if x >= (xmin + xmax) / 2 then
        if y < (ymin + ymax) / 2
        then
          printt x1 x y (xmin +(xmax+1-xmin)/2) xmax ymin (ymax-(ymax+1-ymin)/2)
        else
          printt x4 x y (xmin+(xmax+1-xmin)/2) xmax (ymin+(ymax+1-ymin)/2) ymax
      else
        if y < (ymin + ymax) / 2
        then
          printt x2 x y xmin (xmax-(xmax+1-xmin)/2) ymin (ymax-(ymax+1-ymin)/2)
        else
          printt x3 x y xmin (xmax-(xmax+1-xmin)/2) (ymin+(ymax+1-ymin)/2) ymax

let rec print tr x y l =
  if y == l then print_endline "" else
  if x == l then ( print_endline ""; print tr 0 (y+1) l ) else
    ( printt tr x y 0 l 0 l; print_string " "; print tr (x+1) y l )




let _ =
    let _ = Scanf.scanf "%c" ( fun x -> x ) in
    let _ = Scanf.scanf "%d" ( fun x -> x ) in
    let l = Scanf.scanf " %d %d" ( fun x y -> x ) in

    let t = populate ( build ( l * l ) ) 0 0 l in

    let n = Scanf.scanf " %d" ( fun x -> x ) in
    print_endline "";
    print t 0 0 l;
    (match t with
    | Node ( Node ( Leaf x, _, _, _ ), _, _, _ ) -> print_int x
    | _ -> ());
    print_endline "";

    (match t with
    | Node ( _, _, Node ( _ , _, Leaf x, _ ), _ ) -> print_int x
    | _ -> ());
    print_endline "";

    
    (match t with
    | Node ( _, Node ( _ , _, Leaf x, _ ), _, _ ) -> print_int x
    | _ -> ());
    print_endline "";


    (match t with
    | Node ( _, _, _, Node ( _ , _, Leaf x, _ ) ) -> print_int x
    | _ -> ());
    print_endline ""