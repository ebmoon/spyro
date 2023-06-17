//@Description 

var {
    ArrayList new_out;

    int size_out;
}

relation {
    newArrayList(new_out);
    size(new_out, size_out);
}

generator {
    boolean AP -> RHS;
    boolean RHS -> size_out == S;
    int S -> -1 | 0 | 1;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    E -> ??;
    ArrayList -> newArrayList() | add(ArrayList, E);
    boolean -> true | false;
}