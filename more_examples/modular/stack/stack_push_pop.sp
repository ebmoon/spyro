//@Description Sketch to reverse a list.

var {
    stack s;
    int v;
    stack push_out;

    boolean pop_err;
    stack pop_out;
}

relation {
    push(s, v, push_out);
    pop(push_out, pop_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty(s) | !is_empty(s);
    boolean RHS -> stack_equal(pop_out, ST);
    int I -> v;
    stack ST -> s | pop(s) | empty() | push(ST, I);
}

example {
    int -> ??(3) | -1 * ??(3) ;
    boolean -> true | false;
    stack -> empty() | push(stack, int);
}