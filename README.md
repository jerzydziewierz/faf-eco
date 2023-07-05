# FAF Eco simulator


The objective is to figure out the build order for the best eco in FAF. 

The build order selection engine is adjustable so that it can be optimized against.

For a start, I assume that the player is UEF and the map is DualGap.


## Simulation engine

has these primary components:

* Unit classes deriving from "Entity" class
* Game state initialization procedure
* Game state step procedure
* Special conditions, if any
* Next build order selection procedure -- this is a parameterizable component
* Game state visualization and statistics
* Optimizer


The "Next build order selector" is the key component under research

The game simulator is a simplified model of the FAF game. It is not intended to be a full game simulator, but rather a simplified model of the game, which is sufficient to determine the best build order.

It carries the following assumptions:
* Only one bulding at the time is built -- all the "build power" of mobile builders is always concentrated
* The energy and mass usage algorithm is my own, it is not derived from the actual game. In my evaluation it appears to behave correctly, but who knows, maybe it is not correct.
* Where in doubt, optimistic simplifications are applied -- that is, the exact performance achieved by this simulator is possibly only a peak theoretical performance, and a player-executed build will likely be slower and more wasteful.
* No consideration is given to the builder movement time or collisions. 
* In this first iteration, building adjacency bonus is ignored, although this might be added later as special condition or other mechanism.

For entities, I am using a frozen attr class so that I can practice best practices for data classes.

On top of the static properties like cost and benefit, entities implement the following methods:
* can_be_built -- returns true if the entity can be built in the current game state
* on_build -- called when the entity is built, enables the entity's effects on the game state

## Build order selection

The build order selection is the key component of the simulation engine. It is a parameterizable component, which can be optimized against.
