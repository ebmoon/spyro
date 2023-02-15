adt List {
    Nil { }
	Cons { int hd; List tl; }
    Tail { List l; }
    Append { List l1; List l2; }
    Snoc { List l; int x; }
    Reverse { List l; }
}

void rewrite_isEmpty(List l, ref boolean ret) {
    switch(l) {
        case Nil: { ret = true; }
        case Cons: { ret = false; }
        case Tail: { assert false; }
        case Append: { assert false; }
        case Snoc: { assert false; }
        case Reverse: { assert false; }
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
        case Reverse: { assert false; }
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
        case Reverse: { assert false; }
    }
}

void rewrite_Head(List l, ref int ret) {
    switch(l) {
        case Nil: { assert false; }
        case Cons: { ret = l.hd; }
        case Tail: { assert false; }
        case Append: { assert false; }
        case Snoc: { assert false; }
        case Reverse: { assert false; }
    }
}

void rewrite_Tail(List l, ref List ret) {
    switch(l) {
        case Nil: { ret = new Tail(l=l); }
        case Cons: { ret = l.tl; }
        case Tail: { ret = new Tail(l=l); }
        case Append: { ret = new Tail(l=l); }
        case Snoc: { ret = new Tail(l=l); }
        case Reverse: { ret = new Tail(l=l); }
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
        case Reverse: { ret = new Snoc(l=l); }
    }
}

void rewrite_Reverse(List l, ref List ret) {
    switch(l) {
        case Nil: { ret = l; }
        case Cons: { rewrite_Snoc(l.tl, l.hd, ret); }
        case Tail: { ret = new Reverse(l=l); }
        case Append: { ret = new Reverse(l=l); }
        case Snoc: { ret = new Reverse(l=l); }
        case Reverse: { ret = new Reverse(l=l); }
    }
}

void rewrite_Append(List l1, List l2, ref List ret) {
    switch(l1) {
        case Nil: { ret = l2; }
        case Cons: { 
            List ll;
            rewrite_Append(l1.tl, l2, ll);
            ret = new Cons(hd=l1.hd, tl=ll);
        }
        case Tail: { assert false; }
        case Append: { assert false; }
        case Snoc: { assert false; }
        case Reverse: { assert false; }
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

void reverse(List l, ref List ret) {
    rewrite_Reverse(l, ret);
}

void is_empty_list(List l, ref boolean ret) {
    rewrite_isEmpty(l, ret);
}

void equal_list(List l1, List l2, ref boolean ret) { 
    rewrite_Equal(l1, l2, ret);
}

void append(List l1, List l2, ref List ret) {
    rewrite_Append(l1, l2, ret);
}

void len_list(List l, ref int ret) {
    rewrite_Len(l, ret);
}