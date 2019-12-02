# fallDetection353

Group members:
* Sedat Demiriz, sdemiriz
* David Liu, dla68
* Amritpal Singh, aamritpa

Our goal was to come up with a method to identify whether a reading from a person's device could be used to determine whether they have fallen or not, while not seeing any similar action as a fall and falsely activating. This project was inspired by the several stories of Apple Watches and other devices automatically calling emergency services when they detect a falling motion from their users.

## Fall Detection Project CMPT 353:

Detect if an action was an actual fall that would require the calling of emergency services to assist the individual. Data is collected from Linear Acceleration sensors with the device in hand while performing action. We wanted to come up with a way to differentiate between a fall that may require emergency help for the person in question, and common actions that we came up with that feature similar The types of action recorded are:

  1. Fall while moving      - simulate trip and fall on front  
  2. Dropping phone         - dropping phone from waist height (likely on something soft)
  3. Sit                    - sit down on something e.g. bed, couch
  4. Lying down             - lie down on something e.g. bed, couch  
  
A choice was made to hold device in hand for the reason of keeping the recordings consistent and avoiding falling on the device when in pocket to prevent any damage to it. The actions were standardized to simplify the situations but do not necessarily cover all directions of fall or various ways of falling, the main goal was to keep the data consistent.

## Data Collection: 

  a. Each action (one fall, one sit, one lie down, one phone drop) is to be recorded in its own .csv file.  
  b. Begin recording -> Wait 2 seconds -> Perform action -> Wait 5 seconds -> End recording  
  c. Preferably recorded on a single device for consistency in measurement. (Not critical.)

## Data Organization:

Data collected by each group member is located in folders `data-INITIALS`:
* `data-AS`
* `data-DL`
* `data-SD`

The collective data folder `data-all` contains all data from the above three folders.  
Each `.csv` file is labelled `experiment-initials-number.csv` e.g. `drop-sd-01.csv`.

## Noise Filtering

Done by Amritpal Singh - Firstly gathering the data into one file to make plotting and analysis easier. Each of the dimension appended with the same dimension for all files and each activity. After merging data, graphs were plotted. Graphs shows irregular patterns which means data recorded contains the noise which makes the graphs hard to analyze. 

Low pass High Filtering- Noise filtering done for each activity and two different kinds of graph plotted, the ones before noise filtering and the one after noise filtering. Then compare the change in values of linear acceleration in each activities. 

Results:- The phone dropping has the highest change in value of linear acceleration for all dimensions. The walking and falling has second highest change in value of acceleration. While laying down and sitting have very small change as compared to falling and dropping. But the change for laying down was slightly higher than sitting.
Change in Linear Acceleration: Drop>Fall>Laying>Sit

Running Code- The file name data_analysis.ipynb which is in data-AS folder and require the path of files. So to run code change the path of files for each activity and then run code. Before and After Noise filtering graphs will be plotted.   

## Data Trimming and Statistics
Done by David Liu - Processed data by trimming down unnecessary data points by identifying areas of interest. Created a ready to be used CSV files from processed data and calculated attributes of interests to be used in statistical analysis and machine learning classifications. Performed initial ANOVA tests and post hoc analysis to identify candidate attributes for classifiers.

Result: ANOVA tests indicated the various attributes indeed have a difference in means and tests performed will require post hoc analysis. Post hoc analysis revealed that all attributes and actions against falling are candidates for a machine learning classifier.

To trim data, process_data.py must be ran in data-all folder containing all of the raw csv data files. The output of csvs of process_data.py was placed into /data-processed. To run the various statistical tests, stats_data.ipynb be in data-all folder and the various results will be displayed in the juypter notebook.

## Machine Learning-based Classification

Done by Sedat Demiriz - Trained several classifiers with various parameter ranges to identify optimal prediction performance for the collected data. The data used to train the classifiers is the resulting data from the statistical analysis step right before. Classifiers used:

* NB Gaussian Classifier
* Decision Tree Classifier
* N Nearest Neighbors Classifier

Result: Based on the benchmarking performed in Python Code, the NNN Classifier was deemed the best fit for classifying the data, resulting in a 96% correct classification accuracy.

To run, use `./classify.py` or `python3 classify.py` on the command line. This will draw data from the `data-processed` directory, report the highest scoring classifier accuracy on the command line, as well as place benchmarking plot in the 'ml-results' directory comparing all three Classifier methods on a range of parameters. Only methods from libraries used in the course and their exercises were used.

## What could be improved or added?

* Various methods of filtering could be used to see if any other method produced better results.
* A more sophisticated method of statistical analysis could be performed.
* Other methods of classification could be employed, or a neural network could be set up and trained.
