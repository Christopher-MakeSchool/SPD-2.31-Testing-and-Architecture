# Refactor Process

1. Put on your favorite music playist.
2. Rename the file from `Tic_Toc_toe_messy.py` to `Tic_Tac_toe_messy.py`
3. Update locale readme line spelling as well
4. Git Comit: \
   `ga .;gcsmg "[Update]: File Name Type Toc To Tac In Tic_Tac_toe_messy.py"` \
   or \
   `git add .;git commit message "[Update]: File Name Typo: Toc To Tac In Tic_Tac_toe_messy.py"`
5. Run the file a few times (2-5) to test it's inital execution and mark down edge cases to look for
   1. Greeted with a choice to be `X` or `O` in the welcome message below: \
        Welcome to Tic Tac Toe! \
        Do you want to be X or O? \
    We can assume we are to only expect a string input of these 2 options, if not we are to handle the situaton appropriately. Next run thorugh we will test a few inputs here. In the meantime, let's choose `X` and `Press Enter?`, we are immediately prompted with a 3x3 grid with the computer going first up in the top right corner. After loosing to the computer by inputing the index of our spaces 1-9 starting at the bottom left to the top right. We are prompted with: \
        `The computer has beaten you! You lose.` \
        `Do you want to play again? (yes or no)` \
    Obviously we chose `yes` to test their continuation funionality. Hooray! It works.
   2. Going back to our first edage case to test, let's try a few inputs that aren't `X` or `O` like [`1-9`, `A-Z`, `a-z`, `Q`, `q`, `hello`, `etc`], from these we are just reprompted: `Do you want to be X or O?`. After running through another game, we won this match and got a modified continuation prompt: \
        `Hooray! You have won the game!` \
        `Do you want to play again? (yes or no)`
   3. We chose `y` to test more edge cases on thier inputs. Hooray! It works. Now let's test some of the positional edge cases we'd expect to see:
        - Can we input letters?                     Nope
        - Can we input numbers incased in quotes?   Nope
        - Can we go on a place already claimed?     Nope
        - Do they account for Draws?                Yep
        - Are you able to quite in the end game?    Yep
6. Now lets open up the file and skim through our #Todos & what lines & methods we find repeating. \
   A Commple things we notice off the bat are:
   1. Their is no `Entry Point` into the file i.e, `if __name__ == "__main__":`
   2. The file is initally 200 lines long
   3. Number of TODOs: \
        18 on lines (4, 5, 61, 73, 84, 98, 100, 103, 129, 149, 150, 155, 159, 162, 174, 179, 191, 196)
   4. It's intial function methods are:
      - drawBoard(board)                            line 12
      - inputPlayerLetter()                         line 28
      - whoGoesFirst()                              line 42
      - playAgain()                                 line 49
      - makeMove(board, letter, move)               line 54
      - isWinner(bo, le)                            line 57
      - getBoardCopy(board)                         line 69
      - isSpaceFree(board, move)                    line 78
      - getPlayerMove(board)                        line 82
      - chooseRandomMoveFromList(board, movesList)  line 90
      - getComputerMove(board, computerLetter)      line 103
      - isBoardFull(board)                          line 139
   5. We should also Add/fix any function's docstrings (using """ insted of #)
7. Using Any &/or All of The Techniques you have learned: \
   **Blod Items:** represent comonly used Techniques \
   - **`Consolidate Conditional Expression`**,
   - **`Decompose Conditional`**,
   - **`Extract Class`**,
   - **`Extract Method`**,
   - **`Extract Superclass`**,
   - `Inline Method`,
   - **`Introducing Explaining Variable`**,
   - `Move Attribute`,
   - `Remove Assignment to Method Parameter`,
   - `Rename Method`,
   - **`Remove Control Flag`**,
   - `Replace Temp with query`,
   - **`Replace Magic Number with Symbolic Constant`**,
   - **`Replace Nested Conditional With Gaurd Clauses`**,
   - **`Split Temporary Variable`**,
8. Fix The Programs Readability, Usability, & Performance By applying the Scratch & Sniff Methodology To This Damp Smelly Code.

---

# PLAN OF ATTACK

## Refactor 1: Entrypoint & Main Function Lines 145-200

1. Starting clsoe to the bttom, Lines 145/6 - 200 is our entry point so let's add a main funcion around it.
2. Then we will run through the TODOs on lines: (149, 155, 159, 162, 174, 179, 191, 196)
   1. (149): The following mega code block is a huge hairy monster. Break it down
   2. (155): Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
   3. (159): Study how this variable is used. Does it ring a bell? (which refactoring method?)
   4. (162): Usually (not always), loops (or their content) are good candidates to be extracted into their own function
   5. (174): Is this 'else' necessary?
   6. (179): Is this 'else' necessary?
   7. (191): Is this 'else' necessary?
   8. (196): Is this 'else' necessary?
3. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
4. Git Comit: `ga .;gcsmg "[Refactor]: Entrypoint & Main Function Lines 145-200"`

## Refactor 2: Move Functions Lines 82-137

Continuing our accent back to the top of this program, next we will

1. Run through the TODO(s) in the function: getComputerMove()
   1. (103): W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
   2. (129): Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
   3. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
2. Run through the TODO(s) in the function: chooseRandomMoveFromList(board, movesList)
   1. (98): How would you write this pythanically? (You can google for it!)
   2. (100): Is this 'else' necessary?
   3. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
3. Run through the TODO(s) in the function: getPlayerMove(board)
   1. (84): W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
   2. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
4. Git Comit: `ga .;gcsmg "[Refactor]: Move Functions Lines 82-137"`

## Refactor 2: Board Functions Lines 12-26, 69-80, & 139-144

Almost finished in our refactoring journey, lets run through and modify any of the TODO(s) that affact the boards functionality

1. For The TODO(s) in The Function: isBoardFull(board)     on line 139,
   1. No TODOs but can be refactored for visibility and functionailty.
   2. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
2. For The TODO(s) in The Function: getBoardCopy(board)    on line 69,
   1. Clean this mess!
   2. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
3. For The TODO(s) in The Function: drawBoard(board)       on line 12,
   1. No TODOs but can be refactored for visibility and functionailty.
   2. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
4. Git Comit: `ga .;gcsmg "[Refactor]: Board Functions Lines 12-26, 69-80, & 139-144"`

## Refactor 2: Play Functions Lines 28-67

Rounding off on the remaing functions,

1. Find The TODO(s) Under The Function: isWinner(bo, le)       on line 57,
   1. Fix the indentation of this lines and the following ones.
   2. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
2. Find The TODO(s) Under The Function: makeMove()             on line 54,
   1. No TODOs, Ratehr Consice & To The Point, Greate Job.
   2. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
3. Find The TODO(s) Under The Function: playAgain()            on line 49,
   1. No TODOs but can be refactored for visibility and functionailty.
   2. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
4. Find The TODO(s) Under The Function: whoGoesFirst()         on line 42,
   1. No TODOs but can be refactored for visibility and functionailty.
   2. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
5. Find The TODO(s) Under The Function: inputPlayerLetter()    on line 28,
   1. No TODOs but can be refactored for visibility and functionailty.
   2. After adjusting these lets run the progam again to test our changes, using the same steps from before, Log any errors below, Remember to link to support or solutions.
6. Git Comit: `ga .;gcsmg "[Refactor]: Play Functions Lines 28-67"`

## Refactor 2: Add/Fix (New) Function Docstrings

- Remember to Annotate the Dockstrings using """Function Name... """ insted of #
- Git Comit: `ga .;gcsmg "[Refactor]: Add/Fix (New) Function Docstrings"`

---

## Final Reflection & Documentation

---

## Rubric

![Rubric](images/Rubric.png)

Rubric is viewable on [Gradescope - Final Exam](https://www.gradescope.com/courses/206382/assignments/1065830)

## Code Review and Feedback

_Instructor feedback will appear in this space._
