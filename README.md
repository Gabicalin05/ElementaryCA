# Elementary Cellular Automaton

One directional cellular automaton. Each cell has two possible states:

* `1` - alive
* `0` - dead

The program prompts the user to choose one of the 256 rules (0 - 255), and generates the requested pattern.

## Code explanation

### Draw function
Prints each line, one by one

### Rules
Converts all cells into a binary number by joining them, then flips the number (as per Wolfram) and converts back to int for user friendliness.

### Generation 0
Generation 0 is created from an array of "dead cells" multiplied by the chosen number of cells, `n_cells`, to display. The array is split into 2, and the middle element is replaced with an "alive cell."

