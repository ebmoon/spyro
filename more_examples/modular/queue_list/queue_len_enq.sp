//@Description Queue module, should run with size 1

var {
    queue q;
    int v;
    queue enq_out;

    int len_out;
}

relation {
    enqueue(q, v, enq_out);
    len_queue(enq_out, len_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty_queue(q) | !is_empty_queue(q);
    boolean RHS -> len_out == S;
    int S -> ?? | len_queue(Q) + ?? | len_queue(Q) - ??;
    queue Q -> q | empty_queue() | enqueue(Q, v);
}

example {
    int -> ??(3) | -1 * ??(3) ;
    boolean -> true | false;
    queue(3) -> empty_queue() | enqueue(queue, int) | dequeue(queue) ;
}