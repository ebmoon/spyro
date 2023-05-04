//@Description 

var {
    HashMap map;
    int key;
    int value;
    HashMap put_out;

    int key2;
    int get_out;
    boolean err;

    boolean err_sub;
}

relation {
    put(map, key, value, put_out);
    get(put_out, key2, err, get_out);
}

generator {
    boolean AP -> !GUARD || RHS;
    boolean GUARD -> true | K == K | K != K;
    boolean RHS -> err | get_out == V && !err;
    HashMap M -> map | newHashMap();
    int K -> key | key2;
    int V -> value | get(M, K, err_sub);
}

example {
    int -> ??(3) | -1 * ??(3) ;
    HashMap -> newHashMap() | put(HashMap, int, int);
    boolean -> true | false;
}