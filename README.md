
CTA Ridership Data Analytics
Author: Ali Shahram Musavi

This program takes the Chicago bus ridership data from api endpoint, loads it to a Postgres table and
visualizes the data using SQL aggregates. The application uses Dash by plotly, it is a python framework
that uses HTML, CSS and React.js to generate the visualizations.

The program helps analyze ridership per routes, and bus stops and route efficiency among everything else.




Dependencies:
  - Dash by Plotly
  - Pandas
  - Plotly
  - json
  - psycopg2




In order to run the program execute the files in the following order:

  --> loader.py
      - Creates a connection to local Postgres Database
      - Creates a table called CTA
      - Gets the data from API endpoint and loads to the db table

  --> app.py  
      - Creates the layout using Dash
      - Runs the program on: http://127.0.0.1:8050/
