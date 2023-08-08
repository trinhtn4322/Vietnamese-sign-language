# Subject: Vietnamese sign language
**This is a class assignment**
This project consists of 3 main parts:
+ Learn about sign languages to prepare for data generation
+ Create data
+ Build recognition model

**Idea:** Each sign will be a sequence of actions of the body, so a neural network will be used for analysis. Instead of analyzing a long video, it will split into a set of contiguous frameworks for processing.

### Part 1: Vietnamese sign language
This project will use 3 simulated signs for 3 movements: hello, thank you, sorry. (cre: https://www.youtube.com/watch?v=YSPRe4TeTxw&t=2s)

### Part 2: Creating data
To be able to capture hand and face movements, we will use the mediapipe framework.
This is a famous framework that supports many human gestures
This data is created by an amateur (me) so it is inevitable that errors in hand and facial movements will be inevitable.
Data after being collected will be in numeric form corresponding to the coordinate points of the hand and face. Then it will be saved to a CSV file. 

After the data is brought to csv, it will go through a few processing steps with Jupyter Notebook.

### Part 3: Build model
The model used here is the RNN model, the reason for using this model is because its regression characteristics can help us analyze consecutive frames, thereby increasing the accuracy of the model.



Project referenced from the video: https://www.youtube.com/watch?v=_52-kz08LvU&t=2317s
