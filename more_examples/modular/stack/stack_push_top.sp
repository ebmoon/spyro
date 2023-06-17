//@Description Sketch to reverse a list.

var {
    stack s;
    int v;
    stack push_out;

    boolean top_err;
    int top_out;
}

relation {
    push(s, v, push_out);
    top(push_out, top_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty(s) | !is_empty(s);
    boolean RHS -> top_out == I;
    int I -> v | top(ST);
    stack ST -> s | empty();
}

example {
    int -> ??(3) | -1 * ??(3) ;
    boolean -> true | false;
    stack -> empty() | push(stack, int);
}