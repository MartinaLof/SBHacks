# SBHacks

# OptiClass

OptiCourse is a course scheduler for university students that allows them to minimize their time on campus based on a set of mandatory and elective courses.

## Problem/Audience

A recurring issue for most university students is that they waste time defining their schedules at the beginning of a quarter or semester. Most students want to minimize break times between classes to enjoy their free time, extracurricular activities and organize extended study periods. According to FileMaker's survey on the nation's college students, 88 percent of college students want to improve their ability to manage their time. There is the need to automate the scheduling process of classes and minimize break times for students to focus on the right things as soon as possible.

Source: https://www.reliableplant.com/Read/3429/college-students-struggle-with-organizational-skills

## Experience
A user lands on the home page and searches for the classes required for the semester or quarter. Then he will select classes that he must complete in the current quarter and elective ones that he wants to take.
By clicking on the organize bottom, the page will lead the user to a scheduling dashboard showing required and elective classes sorted by the least amount of break time during a day for a week. The user can block time for extracurricular activities in the "Extra Activities" section. The user can then drag the bottom to indicate the time where it wants the schedule to minimize for break times during the week based on the extracurricular activities, required and elective courses. Once the user sees the desired schedule, he or she can select it and a print-out version will be available.

# Technical

## Instructions for the Schedule Builder

Goal: Convert viable schedules into a matrix that the user has freedom to modify and optimize an academic schedule.

1. Go to the final cell of the iPython file:
    1a. Input list of mandatory classes needed
    1b. Input list of possible electives (as many as you want)
    1c. Input the maximum number of classes you want for that semester

2. Output a matrix scheme (168, 5) for timings with each built on 5 minute intervals of an optimal schedule times and what sections to get. Each column represents a time from 8 a.m. to 10 p.m. broken up into 5 minute intervals.

3. Use your entire set of schedule timings to try and manage preferences and blocks in schedule however you want. You can modify the matrix and/or narrow down the "full schedules listing" in according to a given person's preference.

4. Output a matrix that to be matched to the available scheduled blocks (represented by ones in the matrix) to find which courses and sections to open. For the read me and how to use schedule builder.

## Models

<li>User</li>

## Views

<li>Course Search</li>
<li>Course Scheduling Dashboard</li>
<li>Final Schedule</li>

## Routes

Course Search (Home)

<li>GET</li>
<li>POST</li>

Course Scheduling Dashboard

<li>GET</li>
<li>POST</li>

Final schedule

<li>GET</li>
<li>POST</li>

## Other

- Languages: HTML, CSS, TypeScript, Python
- Technologies: Angular, Overleaf, Software for Convex Optimization
- Color: #364599

## SBHacks Milestones
- Course Database (Json)
- Break time minimization algorithm (Python)
- Course scheduling recommendation algorithm (Python)
- Course Scheduling Dashboard (Angular)

## SBHacks Competing Challenges
- Grand Prize
- SB Hacks - Best Hack for College Students
- LogMeIn - Best Use of Machine Learning

## Demo Photos
