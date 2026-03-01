// Language: F#
module thing

let l = int64(System.Console.ReadLine())
let n = int(System.Console.ReadLine())

let rec readlines n out = 
    match n with
    | 0 -> out
    | n -> readlines (n-1) (int64(System.Console.ReadLine()) :: out)

let rec findDrinkCount l ds m acc =
    match ds with 
    | [] -> acc
    | d::ds when d+m > l -> acc
    | d::ds -> findDrinkCount l ds (m+d) (acc+1)

let lines = (readlines n []) |> List.sort 
printfn "%d" (findDrinkCount l lines 0L 0)
