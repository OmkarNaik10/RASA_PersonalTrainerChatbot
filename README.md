# RASA_Sumbission
# version: "3.1"
# This ChatBot Help you Stay Fit with proper nutrition and workout plan


Done API calls that give your Maintenance calories TDEE  based on your lifestyle.

Done Database Connection That stores your Goals such as PR and Workout.

Done Slack Deployment.

# Demo: https://www.youtube.com/watch?v=hgAHhL085mE&t=1s

Conversational Flow:

# Step1:
  - intent: greet

    - hey
    - hello
    - hi
    - hello there
    - good morning
    - good evening
    - moin
    - hey there
    - let's go
    - hey dude
    - goodmorning
    - goodevening
    - good afternoon



# Step2:
  - intent: mood_great

    - perfect
    - great
    - amazing
    - feeling like a king
    - wonderful
    - I am feeling very good
    - I am great
    - I am amazing
    - I am going to save the world
    - super stoked
    - extremely good
    - so so perfect
    - so good
    - so perfect

# Step3:
  - intent: todays_schedule

    - I want my todays schedule
    - give me my todays schedule
    - whats my schedule
    - todays plan
    - todays schedule

# Step4:
  - intent: HW_remaining

    - My HW and study plan?
    - what is my HW?
    - Assignment?
    - Homework?
    - Study Plan?


# Step5:
  - intent: togym

    - I am planning to go for gym workout
    - gym workout
    - going for gym workout
    - go to gym for workout
    - going to hit gym today

# Step6:
  - intent: name_workout
    - I am planning to do chest
    - I am planning to do triceps
    - planning to do traps
    - to do triceps
    - work on lowback
    - to do legs
    - planning to do back
    - planning to do hamstring
    - planning to do shoulder
    - planning to do pull
    - planning to do push


# Step7:
  - intent: workout_schedule

    - Give me my workout schedule
    - my workout schedule
    - what is my workout schedule
    - workout schedule
    - How is my workout schedule  

# Step8:
  - intent: biceps_workout

    - bicep-workout plan
    - bicep-variation
    - bicep-exercise
    - bicep-variation
    - bicep-workout plan
  
  # Step9:
  - intent: triceps_workout

    - tricep-workout
    - tricep-exercises
    - what tricep-exercise I am training?
    - tricep-variation
    - tricep-workout
 
 # Step10:
  - intent: chest_workout

    - chest-workout
    - chest-exercises
    - what chest-exercise I am training?
    - chest-variation
    - chest-workout
 
 # Step11:
  - intent: back_workout

    - back-workout plan?
    - back-variation
    - what are back-exercises
    - back-variation
    - back-workout plan
 
 # Step12:
  - intent: shoulder_workout

    - shoulder-workout plan?
    - shoulder-variation
    - what are shoulder-exercises
    - shoulder-variation
    - shoulder-workout plan
  
  # Step13:
  - intent: legs_workout

    - legs-workout plan?
    - legs-variation
    - what are legs-exercises
    - legs-variation
    - legs-workout plan
 
 # Step14:
  - intent: info_population

    - I want the state population
    - what is the state population
    - want the state population
    - state population

# Step15:
  - intent: name_location

    - California
    - Alabama
    - Georgia
    - Minnesota
    - New York

# Step16:
  - intent: info_uni

    - I want some names of university
    - names of university
    - want some names of university
    - some names of university

# Step17:
  - intent: uni_name

    - United States
    - USA
    - US
    - IN
    - India

# Step18:
  - intent: want_bmi

    - I want my bmi
    - want my bmi
    - give me my bmi
    - result of my bmi
    - how do I get my bmi
  
  # Step19:
  - intent: bmigetheight_input

    - my height in meter is 1.75
    - my height is 1.85
    - height is 1.8
    - so my height is 1.77
    - 1.75
    - 1.73

# Step20:
  - intent: weight_input

    - my weight in kg is 60
    - my weight is 62
    - weight is 65
    - so my weight is 64
    - 60
    - 62

# Step21:
  - intent: bmiresult

    - do you think I am fit
    - do I look fit
    - I am fit
    - say something related to my fitness 

 # Step22:
  - intent: dietplan

    - give me my diet plan
    - my diet plan
    - diet plan
    - whats my diet plan
 
# Step23:
  - intent: givecaloriesfood

    - I want total calories of food
    - total calories of food
    - calories of food
    - calories of food

 # Step24:
  - intent: enterfoodname

    - 1 large mango
    - 1 large apple
    - 1 large banana
    - 1 large tomatoes 

# Step25:
  - intent: request_detail

    - I want to fill my todays workout detail
    - fill my todays workout detail
    - I want to track my todays workout details
    - my todays workout detail

# Step26:
  - intent: pushpulllegs

    - my exercise todays pushworkout
    - my exercise todays pullworkout
    - my exercise todays legsworkout
    - todays exercise pushworkout
    - todays exercise pullworkout
    - todays exercise legsworkout

# Step27:
  - intent: workoutdescription

    - exercise heavyweight
    - exercise lightweight
    - exercise bodyweight
    - exercise resistance

# Step28:
  - intent: storedatabase

    - yes I want to store my information
    - yes store my current information
    - yes store info
    - yes dump the info



Story2:

  - intent: greet_omi

    - Hey omi ssup
    - Hello omi how are you?
    - Hey omi how you feeling?
    - ssup omi


  - intent: omi_reply

    - Hows the josh omi
    - Hows the power
    - Hows life
    - Hows the josh


  - intent: mood_unhappy

    - my day was horrible
    - I am sad
    - I don't feel very well
    - I am disappointed
    - super sad
    - I'm so sad
    - sad
    - very sad
    - unhappy
    - not good
    - not very good
    - extremly sad
    - so saad
    - so sad



