/**
 * @name revealModal
 * @function
 * @description Opens the help modal when the help button is clicked
 */
function revealModal(category) {
    let modal = document.getElementById("learn_more_modal");
    if(category == 'glass') {
      document.getElementById("content").innerHTML = "<h3>Glass</h3><p>This is glass</p>";
      
      // document.getElementById('learn_more_title').innerHTML = "Glass";
      
      // // Add content here
      // document.getElementById('content').innerHTML = "This is the glass category";
      // document.getElementById('more_content').innerHTML = "Be careful with glass!";

    } else if(category == 'paper') {
      document.getElementById('learn_more_title').innerHTML = "Paper";
      
      // Add content here
      document.getElementById('content').innerHTML = "This is the glass category";

    } else if(category == 'plastic') {
      document.getElementById('learn_more_title').innerHTML = "Plastic";
     
      // Add content here
      document.getElementById('content').innerHTML = "This is the glass category";

    } else if(category == 'aluminum') {
      document.getElementById('learn_more_title').innerHTML = "Aluminum";
      
      // Add content here
      document.getElementById('content').innerHTML = "This is the glass category";

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
