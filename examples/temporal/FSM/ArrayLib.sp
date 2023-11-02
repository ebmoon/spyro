struct Trace {
    int size;
    Event[size] events;
}

void newTrace(ref Trace ret) {
    int size = 0;
    Event[size] events;

    ret = new Trace(
        size = size,
        events = events
    );
}

void addTrace(Trace arr, Event e, ref Trace ret) {
    int size = arr.size + 1;

    Event[size] events;

    events[0::arr.size] = arr.events[0::arr.size];
    events[arr.size] = e;
    
    ret = new Trace(
        size = size,
        events = events
    );
}

void sizeTrace(Trace arr, ref int ret) {
    ret = arr.size;
}

void getTrace(Trace arr, int idx, ref Event ret) {
    ret = arr.events[idx];
}




struct BoolArray {
    int size;
    boolean[size] elements;
}

void newBoolArray(ref BoolArray ret) {
    int size = 0;
    boolean[size] elements;

    ret = new BoolArray(
        size = size,
        elements = elements
    );
}

void addBoolArray(BoolArray arr, boolean e, ref BoolArray ret) {
    int size = arr.size + 1;

    boolean[size] elements;

    elements[0::arr.size] = arr.elements[0::arr.size];
    elements[arr.size] = e;
    
    ret = new BoolArray(
        size = size,
        elements = elements
    );
}

void sizeBoolArray(BoolArray arr, ref int ret) {
    ret = arr.size;
}

void getBoolArray(BoolArray arr, int idx, ref boolean ret) {
    ret = arr.elements[idx];
}