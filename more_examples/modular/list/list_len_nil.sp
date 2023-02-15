//@Description 

var {
    list nil_out;
    int len_out;
}

relation {
    nil(nil_out);
    len(nil_out, len_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true;
    boolean RHS -> len_out == ??;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
    boolean -> true | false;
}