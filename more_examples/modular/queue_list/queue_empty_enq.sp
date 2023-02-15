//@Description Queue module, should run with size 1

var {
    queue q;
    int v;
    queue enq_out;

    boolean is_empty_out;
}

relation {
    enqueue(q, v, enq_out);
    is_empty_queue(enq_out, is_empty_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty_queue(q) | !is_empty_queue(q);
    boolean RHS -> is_empty_out == BB ;
    boolean BB -> true | false | is_empty_queue(Q) | !is_empty_queue(Q);
    queue Q -> q | empty_queue();
}

example {
    int -> ??(3) | -1 * ??(3) ;
    boolean -> true | false;
    queue(3) -> empty_queue() | enqueue(queue, int) | dequeue(queue) ;
}