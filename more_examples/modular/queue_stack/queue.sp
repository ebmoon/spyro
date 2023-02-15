struct queue {
	Stack pushStack;
    Stack popStack;
}

void empty_queue(ref queue ret) {
    ret = new queue();
    empty(ret.pushStack);
    empty(ret.popStack);
}

void is_empty_queue(queue q, ref boolean ret) {
    is_empty_stack(q.popStack, ret);
}

void enqueue(queue q, int val, ref queue ret) {
    if (q == null) {
        ret = null;
    } else {
        ret = new queue();
        boolean b;
        is_empty_stack(q.popStack, b);
        if (b) {
            ret.pushStack = q.pushStack;
            push(q.popStack, val, ret.popStack);
        } else {
            push(q.pushStack, val, ret.pushStack);
            ret.popStack = q.popStack;
        }
    }
}

void front(queue q, ref int v_out) {
    boolean b;
    is_empty_stack(q.popStack, b);
    if (b) {
        v_out = 0;
    } else {
        top(q.popStack, v_out);
    }
}

void reverse(Stack st, ref Stack ret) {
    boolean b;
    Stack st_iter = st;

    empty(ret);
    is_empty_stack(st_iter, b);
    while(!b) {
        int x;
        top(st_iter, x);

        Stack st_tmp;
        pop(st_iter, st_tmp);
        st_iter = st_tmp;
        
        Stack ret_tmp;
        push(ret, x, ret_tmp);
        ret = ret_tmp;

        is_empty_stack(st_iter, b);
    }
}

void dequeue(queue q, ref queue q_out) {
    boolean b;
    is_empty_stack(q.popStack, b);
    if (b) {
        empty_queue(q_out);       
    }
    else {
        q_out = new queue();
        
        Stack st;

        pop(q.popStack, st);
        is_empty_stack(st, b);
        if (b) {
            empty(q_out.pushStack);
            reverse(q.pushStack, q_out.popStack);
        } else {
            q_out.pushStack = q.pushStack;
            q_out.popStack = st;
        }
    }
}

void equal_queue(queue q1, queue q2, ref boolean ret) {
    queue q1d;
    queue q2d;

    int x1;
    int x2;

    boolean b1;
    boolean b2;

    if (q1 == null || q2 == null) {
        ret = false;
    } else {
        is_empty_queue(q1, b1);
        is_empty_queue(q2, b2);

        if (b1) {
            ret = b2;
        } else if (b2) {
            ret = false;
        } else {
            front(q1, x1);
            front(q2, x2);

            if (x1 == x2) {
                dequeue(q1, q1d);
                dequeue(q2, q2d);
                equal_queue(q1d, q2d, ret);                
            } else {
                ret = false;
            }
        }
    }
}

void len_queue(queue q, ref int ret) {
    int tmp;
    len_stack(q.pushStack, tmp);
    len_stack(q.popStack, ret);
    ret = ret + tmp;
}