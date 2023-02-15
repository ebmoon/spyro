//@Description Sketch to reverse a list.

var {
    stack s;
    int v;
    stack push_out;

    int len_out;
}

relation {
    push(s, v, push_out);
    stack_len(push_out, len_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty(s) | !is_empty(s);
    boolean RHS -> len_out == S;
    int S -> ?? | stack_len(ST) + ?? | stack_len(ST) - ??;
    stack ST -> s | empty() | push(ST, v);
}

example {
    int -> ??(3) | -1 * ??(3) ;
    boolean -> true | false;
    stack -> empty() | push(stack, int);
}