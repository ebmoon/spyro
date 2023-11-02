var {
    private int a;
    int b;
}

relation {
    mul2(a, b);
}

generator {
    boolean AP -> div_by(Int, ??(3));
    int Int -> b;
}

example {
    int -> ??(3);
}

void mul2(int a, ref int b){
    b = 2 * a;
}

void div_by(int x, int y, ref boolean out){
    out = (x % y == 0);
}