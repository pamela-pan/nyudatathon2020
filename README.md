### Intro
This project was developed in 36 hours across 3 timezones as a part of the **NYU 2020 Datathon** collaborated between [NYU Center for Data Science](https://cds.nyu.edu/) and [Understood.org](https://www.understood.org/). 

### Challenge partner
Understood is an educational service provider to individuals who have ADHD or learning disabilities, as well as their caregivers, teachers, and parents. The company seeks innovative designs and collaborations to help the population who learn or think differently to explore a variety of intellectual journeys.

<img src='https://github.com/pamela-pan/nyudatathon2020/blob/main/Mission%20of%20Challenge%20Partner.png'>

### Challenge details
Understood was looking for an efficient way to identify non-profit collaborators. They challenged participating teams to build a programmatic solution in 36 hours, details include the following:
- Build an automated tool to create and populate a dataset of companies that have potential to partner with Understood.org.
- Build logic for Understood.org to score how closely each company aligns with their mission statement.

### Team Name: We Will Never Know...
Leaders: Lawrence Liu, Pamela Pan

Members: Xu Han, Ahana Kumar

### Methodology
Our team utilizes the two databases—ProPublica Non-profit database and GuideStar. 
- For ProPublica NonProfit Database, we used its API to grab basic information of an organization, including employer identification number and
- For GuideStar, because we don't have access to its API, so we scraped off the mission statements of organizations. 

### Output
- Code ([link](https://github.com/pamela-pan/nyudatathon2020/blob/main/code.py))
- Variables scraped on sheet 1 & List of potential partners on sheet 2 ([link](https://github.com/pamela-pan/nyudatathon2020/blob/main/Non-profit%20Ecosystem.csv))

### Advantages & Difficulties
The advantages of our project include the ability to directly change parameters in code to get the data of interest, as well as a complete mission statement of each organization. 
Parameters could be anything from an organization's name to location names. 

We have overcome several challenges, including using user_agents to mobilize multiple user addresses in order to prevent MFA from GuideStar. 
Some remaining challenges include 
1. failure to use LinkedIn data despite using user_agents; 
2. failure to use more Organization Variables from ProPublica due to unclear information on the website & limited time to consult customer service.
