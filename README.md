# A Personalized Recommender System in E-learning
Diploma Thesis project conducted during my studies at the Computer Engineering & Informatics Department in Patras, Greece (2022).

# Description
- In this project, a learning material recommendation system is designed/implemented, using Artificial Intelligence, so that the user can easily locate the resources for a specific learning subject.
- Sources are obtained through suggestions of other users with similar characteristics, who are academically/demographically matched to the user making the search.

# System Architecture 
- The architecture of the proposed system consists of a Database in which all data are recorded: users (teachers – learners – administrator), courses, recommendations, educational materials, and statistics (user rating for the material and average user rating). 
- The front-end part consists of the HTML pages, the JavaScript-jQuery code as well as the CSS styles, while the back-end part consists of the Flask in Python language that sends the results in JSON format to the front-end part of the application.
- In order to run this application, you must first connect to the MySQL server and the Apache Web Server of the XAMPP program. This way we can connect to our Database.
- To connect to the local server, the Anaconda environment can be used, specifically Anaconda's Spyder (Python code development environment).
- In Spyder, we run the server in Flask, which runs at 127.0.0.1:5000.
