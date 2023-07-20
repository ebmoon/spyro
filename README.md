# Spyro[Sketch] OOPSLA 2023 Artifact

This is the artifact for paper #481 "Synthesizing Specifications". 

Spyro synthesizes provably sound, most-precise specifications from given function definitions.


## Claims

### Claims supported by this artifact

The artifact supports the following claims:

1. Quantitative analysis:
    * Application 1: Spyro[Sketch] can synthesize the best L-properties for 35/35 Spyro[Sketch] problems and guarantee that 34 out of 35 are the best L-conjunctions.
    * Application 2: Spyro[Sketch] can synthesize the best algebraic properties for 12/12 Spyro[Sketch] problems from the ArrayList, ArraySet, and HashMap modules, and guarantee that all they are the best L-conjunctions.
    * Application 3: Spyro[Sketch] can synthesize the best sensitivity L-properties for 18/18 Spyro[Sketch] problems about Hamming/edit distance on List functions, and guarantee that all they are the best L-conjunctions.
    * Application 4: Spyro[Sketch] can synthesize the best 4-bit inequalities for 9/9 Spyro[Sketch] problems from bit-vector operations, and guarantee that 8/9 are the best L-conjunctions.

 for 35/35 benchmark problems, and guarantee 34/35 are best L-conjunction.

2. The Algorithm 1 with line 12 is faster than the Algorithm 1 without line 12.


### Claims not supported by this artifact

This artifact may not support some claims of the paper. Specifically,

1. The running time and number of SMT calls may be different to Table 1 or Table 2.

2. Each conjunct synthesized by Spyro[Sketch] may be different to the Fig. 3, while the L-conjunctions are equivalent.

#### Reason

All the evaluation data of paper (including Table 1, 2 and Fig. 3) were generated from Apple M1 8-core CPU with 8GB RAM.
Sketch binary compiled for different architecture / OS may produce different results.
Spyro[Sketch] has a high variance in running time. To obtain reliable results, it is recommended to execute it with a minimum of three random seeds.

## Setup

### Requirements

The artifact requires dependencies if you try to run on your local machine

* python (version >= 3.6), including
    * numpy (only for `run_benchmarks.py`)
* [Sketch](https://people.csail.mit.edu/asolar/) (version >= 1.7.6)
    * Note: The tar-ball in the Sketch wiki is 1.7.5, which may not work

### Setting Sketch Path

You should add `sketch-frontend` directory to the environment variable `$PATH`.

Alternatively, you may set path to the Sketch binary, by editing `config` file:

```
SKETCH_PATH=<PATH TO SKETCH-FRONTENT>/sketch
```


## Structure of this artifact

* `config.ini` contains path to the Sketch binary or directory to store temporary files

* `benchmarks` contains all the Spyro[Sketch] benchmarks.
    * `benchmarks/application1` contains all the specification mining benchmarks from the section 5.1.
    * `benchmarks/application2` contains all the algebraic specification synthesis benchmarks from the section 5.2.
    * `benchmarks/application3` contains all the sensitivity analysis benchmarks from the section 5.3.
    * `benchmarks/application4` contains all the bit-vector inequality benchmarks from the section 5.4.

* `tmp` contains temporary files created during the running of Spyro[Sketch]

* `results` contains the result of execution.



## Running the evaluation

### Running Spyro[Sketch] for single example

To run spyro on default setting, run `python3 spyro.py <PATH-TO-INPUT-FILE>`.
This will synthesize minimized properties from input file, and print the result to `stdout`.


### Flags

* `infiles`: Input files. Use concatenation of all files as the input code.
* `outfile`: Output file. Default is `stdout`
* `-v, --verbose`: Print descriptive messages, and leave all the temporary files.
* `--write-log`: Write trace log if enabled. 
* `--timeout`: Timeout of each query to Sketch. Default is 300s.
* `--disable-min`: Disable formula minimization.
* `--keep-neg-may`: Disable freezing negative examples.
* `--num-atom-max`: Number of disjuncts. Default is 3.
* `--inline-bnd`: Number of inlining/unrolling. Default is 5.

### Understanding Spyro[Sketch] input

Spyro[Sketch] takes one or more files as input and treats those files as concatenated into a single input file. Each set of input file must contain exactly one definition for `var`, `relation`, `generator`, and `example`. The following is an example of each section for list reverse function.

#### Variables
```
// Input and output variables
var {
    list l;
    list lout;
}
```

#### Signature
```
// Target functions that we aim to synthesize specifications
// The last argument to the function is output
relation {
    reverse(l, lout);
}
```

#### Property generator (i.e. search space)
```
// The DSL for the specifictions.
// It uses the top predicate as a grammar for each disjunct.
// The maximum number of disjuncts are provided by the option "--num-atom-max"
// compare is macro for { == | != | <= | >= | < | > }
// ??(n) denotes arbitrary positive integer of n bits
// Provide only input arguments to function call
generator {
    boolean AP -> is_empty(L) | !is_empty(L) 
                | equal_list(L, L) | !equal_list(L, L)
                | compare(S, S + ??(1));            
    int S -> len(L) | 0 ;
    list L -> l | lout ;
}
```

#### Example generator (i.e. example domain)
```
// recursive constructor for each type
// Provide only input arguments to function call
// integer is chosen from arbitrary positive or negative 3-bits integer
example {
    int -> ??(3) | -1 * ??(3) ;
    list -> nil() | cons(int, list);
}
```

### Implementation
```
// The return value of function is passed by reference
void reverse(list l, ref list ret) {
    if (l == null) {
        ret = null;
    } else {
        list tl_reverse;
        reverse(l.tl, tl_reverse);
        snoc(tl_reverse, l.hd, ret);
    }
}
```

### Understanding Spyro[Sketch] output

The synthesize properties are given as a code that returns a Boolean value, where the value is stored in the variable `out`. 
It means that the value stored in `out` must always be true.

For example, the following is synthesized properties of `application1/list/reverse.sp`:

```
Property 0

bit var_50 = 0;
equal_list(lout, l, var_50);
int var_52 = 0;
len(l, var_52);
bit out_s1 = var_50 || (var_52 > 1);
out = out_s1;


Property 1

int var_102 = 0;
len(lout, var_102);
int var_102_0 = 0;
len(l, var_102_0);
out = var_102 == var_102_0;
```

The property 0 means
$$eq(l_{out}, l) \vee len(l) > 1$$
must be true.

The property 1 means
$$len(l_{out}) == len(l)$$
must be true.

### Running Spyro[Sketch] for benchmark set

Command `python3 run_benchmarks.py -a` will run Spyro[Sketch] for every benchmark problem with three differents random seeds `[32, 64, 128]`. You can execute only certain applications using the `-1`, `-2`, `-3` and `-4` arguments. For example, the command `python3 run_benchmarks_full.py -1 -3` only runs application 1 and application 3. Running `python3 run_benchmarks.py -a` will take about 2-3 days.

This will generate files containing synthesized properties and CSV files containing statistics in the `results` directory. For example, `application1_default_32.csv` contains statistics for Application 1 with seed 32, and `application3_nofreeze_128.csv` contains statistics for Application 3 with seed 128, executed without freezing negative examples.
It also creates files with suffix `_median`, which has median running time among three runs.

`python3 run_benchmarks_median.py` does the same to `python3 run_benchmarks.py`, but only run each benchmark problem with single random seed value, which generated the median value on our local machine. The output file of `run_benchmarks_median.py` will have suffix `_median`. Running `python run_benchmarks_median.py -a` will take less than 20 hours.

