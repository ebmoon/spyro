//@Description Queue module, should run with size 1

var {
    queue q;
    int v;
    queue enq_out;

    int front_out;
}

relation {
    enqueue(q, v, enq_out);
    front(enq_out, front_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty_queue(q) | !is_empty_queue(q);
    boolean RHS -> front_out == I ;
    int I -> v | front(Q);
    queue Q -> q | empty_queue();
}

example {
    int -> ??(3) | -1 * ??(3) ;
    boolean -> true | false;
    queue(3) -> empty_queue() | enqueue(queue, int) | dequeue(queue) ;
}