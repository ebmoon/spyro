//@Description 

var {
    list nil_out;
    list tail_out;
}

relation {
    nil(nil_out);
    tail(nil_out, tail_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true;
    boolean RHS -> equal_list(tail_out, L);
    list L -> nil();
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
    boolean -> true | false;
}