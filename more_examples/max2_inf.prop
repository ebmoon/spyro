//@Description Toy benchmarks to show complex recursive generators.

var {
    int x1;
    int x2;
    int o;
}

relation {
    max2(x1, x2, o);
}

generator {
    boolean B -> AP | (AP || B) ;
    boolean AP -> compare(I, I) ;
    int I -> x1 | x2 | o ;
}

example {
    int -> ??(5) | -1 * ??(5) ;
}

void max2(int x, int y, ref int out){
    if (x > y) {
        out = x;
    } else {
        out = y;
    }
}