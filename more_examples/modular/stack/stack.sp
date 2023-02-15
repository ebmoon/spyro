struct stack {
	List l;
}

void empty(ref stack ret) {
    ret = new stack();
    nil(ret.l);
}

void push(stack s, int val, ref stack ret) {
    if (s == null) {
        ret = null;
    } else {
        ret = new stack();
        cons(val, s.l, ret.l);
    }
}

void pop(stack s, ref stack ret_stack) {
    if (s == null || s.l == null) {
        ret_stack = null;
    } else {
        ret_stack = new stack();
        tail(s.l, ret_stack.l);
    }
}

void top(stack s, ref int ret_val) {
    if (s == null || s.l == null) {
        ret_val = 0;
    } else {
        head(s.l, ret_val);
    }
}

void is_empty(stack s, ref boolean ret) {
    is_empty_list(s.l, ret);
}

void stack_equal(stack s1, stack s2, ref boolean ret) {
    if (s1 == null || s2 == null) {
        ret = s1 == s2;
    } else {
        equal_list(s1.l, s2.l, ret);
    }
}

void stack_len(stack s, ref int ret) {
    if (s == null) {
        ret = 0;
    } else {
        list_len(s.l, ret);
    }
}