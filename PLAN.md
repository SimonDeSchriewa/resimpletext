# Plan for resimpletext

## What?

A program that serves markdown files to the user. It will be a reader, for now,
but, could become a text editor.

## Why?

To learn to make projects.

## How?

### Abstract Process

- Opens a markdown file.
- Transforms its contents to html.
- Renders the html to the user.

## Analisis

The program will do the following tasks:
- Seek and open files (mainly .md files).
- Transform the .md file to html.
- Render the produced html content to the user.

Components the program needs:
- GUI.
- The file processing component.

## What Architecture?

The initial module layout:

``bash
src/
    gui/
    file_manager/
main.py
``

# Known Unkowns

- How the GUI will work?
- How the file management will work?
- How the GUI and the file management wil work together?
- How to document the code?
- How to document the program?
- How to manage large files?

# Implementation Plan

## Requirements

- Support Linux, Windows.
- Intuitive GUI.
- Support the CommonMark markdown specification.

## Roadmap

- [X] Implement the file_manager.
- [ ] Implement the GUI.
- [ ] Glue the GUI and the file_manager togrther.

## To-Do

- [ ] Set up git for this project with local settings.
- [ ] Implement the GUI (see src/gui/GUI_PLAN.md).
