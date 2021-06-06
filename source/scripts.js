/**
 * @name revealModal
 * @function
 * @description Opens the help modal when the help button is clicked
 */
function revealModal(category) {
    let modal = document.getElementById("learn_more_modal");
    if(category == 'glass') {
      document.getElementById("content").innerHTML = "<h3>Glass</h3>" +
            "<p>" + 
            "<h4> Special Instructions: </h4>" + 
              "<ul><li> Don’t break it</li><li> Ensure it's untreated glass (no mirrors, windows, etc)</li><li> Clean it (rinse, make sure there's no food, non-water liquid)</li></ul>" + 
            
            "<h4> Examples of Recyclable Glass: </h4>" + 
            "<ul><li> Glass bottles</li><li> Glass jars</li><li> Glass containers</li></ul>" + 

            "<h4> Facts about Glass Recycling: </h4>" +
            "<ul><li> A glass bottle could take up to 4000 years to decompose if not recycled</li><li> More than 28 billion recyclable glass bottles go to landfills each year, enough to fill about 2 Empire State Buildings every month</li><li> Recycling one glass bottle saves enough energy to light a room for 4 hours</li></ul>" + 

            "Glass is a better alternative than plastic when it comes to recycling, but glass is one of the least properly recycled materials out there! Though some glass can be recycled over and over again, making it a good choice, other types of glass (such as ceramics, lightbulbs, and mirrors) contain other materials in addition to the regular glass, so they cannot be recycled. A good way to make sure your glass is recyclable is to look out for any indications on the packaging. Another great way is to ask yourself: is it a bottle, jar, or container?" + 

            "<h4> Resources: </h4>" +
            "<ul><li> <a href='https://www.hazardouswasteexperts.com/five-tips-for-recycling-glass/'>https://www.hazardouswasteexperts.com/five-tips-for-recycling-glass/ </a> </li><li> <a href='https://wwf.panda.org/discover/knowledge_hub/teacher_resources/project_ideas/recycling_glass/'>https://wwf.panda.org/discover/knowledge_hub/teacher_resources/project_ideas/recycling_glass/ </a>  </li><li> <a href='https://www.calrecycle.ca.gov/glass'> https://www.calrecycle.ca.gov/glass </a> </li></ul>"  

            "</p>";

    } else if(category == 'paper') {
      document.getElementById("content").innerHTML = "<h3> Paper </h3>" +
            "<p>" +

            "<h4> Special Instructions: </h4>" +
            "Make sure the paper you recycle is clean and free of any other materials (such as tape, food, metal, etc)" +


            "<h4> Examples of Recyclable Paper: </h4>" +
            "<ul><li> Newspapers, magazines, catalogs</li><li> Mail, envelopes</li><li> Printer paper envelopes</li><li> Gift wrapping paper (as long as it's not coated in plastic or shine)</li><li> Cardboard</li><li> Egg cartons</li></ul>" +

            "<h4> Facts about Paper Recycling: </h4>" + 
            "<ul><li> Americans use about 700 pounds worth of paper per person each year</li><li> Recycling a stack of newspaper 3 feet high saves one whole tree</li><li> About 1 billion trees worth of paper is thrown away each year in the US</li></ul>" +

            "Paper is important to recycle because if it's not recycled, it can release carbon gas into the atmosphere. It's also important because it reduces the amount of trees that need to be cut down to make new paper products. Paper is the most recycled product around the world, yet in the US only around 65% of the paper in the US get recycled." +

            "<h4> Resources: </h4>" +
            "<ul><li> <a href='https://www.calrecycle.ca.gov/publiced/earthday/what'> https://www.calrecycle.ca.gov/publiced/earthday/what</a> </li><li> <a href='https://www.thebalancesmb.com/paper-recycling-facts-figures-and-information-sources-2877868#:~:text=Over%2068%20million%20tons%20of,continues%20to%20improve%20over%20time'> https://www.thebalancesmb.com/paper-recycling-facts-figures-and-information-sources-2877868#:~:text=Over%2068%20million%20tons%20of,continues%20to%20improve%20over%20time</a> </li></ul>" +

            "</p>";

    } else if(category == 'plastic') {
      document.getElementById("content").innerHTML = "<h3> Plastic </h3>" +
            "<p>" +
            "<h4> Special Instructions: </h4>" +
            "<ul><li> Typically only rigid plastics are recyclable. Plastic bags often jam recycling machines. </li><li> Check out the special codes on plastic items (recycling sign with a number in it)-- if it's 1 or 2, definitely recycle!</li><li> Plastic beverage bottles with codes 3-7 can be turned into special recycling centers, but not thrown in with your other recycling</li><li> Make sure the plastic is well rinsed out of any food or drinks</li><li> Ensure that the plastic doesn't have any stickers or other plastics around it</li></ul>" +

            "<h4> Examples of Recyclable Plastic: </h4>" +
            "<ul><li> Plastic bottle</li><li> Plastic containers</li><li> Milk and other food jugs</li></ul>" +

            "<h4> Facts about Plastic Recycling: </h4>" +
            "<ul><li> 2.5 milion plastic bottles are thrown away every hour in the US</li><li> Recycling plastic takes 88% less energy than making it from scratch</li><li> Recycling plastic can save up to two times the energy it takes to burn it down (plus recycling plastic doesn't emit the same harmful gases that incineration does</li><li> Plastic bags can take 1000 years to decompose</li><li> Some plastics, such as styrofoam, never decompose</li></ul>" +

            "<h4> Resources: </h4>" +
            "<ul><li> <a href='https://www.calrecycle.ca.gov/publiced/earthday/what https://www.usi.edu/recycle/plastic-recycling-facts/'> https://www.calrecycle.ca.gov/publiced/earthday/what https://www.usi.edu/recycle/plastic-recycling-facts/</a></li></ul>" +

            "</p>";

    } else if(category == 'aluminum') {
      document.getElementById("content").innerHTML = "<h3> Metal </h3>" +
            "<p>" +
            "<h4> Special Instructions: </h4>" +
            "<ul><li> Clean it (rinse, make sure there's no food, non-water liquid)</li></ul>" +

            "<h4> Examples of Recyclable Metal: </h4>" +
            "<ul><li> Soda can</li></ul>" +

            "<h4> Facts About Metal Recycling: </h4>" +
            "<ul><li> An recycled aluminum can can make it back to a grocery store shelf as brand new in as little as two months</li><li> Like glass, aluminum can also be recycled forever without losing any quality</li><li> Recycling a single aluminum can can save enough energy to power a TV for 3 hours</li></ul>" +

            "<h4> Resources: </h4>" +
            "<ul><li> <a href='https://www.roadrunnerwm.com/blog/50-interesting-recycling-facts'> https://www.roadrunnerwm.com/blog/50-interesting-recycling-facts</a></li></ul>" +

            "</p>";

    }
    modal.style.display = 'block';
}

/**
 * @name hideHelp
 * @function
 * @description Closes the help modal when the 'x' inside the modal or anywhere outside of the modal is clicked
 */
function hideModal() {
    let modal = document.getElementById("learn_more_modal");
    modal.style.display = 'none';
}

// export functions for testing
export { revealModal, hideModal }; 
