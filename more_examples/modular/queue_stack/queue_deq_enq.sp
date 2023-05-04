//@Description Queue module, should run with size 1

var {
    queue q;
    int v;
    queue enq_out;

    queue deq_out;
}

relation {
    enqueue(q, v, enq_out);
    dequeue(enq_out, deq_out);
}

generator {
    boolean AP -> !GUARD || EQ;
    boolean GUARD -> true | is_empty_queue(q) | !is_empty_queue(q);
    boolean EQ -> equal_queue(deq_out, Q);
    queue Q -> empty_queue() | q | dequeue(q) | enqueue(Q, v);
}

example {
    int -> ??(3) | -1 * ??(3) ;
    boolean -> true | false;
    queue(3) -> empty_queue() | enqueue(queue, int) | dequeue(queue) ;
}