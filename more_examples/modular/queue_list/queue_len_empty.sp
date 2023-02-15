//@Description Queue module, should run with size 1

var {
    queue empty_out;

    int len_out;
}

relation {
    empty_queue(empty_out);
    len_queue(empty_out, len_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true;
    boolean RHS -> len_out == ??;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    boolean -> true | false;
    queue(3) -> empty_queue() | enqueue(queue, int) | dequeue(queue) ;
}