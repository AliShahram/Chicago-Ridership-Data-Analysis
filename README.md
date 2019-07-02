
# CTA Ridership Data Analysis
Author: Ali Shahram Musavi

This program takes the Chicago bus ridership data from api endpoint, loads it to a Postgres table and
visualizes the data using SQL aggregates. The application uses Dash by plotly, it is a python framework
that uses HTML, CSS and React.js to generate the visualizations.

The program helps analyze ridership per routes, and bus stops and route efficiency among everything else.




## Dependencies:
  - Dash by Plotly
  - Pandas
  - Plotly
  - json
  - psycopg2




## In order to run the program execute the files in the following order:

  *  loader.py
      - Creates a connection to local Postgres Database
      - Creates a table called CTA
      - Gets the data from API endpoint and loads to the db table

  * app.py  
      - Creates the layout using Dash
      - Runs the program on: http://127.0.0.1:8050/

<img width="982" alt="Screen Shot 2019-07-02 at 3 40 59 PM" src="https://user-images.githubusercontent.com/25894620/60542350-ba60ee00-9ce1-11e9-81d3-2a7646a42f4b.png">

<img width="950" alt="Screen Shot 2019-07-02 at 3 41 08 PM" src="https://user-images.githubusercontent.com/25894620/60542369-c5b41980-9ce1-11e9-8c96-a00b6e6dc6e7.png">

<img width="1229" alt="Screen Shot 2019-07-02 at 3 41 35 PM" src="https://user-images.githubusercontent.com/25894620/60542381-cc429100-9ce1-11e9-964b-66cc48560241.png">

<img width="1238" alt="Screen Shot 2019-07-02 at 3 42 06 PM" src="https://user-images.githubusercontent.com/25894620/60542388-d19fdb80-9ce1-11e9-8069-14a7d94b34dd.png">
