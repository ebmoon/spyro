//@Description 

var {
    list l;
    int x;
    list cons_out;
    int len_out;
    boolean err;
}

relation {
    cons(x, l, cons_out);
    len(cons_out, len_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty(l) | !is_empty(l);
    boolean RHS -> len_out == S ;
    int S -> ?? | len(L) + ?? | len(L) - ??;
    list L -> l | nil();
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
    boolean -> true | false;
}