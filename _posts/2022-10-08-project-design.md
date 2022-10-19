---
toc: true
layout: post
categories: [trimester 1]
title: Project Design
---

## Program Purpose and Function

Purpose: To create a language translator
**Input:** Artist Name and Album
**Output:** Album duration, album song names, number of songs, album cover photo
The purpose of this program is to provide users with data about their favorite artists including their albums, songs, and album duration and allow them to choose their favorite artists.

## Roles:

Grace: Dev-Ops
Amitha: Frontend
Claire: Backend
Tanisha: Backend

## Managing Complexity

Use a function to read user input and only provide wanted album information allowing user to use favorites tab to organize the artists they enjoy

## Procedural Abstraction
using artist[album], retrieve only wanted data from the dictionary. call developed function to run based on user input.

## Algorithm Implementation
Develop algorithm to count number of songs in album given API data
Algorithm to create 'favorite artists' tab, where users can select their favorite artists to be saved in a seperate section of the application

## Testing
Input multiple artists and album. See if each selected data type displays proper data. Add artists to 'favorites' and see if that data is stored

## API

Using API: [Translator](/repository_1/_notebooks/2022-10-7-API.ipynb)
Using API: [API for Music](/repository_1/_notebooks/2022-10-7-API.ipynb)

![]({{ site.baseurl }}/images/screen1.png "Input what artist/band user would like to know about")
![]({{ site.baseurl }}/images/screen2.png "Shows selected band with thumbnail")
![]({{ site.baseurl }}/images/screen3.png "Shows information about artist/band")
![]({{ site.baseurl }}/images/screen4.png "Hows user's favorite artists/bands")