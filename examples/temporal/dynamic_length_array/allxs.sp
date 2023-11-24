var {
    int n;
    int p;
    Trace tr;
}

relation {
    prog(n, p, tr);
}

generator {
    boolean AP -> Now(PT);
    BoolArray PT -> Globally(PNT) | Eventually(PNT);
    BoolArray PNT -> eqx(tr, p) | eqx(tr, 1) | eqx(tr, 0);
}


example {
    int -> ??(3);
    boolean -> ??(1);
    Event -> genEvent();
    Trace -> newTrace() | addTrace(Trace, Event);
}


struct Event{
    int x;
}

generator void genEvent(ref Event e)
{
    e = new Event(x = ??(3));
}

void Eventually(BoolArray seq, ref BoolArray ret) {
    boolean[seq.size] elements;
    elements[seq.size - 1] = seq.elements[seq.size - 1];
    for(int i = seq.size - 2; i >= 0; i--) 
        elements[i] = elements[i+1] || seq.elements[i];
    ret = new BoolArray(
        size = seq.size,
        elements = elements
    );
}

void Globally(BoolArray seq, ref BoolArray ret) {
    boolean[seq.size] elements;
    elements[seq.size - 1] = seq.elements[seq.size - 1];
    for(int i = seq.size - 2; i >= 0; i--) 
        elements[i] = elements[i+1] && seq.elements[i];
    ret = new BoolArray(
        size = seq.size,
        elements = elements
    );
}

void Now(BoolArray seq, ref boolean ret)
{
    ret = seq.elements[0];
}


void eqx(Trace tr, int p, ref BoolArray ret) {
    newBoolArray(ret);
    for(int i=0;i<tr.size;i++) 
    {
        boolean b = (tr.events[i].x == p);
        addBoolArray(ret, b, ret);   
    }
}

void prog(int n, int p, ref Trace tr) {
    newTrace(tr);
    for(int i=0;i<n;i++)
    {
        Event e = new Event(x = p);
        addTrace(tr, e, tr);
    }
}