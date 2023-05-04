var {
    int x;
    int y;
    boolean b;
}

relation {
    rel(x, y, b);
}

generator {
    boolean INEQ -> !b || bvadd3(CX, CY, C) <= bvadd3(CX, CY, C);
    int CX -> bvmul(C, x);
    int CY -> bvmul(C, y);
    int C -> ??(8);
}

example {
    int -> ??(8);
    boolean -> ??;
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

void rel(int x, int y, ref boolean ret) {
    ret = ((x + y + 4) % 256 <= (x + 15 * y + 7) % 256);
    ret = ret && ((2 * x + 14 * y + 3) % 256 <= (x + 15 * y + 7) % 256);
}