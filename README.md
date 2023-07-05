# FAF Eco simulator


The objective is to figure out the build order for the best eco in FAF. The build order is based on the following assumptions:

* The player is UEF
* The player is on the "Dual Gap" map


## Simulation engine

has these primary components:

* Unit classes deriving from "Entity" class
* Game state initialization procedure
* Game state step procedure
* Special conditions
* Next build order selection procedure
* Game state visualization and statistics
* Optimizer


The "Next build order selector" is the key component under research

The game simulator is a simplified model of the FAF game. It is not intended to be a full game simulator, but rather a simplified model of the game, which is sufficient to determine the best build order.
It carries the following assumptions:
* Only one bulding at the time is built -- all the "build power" of mobile builders is always concentrated
* The energy and mass usage algorithm is my own, it is not derived from the actual game. In my evaluation it appears to behave correctly, but who knows, maybe it is not
* Where in doubt, optimistic simplifications are applied -- that is, the exact performance achieved by this simulator is possibly only a peak theoretical performance, and a player-executed build will likely be slower and more wasteful. In particular, no consider
* No consideration is given to the builder movement time or collisions. 
* In the first iteration, building adjecency bonus is ignored, altough this might be added later

