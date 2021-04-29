# Project Milestones and Schedule (1-2 pages)
* Define milestones that clearly define their objective, what it means to complete each milestone, who is responsible, and when you expect to complete them. 
* Define the milestones at two scales, a high level set of key milestones aka deliverables, and a low level set of weekly milestones that move you towards deliverables.
* You must be able to demonstrate the completion of each deliverable. For example, take a video of something working, make a graph showing some processed data, or complete a documented github repos. 
* Prioritize and organize your milestones. Some are necessary, others are useful, some are hopeful if time permits, etc. Gantt charts are helpful to better visualize the milestones and understand their dependencies.
* Describe your minimal viable product. This should be something that you will achieve with very high probability. It demonstrates the basic functionality and idea and enables feedback. Aim to get an MVP as soon as possible. Then iterate quickly on top of that adding more features as you have time.
* A good rule of thumb is one milestone per person per week. And one deliverable per person every 2-3 weeks. The general expectation for UCSD classes is 8 hours/week of work outside of lecture. Think about breaking milestones into 8-10 hours of work. Be realistic at the same time, make sure you are driving towards a deliverable. 

![Gantt Chart](Gantt_Chart.png)

### Milestones
[Gantt Chart](https://docs.google.com/spreadsheets/d/1hELHBSfVzhgVlQ-FRjqm1UXFKXBpGtuc2WCGuSOQzQU/edit?usp=sharing)

* Connect hardware together
  * Raspberry Pi home screen is visible on the touchscreen - Jasmine + Mihai
  * Can see what’s on the camera on the touchscreen - Jasmine + Mihai
* Barcodes
  * Camera can identify barcode - Steven
  * Camera can read barcode - Steven
  * Program can search through barcode database - Steven + Yilin
  * Program can categorize and print out correct category based on barcode - Steven + Yilin
UI/UX
  * Set up basic github site (milestone) - Julia
We’ll know this component is complete when we have a Github page that we can access with a url similar to “http://smartwaste.github.io/” that has “hello world” printed on the front page
  * Design interface of app (milestone) - Julia + Yilin
We’ll know this part is complete when we have a figma design of our interface, complete with all the components we’d like to have (buttons, pop ups, waste classification)
  * Implement basic interface (deliverable) - Julia + Jasmine
We’ll know this part is complete when we have correct classification of our waste displayed on screen (or at a minimum the classification given by the model, even if it still needs tuning) as well as buttons for pop ups of additional information.
    * Includes displaying correct categories - Jasmine
    * Buttons for info / pop up modals connected to buttons + exits - Julia + Yilin
  * Connecting camera feed (milestone + deliverable) - Julia + Jasmine
We’ll know this part is complete when the image captured by the camera is displayed on the website.
  * Testing (milestone) - Jasmine + Yilin
We’ll know this part is complete when all of our tests have been run successfully.
  * Map (deliverable, tentative) - Julia + Yilin
We’ll know this part is complete when there is a feature to see special waste sites on our website.
* Object classification using machine learning
  * Run the classifier on the Raspberry Pi. - Mihai 
  * Make the classifier run the predictions using data from the Raspberry Pi Camera. - Mihai 
  * Decide upon model architecture - Mihai + Steven
  * Implement an object classification model - Mihai + Steven
    * Common items
      * Paper
      * Water bottle
      * Can
      * Glass bottle
    * Some specialty recyclables
      * Pencil/pen
      * Contact lens case
      * Batteries 
    * Some organic waste
      * Newspaper
      * Banana peel
  * Implement a waste classification model to detect the following classes.  : Glass, Paper, Cardboard, Plastic, Metal, Trash. - Mihai + Steven
  * Test our models performance and accuracy. 
