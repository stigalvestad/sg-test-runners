# Make list of test runners
Made for orienteering race Sørlandsgaloppen. We use test runners to run through courses, to ensure everything is OK 
before the competition begins.

Finding test runners to run different courses can be tedious to do manually, 
given you need to take into account what they can do and when they can participate.

## Intent
Given a input-csv which contains test runners and which difficulty and course they can maximum run, produce a list
of test runners for each day which satisfies those constraints.

## Prerequisites
Use input-template.csv and make input.csv containing all runners and their info. 

* Navn: name of the test-runner
* Klubb
* Tlf
* E-post
* Torsdag: add "x" if runner can run this day
* Fredag: add "x" if runner can run this day
* Lørdag: add "x" if runner can run this day
* Søndag: add "x" if runner can run this day
* Kommentar: any comment
* MaxCourse: Courses 1-21 expected. 1 is longest, then decreasing length and difficulty going towards 21.	
* MaxDifficulty: A, B, C or N. Standard difficulties in Norwegian orienteering.
* Sorting: To resolve runners who are both qualified for same course, look at sorting. Lower number means the runner
* is preferred over a runner with higher number.

## Using it
Make sure input.csv contains all runners. 
Then execute script, it will print who can run the courses each day and which courses are MISSING runners. 
