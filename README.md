# LLMANY

## Authors
Oskar Kuliński, Kajetan Ożóg, Michał Smorągiewicz

## Description
An open-source app letting you access many LLMs and in the future other AI models in one place. Focused on convenience and simplicity.

## Tech stack
The app is built using electron, with react on the frontend and python powering the backend.

## Technical design

### Design patterns
Design patterns used in the app:
- bridge - joins the react frontend with the python backend
- Model-View-ViewModel - used to create the frontend
- Factory - creates the appropriate request class,
for the requests sent from frontend
- Command - handles all the information about requests sent to backend

### SOLID implementation
SOLID was implemented by dividing the responsibilities between classes, so that no class handless more than one responsibility.