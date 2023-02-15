//@Description 

var {
    list nil_out;

    int v;
    list snoc_out;
}

relation {
    nil(nil_out);
    snoc(nil_out, v, snoc_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true;
    boolean RHS -> equal_list(snoc_out, L);
    list L -> nil();
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
    boolean -> true | false;
}