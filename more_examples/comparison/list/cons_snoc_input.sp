var {
    list l;
    int v;
    
    list cons_out;
    list snoc_out;
}

relation {
    cons(v, l, cons_out);
    snoc(l, v, snoc_out);
}

generator {
    boolean P -> AP || AP || !equal_list(cons_out, snoc_out);
    boolean AP -> is_empty(L) | !is_empty(L) 
                | equal_list(L, L) | !equal_list(L, L)
                | mem(L, v) | !mem(L, v)
                | compare(S, S + ??(1))
                | true | false;
    int I -> v ;
    int S -> len(L) | 0 ;
    list L -> l;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
}