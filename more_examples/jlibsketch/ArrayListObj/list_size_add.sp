//@Description 

var {
    ArrayList a;
    E e;
    ArrayList add_out;

    int size_out;
}

relation {
    add(a, e, add_out);
    size(add_out, size_out);
}

generator {
    boolean AP -> !GUARD || !GUARD || RHS;
    boolean GUARD -> true | compare(S, S);
    boolean RHS -> size_out == S;
    int S -> size(L) + C | C;
    int C -> ??(2) - 1;
    ArrayList L -> newArrayList() | a;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    E -> ??;
    ArrayList -> newArrayList() | add(ArrayList, E);
    boolean -> true | false;
}