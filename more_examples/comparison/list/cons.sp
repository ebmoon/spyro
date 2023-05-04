var {
    list l;
    int v;
    list lout;

    int x;
    int y;
}

relation {
    cons(v, l, lout);
}

generator {
    boolean AP -> is_empty(L) | !is_empty(L) 
                | equal_list(L, L) | !equal_list(L, L)
                | mem(L, I) | !mem(L, I)
                | ord(L, I, I) | !ord(L, I, I)
                | I == I | I != I;
    int I -> v | x | y ;
    list L -> l | lout;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
}