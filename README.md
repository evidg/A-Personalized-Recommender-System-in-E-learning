# A Personalized Recommender System in E-learning
Diploma Thesis project conducted during my studies at the Computer Engineering & Informatics Department in Patras, Greece (2022).

# Description
In this project, a cooperation framework is proposed for the possibility of appropriate sharing of educational material using artificial intelligence so that the learners receive the best suggestions for them. More specifically, a system of educational material recommendations is defined, designed, and implemented so that the user can easily locate the resources required for learning in a specific subject. Sources are obtained through recommendations from other users with similar characteristics, where they match the searcher academically and demographically. This system puts order in the chaos of educational material that one can search for through the internet. Still, at the same time, it adapts to the abilities and educational needs of the user himself, who has the possibility to receive recommendations calibrated on the basis of his own profile and categorized to the corresponding item, working in a smarter way than searching based on keywords or suggestions based on the number of people viewing an item.

# System Architecture 
- The architecture of the proposed system consists of a Database in which all data are recorded: users (teachers – learners – administrator), courses, recommendations, educational materials, and statistics (user rating for the material and average user rating). 
- The front-end part consists of the HTML pages, the JavaScript code as well as the CSS styles, while the back-end part consists of the Flask in Python language that sends the results in JSON format to the front-end part of the application.
- In order to run this application, you must first connect to the MySQL server and the Apache Web Server of the XAMPP program. This way we can connect to our Database.
- To connect to the local server, the Anaconda environment can be used, specifically Anaconda's Spyder (Python code development environment).
- In Spyder, we run the server in Flask, which runs at 127.0.0.1:5000.
