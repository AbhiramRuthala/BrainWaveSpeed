#A simple way to understand EEG data. Input your frequency and wavelength in terms of set numbers. You might have to convert them to meet the unit specifics. 
#I'll update this with a feature to do conversions if your brain wave data doesn't meet the unit specifics. 
#The reason we need those units is so that the answer is in meters/second.
frequencyinput = float(input("Write your frequency levels (The number of waves occuring in a duration of time) in 1/s: "))
wavelengthinput = float(input("Write your wavelength (distance between peak to peak of the wave) in meters: "))

#Use the nu = c/lambda formula but apply that to brain waves.
wavespeed = wavelengthinput * frequencyinput

#Print the result using string concatenation.
print("The speed of your brain wave is: " + str(wavespeed) + " m/s")

#A relatively objective look on brainwave speed. This'll help us classify waves not only in terms of frequency but also in speed, allowing us to get a comprehensive view of what such brain waves do at different parts of the frequency range.
#Speed can be identified through frequency, but this provides a more holistic approach.
