# README

spyro synthesizes provably sound, most-precise specifications from given function definitions.



## Setup

### Requirements

* python (version >= 3.6)
* [Sketch](https://people.csail.mit.edu/asolar/) (version >= 1.7.6)

### Setting Sketch Path

You should add `sketch-frontend` directory to the environment variable `$PATH`.

Alternatively, you may set path to the Sketch binary, by editing `config` file:

```
SKETCH_PATH=<PATH TO SKETCH-FRONTENT>/sketch
```





## Running spyro

To run spyro on default setting, run `python spyro.py <PATH-TO-INPUT-FILE>`.
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
