# GUI Plan

# What it should do?

- Let the user select the file to be open, at any given time.
- Show the user the contents of the file.
- Be thought to later implement text editing.

## Analisis

The GUI has two functions, select a file to open and show the content of the 
file, it has to be flexible enough to later add editing features.

Therefore it needs the following widgets:
- A menu and/or popup widget to seek and select a file.
- A widget capable of rendering html to show the content (view).
- A widget to show the content in plain text (raw).
- A widget to switch between view, raw and both.

# Widget Layout 

---------------------------------------------------------------------
| |open|            |switcher|                                      |
---------------------------------------------------------------------
| ----------------------------------------------------------------- |
| |                                                               | |
| |                                                               | |
| |                                                               | |
| |                                                               | |
| |                                                               | |
| |                                                               | |
| |            raw/view of the file                               | |
| |                                                               | |
| |                                                               | |
| |                                                               | |
| |                                                               | |
| |                                                               | |
| |                                                               | |
| |                                                               | |
| |                                                               | |
| ----------------------------------------------------------------- |
---------------------------------------------------------------------

---------------------------------------------------------------------
| |open|            |switcher|                                      |
---------------------------------------------------------------------
| ----------------------------------------------------------------- |
| |                              |                                | |
| |                              |                                | |
| |                              |                                | |
| |                              |                                | |
| |                              |                                | |
| |                              |                                | |
| |       Raw text               |     View text                  | |
| |                              |                                | |
| |                              |                                | |
| |                              |                                | |
| |                              |                                | |
| |                              |                                | |
| |                              |                                | |
| |                              |                                | |
| |                              |                                | |
| ----------------------------------------------------------------- |
---------------------------------------------------------------------


# Inicial Module Layout

```bash
src/gui/
        gui.py              Where everything will merge
        widget_layout.py    The widget layout
        event_handler.py    The event bindings
        [themes.py]         Maybe a theme system
```

# Module Layout v2

```bash
src/gui/
        gui.py              Where everything will merge
        [themes.py]         Maybe a theme system
```

# Roadmap

- [ ] Implement the gui.

# To-Do

- [ ] Change raw from being an Entry to be somthing that hold more tha one \
      line.
- [ ] Add the file opening widget.
- [ ] Manage the layouts better.
- [ ] Glue the GUI and the file_manager togrther.
