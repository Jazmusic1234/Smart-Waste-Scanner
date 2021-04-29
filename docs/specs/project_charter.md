# Project Charter (4-5 pages)

### High Level Description

Our project is an interactive teaching tool that uses machine learning and computer vision to detect and classify different types of waste and tell the user where to dispose of them. It will consist of a Raspberry Pi, camera, and tablet.

*****************
### Project Overview (1/2 page)
###### *Summarize the project in layperson’s terms (e.g., one that a non-engineer could understand). This should not be more than one paragraph.*

The Smart Waste Scanner will have a Raspberry Pi, camera, and a touchscreen. The user will be able to hold up an item to the camera and it will figure out what that item is and whether it should go in the recycling, compost, specialty recycling, or trash and display the correct category on the touchscreen. On the screen, there will also be buttons that the user can click on to learn more information. For example, if the user doesn’t know what composting is they can click on the “What is composting?” button. If they want to learn about how much waste is recycled every year, they can click on the “Recycling Stats” button. There will also be a map on the screen that shows the nearest location that the item can be disposed of. If it’s compost, it will show a map of the community gardens on campus that accept compost. If it’s specialty recycling, the map will show the location of the Sustainability Resource Center.


*****************
### Project Approach (1-2 pages)
###### *Provide more details about what you will accomplish and how you plan to accomplish it.*

There are so many different types of waste which makes it possible for this project to be built upon in the future. But due to the fact that we only have 6 weeks to create a prototype of the project, we will limit the scope of the waste that our scanner will be able to detect to barcodes and basic materials (Glass, Paper, Cardboard, Plastic, Metal, Trash).

We have 3 teams: hardware, machine learning/computer vision, and UI/UX. Each team has its own milestones to complete throughout this project. We’ve split the milestones into 3 deliverables each of which will be due every 2 weeks. For each deliverable, the first week will be used for exploratory programming, research, and basic implementation. The second week will be used for troubleshooting, testing, and integration of the different teams’ portions of the project. At the end of every week, we will review what we accomplished and see if we are on schedule or not and adjust the schedule accordingly. 

The hardware team will get the Raspberry Pi, tablet, and camera connected together and setup. The ML/CV team will work on the program which will consist of barcode reading, object detection, and waste classification. The UI/UX team will work on the user interface portion so setting up the website on Github pages, designing the website, getting the page to change depending on the category of the waste, and implementing the buttons and more info pop ups. 

Luckily, due to the nature of this project, we are able to easily work on it remotely. The software does not depend on the hardware to run and be tested. Most of the software development will be done on our laptops since it only needs a camera and a screen, both of which a laptop have. 2 members will work on getting the hardware setup so that when it comes time to show our final product, we just need to open the website on the Raspberry Pi and make sure that it is using the external camera connected to the Raspberry Pi.

*****************
### Minimum Viable Product (1-2 pages)
###### *Describe a minimum viable product that demonstrates your project. This should be something that you will achieve with very high probability. It demonstrates the basic functionality and idea and enables feedback. Aim to get an MVP as soon as possible. Then iterate quickly on top of that adding more features as you have time. How will you iterate upon that over the quarter? What are the specific objectives of the project for this quarter? What are the longer term goals?*

Generally, the product shall be able to classify a type of waste when held up to the camera and direct the user to the proper location of which the waste should be disposed of. The overall effect of this is to decrease overall landfill and pollution while also increasing the availability of natural resources.

The product should consist of three main components: hardware, software, and user-interface/user-experience. All three sections integrated together will produce a product that should be able to guide the user in properly disposing waste in the correct location.

In terms of hardware, the product should consist of a touch-screen display and a camera. While the camera serves as the scanner that can detect objects, the touch-screen display would consist of the user interface that would display both information regarding the detected waste and a visual to what the camera sees. The hardware is the core component of our product as it combines the software and the UI/UX together. On the software side, we plan to combine machine learning and computer vision to handle the logic of detecting waste using OpenCV for detection and TensorFlow for machine learning. For the Minimal Viable Product, the product shall be able to identify waste by scanning the barcode attached to the product. Further implementations and features we hope to implement in the future would consist of holding the object to the camera without scanning for any barcode. In terms of the UI/UX, the product shall be easy to use so that no person shall be limited to using this product. The purpose of this product is to teach others the proper methods of disposing of items, and a solid foundation of the UI/UX would help achieve this goal.

Our product should start with ensuring the waste is properly identified, which both the hardware and software are responsible for. Additional features of our product are related to the UI/UX, making it easier for a user to dispose of products. Ideas that the product can implement are Google Maps, text message reminders, and more. In terms of software, a possible feature we can implement is training a separate computer module so that it is ensured that any type of waste can be identified. This means we would need to develop a neural network that would handle this logic.

Our goal for the quarter is to create a product that would educate and ensure that waste is placed in the correct category. We plan on achieving this with Smart Waste Scanner, an intelligent touch-screen display with a camera that can identify any type of waste and instruct the user to place it in the correct bin. Goals that can be classified as longer-term would be to implement additional features such as Google Maps to increase the user-experience of our product.

*****************
### Constraints, Risk, and Feasibility (1/2-1 page)
###### *What are the potential stumbling blocks? What is realistically feasible here? The quarter goes by very quickly. The better approach is to over-deliver on what you promise, rather than under deliver on a set of unrealistic goals. Be sure to include risks – a list of things that could go wrong and how to avoid them.*

There are a few potential stumbling blocks.  The first is finding a free or inexpensive barcode scanning API.  We’ll need to use an API because the CV implementation from camera images is difficult and certainly not feasible for our time frame.  Additionally, we’ll need to find/build/train a model for waste detection that fits our set of objects we’d like to classify.  We could also potentially have problems running our model on the Raspberry Pi, or finding a lightweight enough model that will work on it.  Finally, connecting all of our components (Raspberry Pi, camera, classifier, interface) could be a challenge.

Realistically, we should be able to deliver a system that properly classifies waste from our small sample set of objects (by taking a picture of the item) and displays the type of waste the object is on our interface along with additional recycling information.  This is realistic because at the very minimum we know that there are models that classify basic items such as banana peels and plastic bottles, so we will be able to properly classify these items, along with others defined in our set.  Additionally, connecting a frontend interface with a backend model is also highly feasible.

One of the biggest risks is biting off more than we can chew and trying to classify too many pieces of waste, leading us to have a product that works ineffectively.  The best way to avoid this risk is by carefully specifying our goals and limiting the set of waste we can sort.  Rather than trying to sort every single possible piece of waste, we’ll keep our list to the following objects: paper, water bottles, cans, glass bottles, pencils/pens, contact lens cases, batteries, newspapers, and banana peels.  Another thing that could go wrong is having too busy of a UI-- a way to avoid this is to carefully specify which features we’d like the user to have and then create a thoughtful design before coding up the frontend.
