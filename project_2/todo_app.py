import curses

# Function to display the to-do list
def display_todo(stdscr, todo_list):
  stdscr.clear()
  stdscr.border(0)
  y = 2
  x = 2
  for item, is_done in todo_list:
    checkbox = "☑" if is_done else "☐"
    stdscr.addstr(y, x, checkbox, curses.A_BOLD)
    stdscr.addstr(y, x + 2, item)
    y += 1
  stdscr.refresh()

# Function to add a new to-do item
def add_todo(stdscr, todo_list):
  stdscr.clear()
  stdscr.border(0)
  stdscr.addstr(2, 2, "Enter new to-do item: ", curses.A_BOLD)
  stdscr.refresh()
  new_item = stdscr.getstr().decode("utf-8")
  todo_list.append((new_item, False))
  display_todo(stdscr, todo_list)

# Function to mark an item as done/undone
def toggle_done(stdscr, todo_list, index):
  todo_list[index][1] = not todo_list[index][1]
  display_todo(stdscr, todo_list)

def main():
  # Initialize curses screen
  stdscr = curses.initscr()
  curses.cbreak()
  stdscr.keypad(True)

  todo_list = []

  while True:
    display_todo(stdscr, todo_list)
    key = stdscr.getch()

    if key == curses.KEY_ENTER:
      add_todo(stdscr, todo_list)
    elif key == curses.KEY_DELETE and len(todo_list) > 0:
      stdscr.addstr(stdscr.getcury(), stdscr.getcurx(), " (Are you sure? y/n) ")
      stdscr.refresh()
      confirm = stdscr.getch().decode("utf-8").lower()
      if confirm == 'y':
        todo_list.pop()
    elif 0 <= key <= len(todo_list) - 1:
      toggle_done(stdscr, todo_list, key)
    elif key == ord('q'):
      break

  curses.nocbreak()
  curses.endwin()

if __name__ == "__main__":
  main()

