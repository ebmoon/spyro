var {
    int x;
    int y;
}

relation {
    cube(x, y);
}

generator {
    boolean INEQ -> bvadd3(CX, CY, C) <= bvadd3(CX, CY, C);
    int CX -> bvmul(C, x);
    int CY -> bvmul(C, y);
    int C -> ??(8);
}

example {
    int -> ??(8);
}

void bvadd(int x, int y, ref int ret) {
    ret = (x + y) % 256; 
}

void bvadd3(int x, int y, int z, ref int ret) {
    ret = (x + y + z) % 256; 
}

void bvmul(int x, int y, ref int ret) {
    ret = (x * y) % 256;
}

void cube(int x, ref int ret) {
    bvmul(x, x, ret);
    bvmul(x, ret, ret);
}