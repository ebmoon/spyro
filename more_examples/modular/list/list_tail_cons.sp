//@Description 

var {
    int v;
    list l;
    list cons_out;

    list tail_out;
}

relation {
    cons(v, l, cons_out);
    tail(cons_out, tail_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty(l) | !is_empty(l);
    boolean RHS -> equal_list(tail_out, L);
    list L -> l | nil() | tail(l) | cons(v, L) ;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
    boolean -> true | false;
}