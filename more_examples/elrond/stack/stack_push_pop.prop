//@Description Sketch to reverse a list.

var {
    stack push_s;
    int push_val;
    stack push_s_out;

    stack pop_s;
    stack pop_s_out;
    int pop_val_out;
}

relation {
    push(push_s, push_val, push_s_out);
    pop(pop_s, pop_s_out, pop_val_out);
}

generator {
    boolean AP -> compare(I, I)
                | is_empty(ST) | !is_empty(ST)
                | stack_equal(ST, ST) | !stack_equal(ST, ST);
    int I -> push_val | pop_val_out;
    stack ST -> push_s | push_s_out | pop_s | pop_s_out;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    stack -> empty() | push(stack, int);
}

struct list {
    int hd;
	list tl;
}

void nil(ref list ret) {
    ret = null;
}

void cons(int hd, list tl, ref list ret) {
    ret = new list();
    ret.hd = hd;
    ret.tl = tl;
}

void head(list l, ref int ret) {
    assert (l != null);

    ret = l.hd;
}

void tail(list l, ref list ret) {
    assert (l != null);

    ret = l.tl;
}

void is_empty_list(list l, ref boolean ret) {
    ret = (l == null);
}

void equal_list(list l1, list l2, ref boolean ret) {
    if (l1 == null || l2 == null) {
        ret = l1 == l2;
    } else {
        equal_list(l1.tl, l2.tl, ret);
        ret = l1.hd == l2.hd && ret;
    }
}

struct stack {
	list l;
}

void empty(ref stack ret) {
    ret = new stack();
    nil(ret.l);
}

void push(stack s, int val, ref stack ret) {
    assert s != null;

    ret = new stack();
    cons(val, s.l, ret.l);
}

void pop(stack s, ref stack ret_stack, ref int ret_val) {
    assert s != null;
    assert s.l != null;
    
    ret_stack = new stack();
    tail(s.l, ret_stack.l);
    head(s.l, ret_val);
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

void list_len(list l, ref int ret) {
    if (l == null) {
        ret = 0;
    } else {
        list_len(l.tl, ret);
        ret = ret + 1;
    }
}

void stack_len(stack s, ref int ret) {
    if (s == null) {
        ret = 0;
    } else {
        list_len(s.l, ret);
    }
}