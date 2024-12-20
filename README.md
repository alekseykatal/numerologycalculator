<h1>Project Description</h1>

<p>This project is a Python tool that creates and manages a simple database using SQLite. The program sets up tables for employee information, their earnings, and Social Security minimum amounts. It then fills those tables with data from text files and generates a report to see if an employee's earnings meet the minimum Social Security requirement each year.</p>

<h2>Features</h2>

<ul>
  <li>Creates an "Employee" table to store Employee ID and Name.</li>
  <li>Creates a "Pay" table to store Employee ID, Year, and Earnings.</li>
  <li>Creates a "SocialSecurityMin" table to store the Social Security minimum amount for each year.</li>
  <li>Loads employee data from 'Employee.txt' into the "Employee" table.</li>
  <li>Loads earnings data from 'Pay.txt' into the "Pay" table.</li>
  <li>Loads Social Security minimum data from 'SocialSecurityMinimum.txt' into the "SocialSecurityMin" table.</li>
  <li>Joins the three tables to show employee earnings for a specific year and compares them to the Social Security minimum.</li>
  <li>Generates a report that shows if the employee's earnings meet or exceed the Social Security minimum for each year.</li>
</ul>
