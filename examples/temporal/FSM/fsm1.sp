var {
    private int n;
    Trace tr;
}

relation {
    prog(n, tr);
}

generator {
    boolean AP -> FSM2(PNT, PNT, PNT, PNT, ??(1), ??(1));
    BoolArray PNT -> eqx(tr, ??(1)) | all_b(tr, ??(1));
}

example {
    int -> ??(3) + 1;
    Event -> genEvent();
    Trace -> newTrace() | addTrace(Trace, Event);
}

struct Event{
    boolean x;
}

generator void genEvent(ref Event e)
{
    e = new Event(x = ??(1));
}

void all_b(Trace tr, boolean b, ref BoolArray ret)
{
    newBoolArray(ret);
    for(int i=0;i<tr.size;i++)
        addBoolArray(ret, b, ret);
}

void eqx(Trace tr, int p, ref BoolArray ret) {
    newBoolArray(ret);
    for(int i=0;i<tr.size;i++) 
    {
        boolean b = (tr.events[i].x == p);
        addBoolArray(ret, b, ret);   
    }
}

void FSM2(BoolArray T00, BoolArray T01, BoolArray T10, BoolArray T11, bit F0, bit F1, ref boolean ret) {
    int cur = 0;
    int n = T00.size;
    for(int i = 0; i < n; i++)
    {
        if(cur == 0) {
            boolean t00, t01;
            getBoolArray(T00, i, t00);
            getBoolArray(T01, i, t01);
            if(t00 == 1)
                cur = 0;
            else if(t01 == 1)
                cur = 1;
            else {
                ret = 0;
                return ;
            }
        }
        else {
            boolean t10, t11;
            getBoolArray(T10, i, t10);
            getBoolArray(T11, i, t11);
            if(t10 == 1)
                cur = 0;
            else if(t11 == 1)
                cur = 1;
            else {
                ret = 0;
                return ;
            }
        }
    }
    if(cur == 0) ret = F0;
    else ret = F1;
}


void prog(int n, ref Trace tr) {
    newTrace(tr);
    for(int i = 0; i < n; i++)
    {
        boolean x;
        if((i % 2) == (n % 2)) 
            x = 0;
        else 
            x = 1;
        Event e = new Event(x = x);
        addTrace(tr, e, tr);
    }
}