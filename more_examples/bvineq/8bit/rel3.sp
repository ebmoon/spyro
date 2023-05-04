var {
    int x;
    int y;
}

relation {
    div2(x, y);
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

void div2(int x, ref int ret) {
    ret = (x / 2) % 256; 
}