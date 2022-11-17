# Navy-scheduler
  a scheduling project for the israeli navy.
  
# Intro
  Since 2005, the Gaza strip is under a maritime closure.
  maintaining the closure is complicated. it requires a lot of planning.
  "916" is the navy unit that is responsible for it.
  
  in years 2005-2020 the shceduling of the positions was made manually.
  The officers put in a lot of effort and many hours of work for solving the weekly "sudoku puzzle".
  
  THIS IS HOW THE ISRAELI NAVY MANAGES THE CLOSURE OF GAZA.
  
# The problem  
  there are several "positions" to staff (it is a bit more complicated).
  there are many staffing "rules", for example:
  - a ship should not be outside the port for more than 72 hours.
  - a ship should not staff the "hard" position for two days straight.
  - a ship cant have more than X hours outside the port in a month.
  
  - and much more that should not be detailed for understandable reasons.
  
  as time passed - more and more rules were added.
  the officers could not solve it any more - it was too hard.
  
  this program solves the puzzle and give the soldiers a free weekend if possible.
  
# Input example
![image](https://user-images.githubusercontent.com/85450521/202538631-e018548d-e900-4c37-8182-1b4428d6c51e.png)


# Output example

![image](https://user-images.githubusercontent.com/85450521/202537810-885e7060-9d45-476c-bcd3-460708bc35b5.png)

   
# How it Works
  the program is actually a recursive algorithm.
  each "rule" is calculated for how restrictive he is.
  the program starts scheduling the ships under the most restrictive "rules".
  every schedule is of course validated for being "legal".
  
  if the all next schedule options are not legal - it goes back in the recursion.
