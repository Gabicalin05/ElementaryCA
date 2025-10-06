# Elementary Cellular Automaton

One directional cellular automaton. Each cell has two possible states:

* `1` - alive
* `0` - dead

The program prompts the user to choose one of the 256 rules (0 - 255), and generates the requested pattern.

## Code explanation

### Rules function
Reads the current cell neighborhood, `left`, `center`, and `right`, and converts each one into one of the binary states 
to identify one of the eight possible neighborhood patterns.

The three bits are joined together into a single binary string, which is then converted to `int`, then flipped (as per
Wolfram's convention).

The function returns the corresponding new state from the ruleset list.

### Generation 0
Generation 0 is created from an array of "dead cells" multiplied by the chosen number of cells, `n_cells`, to display. 
The array is split in half, and the middle element is replaced with an "alive cell."

The `int` input from the user is converted into binary with 8 digits zero-padded on the left, and used to build the 
`ruleset` list. Generation 0 is then displayed.

### New Generations
The program creates up to 100 more generations after the initial one.

In the `newGen`, each cell's new value depends on its neighbors. A wraparound (`(i +- 1) % n`) was used to handle the 
edges, first and last cells, going out of bounds. 

### Draw function
Prints each line, one by one.
