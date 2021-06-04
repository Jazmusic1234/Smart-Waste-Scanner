/**
 * @name revealModal
 * @function
 * @description Opens the help modal when the help button is clicked
 */
function revealModal(category) {
    console.log('here')
    let modal = document.querySelector('.modal');
    if(category == 'glass') {
      document.getElementById('learn_more_title').innerHTML = "Glass";
    } else if(category == 'paper') {
      document.getElementById('learn_more_title').innerHTML = "Paper";
    } else if(category == 'plastic') {
      document.getElementById('learn_more_title').innerHTML = "Plastic";
    } else if(category == 'aluminum') {
      document.getElementById('learn_more_title').innerHTML = "Aluminum";
    }
    modal.style.display = 'block';
    // modal.style.visibility = 'visible';
}

/**
 * @name hideHelp
 * @function
 * @description Closes the help modal when the 'x' inside the modal or anywhere outside of the modal is clicked
 */
function hideModal() {
    let modal = document.querySelector('.modal');
    modal.style.display = 'none';
    // modal.style.visibility = 'hidden';
}

// export functions for testing
export { revealModal, hideModal }; 
