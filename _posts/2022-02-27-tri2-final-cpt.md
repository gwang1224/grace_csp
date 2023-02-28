---
title: Trimester 2 College Board Create Performace Task
layout: base
categories: [trimester 2]
description: 
toc: true
---

<!-- <iframe width="560" height="315" src="" frameborder="0" allowfullscreen></iframe> -->

## Program Purpose

### 3.a.i

The purpose of the program is to test the users knowledge on periods and overall women's health and educate people on what they are lacking in their education.

### 3.a.ii

The function of program is that the user will be asked 10 questions about periods and women's health. After they have inputted their answers and submitted, their score out of 10 will be displayed. If the user wishes to log their score, then they can input their name and score into the scoreboard and see other people's scores as well.

### 3.a.iii

In the quiz, the user will input the answers and after they submit, the output will be the score that is generated from how well they did. Additionally, using the database, the user is able to input their name and their score to store in a scoreboard. The output is that their name and score will be printed along with the others in a table.

## Data Abstraction

### 3.b.i

Data stored in a list

<img src="https://cdn.discordapp.com/attachments/1068416415251570689/1079960335592734792/Screenshot_2023-02-27_at_6.56.25_PM.png">

### 3.b.ii

<img src="https://cdn.discordapp.com/attachments/1068416415251570689/1079961153263898724/Screenshot_2023-02-27_at_6.59.59_PM.png">

## Managing Complexity

### 3.b.iii

The name of the list I used is called answers.

### 3.b.iv

The data in the list consists of the answers to the quiz.

### 3.b.v

The data in the list helps manage complexity because it shortens the code by not having to create independent variables for every single questions. After the user has submitted their answer, the user answers can then be checked through iterating through the answers list to check for correct answers rather that checking each individual answer with separate variables.


## Procedural Abstraction

### 3.c.i

Procedure with Parameters

<img src="https://cdn.discordapp.com/attachments/1068416415251570689/1079962881791111168/Screenshot_2023-02-27_at_7.06.51_PM.png">

<img src="https://cdn.discordapp.com/attachments/1068416415251570689/1079965869293174884/Screenshot_2023-02-27_at_7.18.43_PM.png">

### 3.c.ii

<img src="https://cdn.discordapp.com/attachments/1068416415251570689/1079964110520860692/Screenshot_2023-02-27_at_7.11.44_PM.png">

### 3.c.iii

These code segments display the three procedures in this program: create, read, and delete. The Score function takes the inputs name and score and stores the parameters in json formatted dictionary. This data is then fetched separately into the create, read, and delete functions. The read function displays the data onto the scoreboard, allowing users of the website to see everybody's scores. Whereas the create function allows the user to input new data that is then outputted using the read function. THe delete function allows the user to delete all the data when the Score function is called. The create function allows for the user to create an input with their name and score, the read function reads the json formatted data, and the delete function deletes all the data. 

## Algorithmic Implementation

### 3.c.iv

This program uses iteration function as seen when validating the user data. When the user does not input a number for their score, the error message "Please enter a valid score or name" will display. Every time the user clicks the submit button with invalid data, this error message will iterate until the requirement of submitting a number that is between 0 and 10 is achieved. 

The program uses sequencing in the create where the user inputs their name and score. As seen the the _Create function, the program first checks to see if the user's name is greater than 2 letters, then it checks whether the score input is greater than 1. If either of these if false, the program will not compute. Then, the user is added to the database after checking for these errors. 

In the validate function, only inputs that fit in the requirements are allowed to be added to the database. As seen, there is an if else statement. The if statement catches all the "bad" data, which includes scores that are letters, greater than 10, or less than 0. However, if the input passes these checks, the create_user function will be initiated and the user inputs will be added to the backend database.


## Testing

### 3.d.i

First call: The first call is a create and fetch from the _Create and _Read function that is used to save the user name and score data that is inputted by the user. The inputs for name is "Taylor Swift" and score is "9". The data appended to the backend, then displayed on the front end.
Second Call: The second call is a create and fetch from the _Create and _Read function that is used to save the user name and score data that is inputted by the user. The inputs for name is "Harry Styles" and score is "a". The data unable to be appended to the backend and does not show on the frontend.

### 3.d.ii

Condition(s) tested by first call: The first call tests the condition that the name input are letters and that the score input in a number. If this is true, the create_user() function will execute.
Condition(s) tested by second call: The second call tests the validate function to make sure that the score is a number, which it fails.

### 3.d.iii

Results of the first call: The result of the first call that the name and score are inputted into the backend database and shown on the frontend.
Results of the second call: The result of the second call is that the error message will display that tells the user to input a valid name and score.