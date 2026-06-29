# Peter Chess Engine v6.3.1

A modified pygame chess engine for the HSC Software Engineering major project.

## Run

```bash
cd "Peter chess engine v6.3.1"
python3 -m pip install -r requirements.txt
python3 src/main.py
```

## Main Features

- Home menu before the match starts
- Player vs Player and Player vs Bot modes
- White, Black or Randomise colour selection
- 10 min Rapid, 3 min Blitz, 1 min Bullet and Endless modes
- Easy, Medium and Hard bot difficulties
- Approximate bot rating targets:
  - Easy: 200-400
  - Medium: 600-800
  - Hard: 1000-1200
- Bot thinking delay:
  - Easy: 4-5 seconds
  - Medium: 3-4 seconds
  - Hard: 2-3 seconds
- Five-second countdown before the clock begins
- Chess.com-style top and bottom player bars with player tags and clocks
- Timer display using minutes, seconds and hundredths
- Click-to-select and click-to-move controls
- Illegal move notification
- Check indication on the king
- Planning arrows for visual move planning
- Win/loss/draw result pop-up
- Post-game review with move history
- Theme changing that also updates the in-game UI colours
- v6.3.1 cogwheel settings menu for match actions

## v6.2.5 Changes

- Improved Easy bot so it behaves carelessly rather than simply avoiding captures.
- Easy bot now still takes pieces and attempts attacks, but can miss the tactical reply.
- Reworked in-game UI so timers and player names appear above and below the board.
- Reduced right sidebar clutter by moving live clock information out of the panel.
- Added a five-second pre-game countdown so players can prepare before the timer starts.
- UI colours now adapt to the selected board theme.

## v6.3.1 Changes

- Added a cogwheel settings button in the bottom-right corner.
- Moved Resign, Restart Match and Return to Home Menu into the settings menu.
- Kept Change Theme visible on the live sidebar.
- Removed the Clear Arrows button because clicking the board clears arrows.
- Enlarged and simplified live match text to make the side panel easier to read.
- Renamed Home Menu actions to Return to Home Menu.


## v6.3.1 Final UI polish
- Replaced the old sun-like settings symbol with an app-style gear/cog icon drawn using pygame shapes.
