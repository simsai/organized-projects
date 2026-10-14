
let switchState = animations = true;


let customEvent = new CustomEvent('animationsOff', {
    detail: { someData: 'someValue' }, // Optional data associated with the event
    bubbles: true, // Whether the event bubbles up through the DOM or not
    cancelable: true // Whether the event can be canceled with event.preventDefault()
  });
let customEvent2 = new CustomEvent('animationsOn', {
    detail: { someData: 'someValue' }, // Optional data associated with the event
    bubbles: true, // Whether the event bubbles up through the DOM or not
    cancelable: true // Whether the event can be canceled with event.preventDefault()
  });






// Function to create HTML for the toggle switch and text
function createToggleSwitch() {
  return `
    <div>
      <span style="vertical-align: middle;">toggle animations</span>
      <div class="toggle" style="display: inline-block;">
        <input type="checkbox" id="toggle-switch" ${switchState ? 'checked' : ''}>
        <label for="toggle-switch"></label>
      </div>
    </div>
  `;
}


  




let toggleswitch = document.getElementsByClassName('toggle').innerHTML;


document.getElementById("settingsIcon").addEventListener("click", function() {
    let toggleSwitchHTML = createToggleSwitch();

    // Trigger SweetAlert2 popup with toggle switch inside
    Swal.fire({
        title: 'settings',
        html: createToggleSwitch(),
        showCancelButton: true,
        confirmButtonText: 'OK',
        customClass: {
          // Custom class to define height
          popup: 'custom-popup-class',
        },
        didOpen: () => {
          // Add event listener to the checkbox inside the popup
          document.getElementById("toggle-switch").addEventListener("change", function() {
            toggled = this.checked;
            
          });
        }

      }).then((result) => {
        // Handle the result (the state of the switch)
        if (result.isConfirmed) {
            
            switchState = toggled  ;
            

          console.log("Switch state: " + switchState);

            if (switchState === false) {

                document.getElementById('para').dispatchEvent(customEvent);

            } else if (switchState === true)  {

                document.getElementById('para').dispatchEvent(customEvent2);

            }

        
        }
          // Perform actions based on the switch state here
        
      });

});


