# fallDetection353

Group members:
* Sedat Demiriz, sdemiriz
* David Liu, dla68
* Amritpal Singh, aamritpa

## Fall Detection Project CMPT 353:

Detect if action was an actual fall that would need for help. Data is collected from g-Force and Linear Acceleration sensors with the device in hand while performing action. We wanted to come up with a way to differentiate between a fall that may require emergency help for the person in question, and common actions that we came up with that feature simmilar The types of action recorded are:

  1. Fall while moving      - simulate trip and fall on front
  2. Fall from standstill   - simulate faint and fall on front
  3. Sit                    - sit down on something e.g. bed, couch
  4. Lying down             - lie down on something e.g. bed, couch
  5. Dropping phone         - dropping phone from waist height (preferably on something soft)
  
A choice was made to hold device in hand for the reason of keeping the recordings consistent and avoiding falling on the device when in pocket to prevent any damage to it. The actions were standardized to simplify the situations but do not necessarily cover all directions of fall or various ways of falling, the goal was to keep the data consistent.

## Data Collection: 

  a. Each action(one fall, one sit, one lie down, one phone drop) is to be recorded in its own .csv file.  
  b. Begin recording -> Wait 2 seconds -> Perform action -> Wait 5 seconds -> End recording  
  c. Preferably recorded on a single device for consistency in measurement. (Not critical.)
