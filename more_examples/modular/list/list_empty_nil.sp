//@Description 

var {
    list nil_out;
    boolean is_empty_out;
}

relation {
    nil(nil_out);
    is_empty(nil_out, is_empty_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true;
    boolean RHS -> is_empty_out == true | is_empty_out == false ;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
    boolean -> true | false;
}