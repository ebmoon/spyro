//@Description 

var {
    list l;
    int x;
    list cons_out;
    boolean is_empty_out;
    boolean err;
}

relation {
    cons(x, l, cons_out);
    is_empty(cons_out, is_empty_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty(l) | !is_empty(l);
    boolean RHS -> is_empty_out == BB ;
    boolean BB -> true | false | is_empty(L) | !is_empty(L);
    list L -> l;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
    boolean -> true | false;
}