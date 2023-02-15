//@Description Sketch to reverse a list.

var {
    int hd;
    list tl; 
    list lout;

    int u;
    int v;
}

relation {
    cons(hd, tl, lout);
}

generator {
    boolean AP -> mem(L, I) | !mem(L, I) 
                | ord(L, I, I) | !ord(L, I, I) 
                | compare(I, I);
    int I -> u | v | hd | head(L);
    list L -> tl | lout;
}

example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
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

void append(list l1, list l2, ref list ret) {
    if (l1 == null) {
        ret = l2;
    } else {
        list tl_append;
        append(l1.tl, l2, tl_append);
        cons(l1.hd, tl_append, ret);
    }
}

void mem(list l, int x, ref boolean ret) {
    if (l == null) {
        ret = false;
    } else if (x == l.hd) {
        ret = true;
    } else {
        mem(l.tl, x, ret);
    }
}

void ord(list l, int x, int y, ref boolean ret) {
    if (l == null) {
        ret = false;
    } else if (x == l.hd) {
        mem(l.tl, y, ret);
    } else {
        ord(l.tl, x, y, ret);
    }
}