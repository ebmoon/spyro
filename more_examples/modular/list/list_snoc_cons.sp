//@Description 

var {
    int v1;
    list l;
    list cons_out;

    int v2;
    list snoc_out;

    boolean err;
}

relation {
    cons(v1, l, cons_out);
    snoc(cons_out, v2, snoc_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty(l) | !is_empty(l);
    boolean RHS -> equal_list(snoc_out, L);
    int I -> v1 | v2;
    list L -> l | nil() | snoc(l, I) | cons(I, L);
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
    boolean -> true | false;
}