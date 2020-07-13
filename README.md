# **Production Management** :
This application is for an industry focused on production. The purpose of this application is, simplicity, productivity, and save time by putting everything related to production in one place. The application can be used by all employees. Those who work in production and those who plan production. All employees in production can interact with all the data flow related to production. Can also be used by service technicians if they need to report on machine availability for production. It would need an admin dashboard For further development in the near future, to be able to restrict administratively to a supervisor, service technicians, or manager to be able to administrative application content by adding, delete and update (production, product, machine, and employee).

# **UX** :
This application manages data about the production (product, machine, employee) related to the company and its products. Application is for all employees on that company who want to interact with data related to they were producing. And to help them to get all information about the production.

### **User Stories**:

- As a machine operator, I want to retrieve and record all data related to production in one place. To save time, simplicity, and more productive.
- As a supervisor or manager, I want to plan and add which product to be produced in which machine to be made and in what order priority and which of the machine operator who has done this work. This gives me more control and an overview of all the data flow that applies to any specific product.
- As a service technician, I want to report in the application which machines are available and which ones are under maintenance. So that all employees related to production get this information that others can plan faster and easier for the next production.

Check out the **[Mockup](https://drive.google.com/file/d/1-bhSFyMNAC_GujQ776xhhiUNm53MhdTn/view?usp=sharing?target=_blank)** that I have created as part of the design process and the design of **[database schema MongoDB](https://drive.google.com/file/d/1HhRcZZc9dld6TTAjd23tcvx-GHrFv2cU/view?usp=sharing?target=_blank)**.

# **Existing Features**

There are five general pages (home, add production, products, machines status, employees.) and subpages like edit, add, delete, register. On the home page, products, machines status, employees that present all data about the productions, products, machines, and employees. All other subpages are about to getting or edit and post the data.

# Features Left to Implement

- **Admin Dashboard**: to be able to the administrative application by the person who has the planning role by edit and deletes.
- **Authentication user**: to give verifying the identity of the employee who has to register the production.
- **Search function**: to search for a specific production.

# Technologies Used

- Codeinstitute: materials and homework and projector during the lesson.
- HTML: by using HTML language to markup web pages in this project.
- CSS: to perform style for the WepApp.
- Materializecss: to perform style and responsive for the WepApp.
- Google fonts: to add fonts to the webApp.
- JavaScript and jQuery to perform:
  1. Navbar links.
  2. Mobile Navigation(navbar responsive for the mobile).
  3. Collapsibles accordion: for the production webpage.
  4. Datepicker: To register the production.
- Websites like: ( **Stackoverflow** ,  **css-tricks** ,  **w3schools** ,  **github** ,  **youtube** ).

# Testing

During testing my project with my mentor, we have fix it some issue.

- Select multiple employees in html registering production. Employees could not be displayed after registration.

After the Mentor Guidance Session 2 - Middle of project call. Initially, I got some feedback and I made a little change:
- Add production numbers to the list (All Production) above production name.
- Correct spelling for some text.
- Align products name in products list.
- Remove all production from the first page (Home) and change it so that it would appear as Landing page. And change it in navbar from Add production to Production.
- Remove register production button when production is registered.
- HTML formatted.

# Deployment

I have chosen to deploy my project in Heroku instead of GitHub. Why Heroku? I need a server to handle the request which GitHub Pages cannot support at this moment. Heroku offers a lot of features and flexibility, all for free. Some of the benefits include:

- Easy setup(deployment).
- Good cooperation and communication using Git and heroku.
- Free hosting.

### Deployment On Heroku:

Click New on the top right corner and select &quot;Create new app&quot;. Give the application a name (This will be included in the public URL for the application) and click Create app. Now we open the project in Gitpod. Login to Heroku through terminal. What we are doing here is we&#39;re creating a connection between our Gitpod application and Heroku that would allow us to push our changes using Git to update the application at any given time. Then, we create a new Git repository using git init. And then is add our files to the repository. And then we are going to associate the Heroku application as our master branch, or remote master branch by using those tow commands (1. heroku git:remote -a production-management. 2. git push heroku master). Now we need the requirements text will contain a list of the applications that are required for Heroku to run the application. The Procfile is also needed to get our application live in Heroku. The Procfile is an instruction to Heroku as to which file is used as our entry point at the application, which file we use to call the application to get it up and running. So we have write this command (heroku ps:scale web=1) over to the Heroku app to tell it to get up and running. And the last step is specifying our IP and our port that the server instance on Heroku will know how to run our Flask application to do that in Heroku home page, we&#39;re going to go to settings \&gt; click on Reveal Config Vars and on the input field Key we should write IP and in input field Value write the IP address which is in my case(0.0.0.0) and do the same with port:5000 in my case. And click on the top right corner &quot;Open app&quot; and the application should be live.