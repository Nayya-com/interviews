# Test Options

This test repo has a server which can be spun up and tunneled with ngrok. The server provides a simple endpoint for guessing a number. The server can be started with the following command.

```
cd backend
npm i
npm run start -- 100
```

The argument after `run start` is for the max number in the guess range, it defaults to 100 and the min number is 0. For some further complexity we could customize this more to allow negative numbers, and custom ranges that do not start at 0.

The endpoint `/guess` is expecting a `POST` with `JSON` that looks like this

```
{
    "guess": 15
}
```

Upon receiving a guess the endpoint will respond with a message indicating the guess was too low, too high, invalid, or correct. Upon receiving a correct guess, the server generates a new number within the range and can continue to be worked with.

For debugging & interviewer help the server will log the guess and correct number in the terminal each time a guess is made.

The server is rate limited to 10 guesses every 10 seconds. This will return a `429` with a message, and can be customized easily by peeping the code.

# React Testing

This is a step by step test for working with react. You are working with the candidate on this problem, when they get stuck try to lightly guide them without giving away too much.

We aren't necessarily expecting anyone to finish all of these steps. Keep note of what steps they made it to, and if you needed to help them on some. If you are running out of time, you can discuss some of the additional steps and get an idea how they'd approach them.

I didn't write any styling steps in here, but I think it would be good to stop them when they've maybe 10 minutes left and talk some about styling. They could do this in CSS or styled components. I would ask them to style the form vertically with some spacing.

```
label
input
button
```

If they made it to the guess counter, guess tracker, and/or scoreboard have them do some layout with those. Maybe guess tracker to the right of the form, and make sure it collapses appropriately to single column for mobile. Here is a simple layout sketch
![Untitled-2023-12-20-1027](https://github.com/Nayya-com/interviews/assets/1495051/8f1a52c7-a48b-4e71-9f64-816a6c544491)


1. Using the server instructions above, spinup the server locally, and get your tunnel link with ngrok.
2. Setup a new coderpad session using [this question](https://app.coderpad.io/dashboard/questions/all/276638).
3. Explain to the candidate that we will be building a react app with typescript & styled components (if they know these it's great, if not it's fine for them to use vanilla JS and CSS or whatever they are comfortable with). The purpose of the app is to let the user guess a number, get feedback, refine their guess, and ultimately figure out the correct number.
4. First things first, ask the candidate to build out the form for this.
5. Paste in your ngrok URL and comment it out, have them wire up the form to send the guess (don't forget, the endpoint is /guess). Wait for this to be working before moving on.
6. Have them display the feedback about their guess to the user.
7. Have them make & display a guess counter.
8. Have them store previous guesses and display them to the user.
9. Have the previous guesses also display the feedback (this could be done with the message, colors indicating higher or lower, or whatever solution they feel like this is a good time to let them make and execute a decision).
10. Have them create a scoreboard that shows the number of guesses it took to successfully answer (you may need to restart the server with a super small range to test this).
11. Have them validate only numbers in the input.
12. Have them make it so the user can't submit numbers that were already guessed.
13. Have them make it so the user can't submit numbers that should be disqualified (if a user guessed 5, and was told it's too low, 0-5 should be disqualified).

## Bonus or things to discuss after

Remember, this is rate limited. Have them break the rate limit, and then have them come up with a solution for the user. If there is time, they can code this, or you can just discuss.

# General Coding Test

This test can be done in whatever language they are comfortable with. Basically they will be writing code to guess the number, you'll want to spin the server up with a higher range maybe 1000 or 10k. You may want to fuss with the rate limiting some throughout the test.

This test is a bit more choose your own adventure than the react version. We are looking for problem solving skills as well as technical know how to implement them. The rate limiting gives a clear message back to the user, so once they encounter this, they can figure out how they want to tackle it.

1. Using the server instructions above, spinup the server locally, and get your tunnel link with ngrok.
2. Start up a coder pad session with whatever language they want to use.
3. Explain that we'll be writing some code to guess a number.
4. Paste in the ngrok URL (don't forget the endpoint is /guess)
5. They can start by just submitting a guess to the endpoint.
6. From here we can start asking the user to automate this given the feedback from the endpoint.
