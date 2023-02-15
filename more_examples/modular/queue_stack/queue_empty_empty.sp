//@Description Queue module, should run with size 1

var {
    queue empty_out;

    boolean is_empty_out;
}

relation {
    empty_queue(empty_out);
    is_empty_queue(empty_out, is_empty_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true;
    boolean RHS -> is_empty_out == BB ;
    boolean BB -> true | false;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    boolean -> true | false;
    queue(3) -> empty_queue() | enqueue(queue, int) | dequeue(queue) ;
}