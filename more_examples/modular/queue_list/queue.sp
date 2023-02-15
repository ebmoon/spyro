struct queue {
	List l;
}

void empty_queue(ref queue ret) {
    ret = new queue();
    nil(ret.l);
}

void is_empty_queue(queue q, ref boolean ret) {
    is_empty_list(q.l, ret);
}

void enqueue(queue q, int val, ref queue ret) {
    if (q == null) {
        ret = null;
    } else {
        ret = new queue();
        snoc(q.l, val, ret.l);
    }
}

void front(queue q, ref int v_out) {
    boolean b;
    is_empty_list(q.l, b);
    if (b) {
        v_out = 0;
    } else {
        head(q.l, v_out);
    }
}

void dequeue(queue q, ref queue q_out) {
    boolean b;
    is_empty_list(q.l, b);
    if (b) {
        q_out = new queue();
        nil(q_out.l);
    } else {
        q_out = new queue();
        tail(q.l, q_out.l);
    }
}

void equal_queue(queue q1, queue q2, ref boolean ret) {
    List q1_list;
    List q2_list;

    if (q1 == null || q2 == null) {
        ret = false;
    } else {
        equal_list(q1.l, q2.l, ret);
    }
}

void len_queue(queue q, ref int ret) {
    if (q == null) {
        ret = 0;
    } else {
        len_list(q.l, ret);
    }  
}