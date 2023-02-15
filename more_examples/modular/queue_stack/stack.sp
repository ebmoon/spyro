adt Stack {
    Empty { }
	Push { Stack s; int x; }
    Pop { Stack s; }
}

void rewrite_isEmpty(Stack st, ref boolean ret) {
    switch(st) {
        case Empty: { ret = true; }
        case Push: { ret = false; }
        case Pop: { assert false; }
    }
}

void rewrite_Equal(Stack st1, Stack st2, ref boolean ret) {
    switch(st1) {
        case Empty: { rewrite_isEmpty(st2, ret); }
        case Push: { 
            boolean b;
            rewrite_isEmpty(st2, b);
            if (b) {
                ret = false;
            } else {
                int x;
                rewrite_Top(st2, x);
                if (st1.x == x) {
                    Stack s;
                    rewrite_Pop(st2, s);
                    rewrite_Equal(st1.s, s, ret);
                } else {
                    ret = false;
                }
            }
        }
        case Pop: { assert false; }
    }
}

void rewrite_Top(Stack st, ref int ret) {
    switch(st) {
        case Empty: { assert false; }
        case Push: { ret = st.x; }
        case Pop: { assert false; }
    }
}

void rewrite_Pop(Stack st, ref Stack ret) {
    switch(st) {
        case Empty: { ret = new Pop(s=st); }
        case Push: { ret = st.s; }
        case Pop: { ret = new Pop(s=st); }
    }
}

void rewrite_Len(Stack st, ref int ret) {
    switch(st) {
        case Empty: { ret = 0; }
        case Push: { rewrite_Len(st.s, ret); ret = ret + 1; }
        case Pop: { assert false; }
    }
}

void empty(ref Stack ret) {
    ret = new Empty();
}

void push(Stack st, int x, ref Stack ret) {
    ret = new Push(s=st, x=x);
}

void top(Stack st, ref int ret) {
    rewrite_Top(st, ret);
}

void pop(Stack st, ref Stack ret) {
    rewrite_Pop(st, ret);
}

void is_empty_stack(Stack st, ref boolean ret) {
    rewrite_isEmpty(st, ret);
}

void equal_stack(Stack st1, Stack st2, ref boolean ret) { 
    rewrite_Equal(st1, st2, ret);
}

void len_stack(Stack st, ref int ret) {
    rewrite_Len(st, ret);
}