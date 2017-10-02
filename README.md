# suvat-calculator
A simple, python suvat projectile calculator that takes any valid x and y values you have, and displays the rest.

**Currently only works for flat ground**

Changes that need to be made:

- [x] Changing the names of the equation functions to make them shorter and easier to call and edit. This will sacrifice some readability, but the readability for those names is terrible and can't improve more.
- [ ] Need to change the equation calculation functions which have more than one root to handle the multiple roots. This may be done by returning a list of the root.
- [ ] ~~Adding on a more versatile calculator for the downward y part of the trajectory. This needs to have an input for if the projectile is fired from above ground, which is often the case.~~
- [ ] Introducing an input interface for firing projectiles from above ground. See 2 for how this links in.
- [ ] A basic function for finding and using the separate components from a given resultant initial velocity and angle, if inputted.
- [ ] Add a section to then calculate values at a different instance ie when s = 10 or v = 5
- [ ] Create a projectile class to contain the projectiles info
- [ ] Use the apex to calc extra vals if can be done and potentially explore the use of calculus if either option is possible
- [ ] Allow multiple projectiles in one 2D space
- [ ] Create a GUI to visually show the projectiles motion
- [ ] Calculate points in which multiple projectiles will collide

**USAGE** 

1. Run 'run.sh' or 'suvatmenu.py' from terminal.
2. Input all x and y components given to you. Note that the y acceleration must be 0.
3. You will see a table of all x values and all y values up to the apex.

Wanna help? Testing is always helpful, and if you find problems or have ideas, make an issue or a pull request of course if you contribute to the code.
