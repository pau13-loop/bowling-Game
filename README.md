# Bowling Game Kata

> In this repository you'll find the **Christamas Kata** about a the score of a Bowling Game. This project has been designed for the Web _Development students_ of the first year. The goal of this Christmas project is improve the skills working with the OOP (Object-Oriented Programing) paradigm and feel comfort working with classes on Python.

## Table of Contents

1. [Motivation](#motivation)
1. [Used Technologies](#used-technologies)
1. [Content](#Content)
1. [Reflections](#reflections)
1. [Retrospective](#retrospective)
1. [License](#license)

---

## Motivation

One of the biggest motivations for this kata is that has been the most difficult if we compare it to the others. This one has been the hard challenge but the funniest one becuase everyone played bowling once in their life but none know the propper rules of the game. First of all we had to know how works the score card just to start to try to solve the kata. Really enjoyable, even more if you have watched the movie of KingPing.

---

**[⬆ back to top](#table-of-contents)**

## Used Technologies

- Python
- Pytest
- MarkDown
- Github

---

**[⬆ back to top](#table-of-contents)**

## Content

> The content of this project it's separed into two different directories **Domain** and **Resources**.

### Domain

In this direcotry we will find that it's subdivided into another two, **src** and **test**.

- **src**

Inside _src_ we have the main program functional and completely operative to any game that could happen at bowling.

---

- **test**

Inside _test_ we have all the test cases that we have built to check the functionality of the program and if it runs correctly following the rules of the score of the bowling games and we added a few more test cases trying to break or find a bug in our program but it didn't happened.

### Original Program

In this directory we have a copy of our original program that was built without a class method and all of it inside the same function, we didn't followed the OOP(Object-Oriented Programing) paradigm at the beggining of our program, we have the original test cases, this ones still been the same ones but with a few small modifications to be able to execute Pytest and work with a class method on Python.

### Resources

The directory of _resources_ how it tells the name has been built to keep all the external resources to the bowling program, in it we will find:

---

###### Explained Bowling Program

In this document we will find an explanation of all our program, explained line by line and block by block with tha aim of the comprehension of the users that will visit our repository trying ot find a challenge to theirselves. How is our first program, we will find it built in just one function and without a class method but it won't supose any problem because when it has been modified to be able to work with a class method and to follow the OOP paradigm you should know that it keep the same structure then it will be easy to understand hoe it works for you.

---

**[⬆ back to top](#table-of-contents)**

## Reflections

It has been a really interesting kata and really enjoyable. Between the Christmass Projects i had i will choose this one straight away even knowing that it left me a few days musing how i could solve it. The first good point of this kata is that finally i learn how it works the score card of bowling. And the best thing is that now i trust myself more when it comes the moment of work with classes with Python. I got to know how the OOP (Object-Oriented Programing) paradigm it works and i had so many problems during this kata that i didn't know how to solve at the beggining but thanks to the deep research i could get over them and know how to react against this kinds of issues that i'll find in the future. An awesome kata, perfect to recmoend to the people that just has started to learno how to work with the OOP (Object-Oriented Programing) paradigm and loves the challenges.

---

**[⬆ back to top](#table-of-contents)**

## Retrospective

###### Did you do any design before you started coding ? If so, does your code have this design now ?

Yes i wrote my test cases and after that i wrote a design of the program that i should make to pass the test cases. The design was of the whole program and i should say that i've done this design without follow the OOP, this means that the original design wad all conformed with a single function that operate for all the test cases. Is true that after finished the program i adapted to the OOP paradigm and i should say that even knowing that the program hass been descomposed and refactorized still keeping the essence of the original design, of course is not looking the same but it's really close of what i thought i want to do.

---

###### At what point did you realize you can't simply loop over frames, that you inf act need to refer to the previous frame as well as the current one in order to calculate the score ? In an ideal world, when should you have realized this ?

I realized this one time i start to code my program, this issue stop my development because i couldn't find a way to check the frames after a strike and how to add the extra point to the score with a boolean. After two nights wondering about how i could do it, i decide to change the _for loop_ for a _while loop_ and get rid of the boolean and by this way i was able to know with wich frame i'm working on and i was able too to check for the frames that were previous or posteriors to the strike and add the extra punctuation to the score without to deal with adversities.

---

###### Look at the code you have ended up with, and compare it with the above desription of the rules of bowling. Is there any similarity in the words used in each ?

Yes, beacuse while i was developing the program i try to called the variables of the program and to name the functions with the bowling vocabulary to make easier the comprehension of the program to users that alredy know how a bowling game work and know how the score card works. If you have played bowling before or even just once in your life you'll be familiarized with the vocabulary.

---

###### Did you do enough refactoring ? How would you know ?

I'm never too sure if i did enough refacotring in my programs but i know it has been well refactorized when the length of the program gets reduced and keep his easy comprehension. When i can't find any code smells in my program. And when i can't find any one of the mistakes that i have to check from my checklist

---

###### How did you decide wich tests to write and in wich order ? Did it matter what order you implemented them in ?

Always i try to start with the easuest test when i know taht the programs pass the test cases i just increase the complexity of the test cases, Always i try to follow the sequence that the instructions of the program that i have to read tells me. For example in case of the bowling game program i never will start with the spares if before i didn't wrote a code that check for the integres and add them to the score, how i could know how many pings i dropped down with the spare if i can't check the throw before ? I just an example to understand how i have worked with the test cases of this program. And i thinks it matters a lot in wich order you choose to implement the test cases. I think it will make a strong influence over your program, on how much time you spent to get the expected result and about how many bugs you have typed on your program. I think that the order that you choose to implement the test cases helps the development of your program and majes you a better programmer in most of the cases.

---

**[⬆ back to top](#table-of-contents)**

## License

MIT License

Copyright (c) 2020 AntoniPizarro and Pau Llinàs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

**[⬆ back to top](#table-of-contents)**
