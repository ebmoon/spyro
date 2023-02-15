//@Description Sketch to reverse a list.

var {
    stack s;
    int v;
    stack push_out;

    boolean top_err;
    int top_out;
}

relation {
    push(s, v, push_out);
    top(push_out, top_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | is_empty(s) | !is_empty(s);
    boolean RHS -> top_out == I;
    int I -> v | top(ST);
    stack ST -> s | empty();
}

example {
    int -> ??(3) | -1 * ??(3) ;
    boolean -> true | false;
    stack -> empty() | push(stack, int);
}

adt List {
    Nil { }
	Cons { int hd; List tl; }
    Tail { List l; }
    Append { List l1; List l2; }
    Snoc { List l; int x; }
}

void rewrite_isEmpty(List l, ref boolean ret) {
    switch(l) {
        case Nil: { ret = true; }
        case Cons: { ret = false; }
        case Tail: { assert false; }
        case Append: { assert false; }
        case Snoc: { assert false; }
    }
}

void rewrite_Len(List l, ref int ret) {
    switch(l) {
        case Nil: { ret = 0; }
        case Cons: { 
            rewrite_Len(l.tl, ret); 
            ret = ret + 1;
        }
        case Tail: { assert false; }
        case Append: { assert false; }
        case Snoc: { assert false; }
    }
}

void rewrite_Equal(List l1, List l2, ref boolean ret) {
    switch(l1) {
        case Nil: { rewrite_isEmpty(l2, ret); }
        case Cons: { 
            boolean b;
            rewrite_isEmpty(l2, b);
            if (b) {
                ret = false;
            } else {
                int x;
                rewrite_Head(l2, x);
                if (l1.hd == x) {
                    List ll;
                    rewrite_Tail(l2, ll);
                    rewrite_Equal(l1.tl, ll, ret);
                } else {
                    ret = false;
                }
            }
        }
        case Tail: { assert false; }
        case Append: { assert false; }
        case Snoc: { assert false; }
    }
}

void rewrite_Head(List l, ref int ret) {
    switch(l) {
        case Nil: { assert false; }
        case Cons: { ret = l.hd; }
        case Tail: { assert false; }
        case Append: { assert false; }
        case Snoc: { assert false; }
    }
}

void rewrite_Tail(List l, ref List ret) {
    switch(l) {
        case Nil: { ret = new Tail(l=l); }
        case Cons: { ret = l.tl; }
        case Tail: { ret = new Tail(l=l); }
        case Append: { ret = new Tail(l=l); }
        case Snoc: { ret = new Tail(l=l); }
    }
}

void rewrite_Snoc(List l, int x, ref List ret) {
    switch(l) {
        case Nil: { ret = new Cons(hd=x, tl=new Nil()); }
        case Cons: { 
            List ll;
            rewrite_Snoc(l.tl, x, ll);
            ret = new Cons(hd=l.hd, tl=ll); 
        }
        case Tail: { ret = new Snoc(l=l); }
        case Append: { ret = new Snoc(l=l); }
        case Snoc: { ret = new Snoc(l=l); }
    }
}

void nil(ref List ret) {
    ret = new Nil();
}

void cons(int hd, List tl, ref List ret) {
    ret = new Cons(hd = hd, tl = tl);
}

void head(List l, ref int ret) {
    rewrite_Head(l, ret);
}

void tail(List l, ref List ret) {
    rewrite_Tail(l, ret);
}

void snoc(List l, int x, ref List ret) {
    rewrite_Snoc(l, x, ret);
}

void is_empty_list(List l, ref boolean ret) {
    rewrite_isEmpty(l, ret);
}

void equal_list(List l1, List l2, ref boolean ret) { 
    rewrite_Equal(l1, l2, ret);
}

void list_len(List l, ref int ret) {
    rewrite_Len(l, ret);
}

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