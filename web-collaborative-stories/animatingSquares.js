
let squares = document.querySelectorAll('.square');
let animationsWereTurnedOff = false



squares.forEach(square => {
  square.addEventListener('mouseover', function(){if (switchState === true) {

    square.style.transform = 'scale(1.5)';
}})
  square.addEventListener('mouseout', function(){if (switchState  ===true) {
    square.style.transform = 'scale(1)';



  }})
})



// Function to start observing
function startObservingHiddenElements() {
  
  
  const hiddenElements = document.querySelectorAll('.square');
  

  // Define your observer
  const observerHiddenElements = new IntersectionObserver((entries, observer) => {
  
      entries.forEach((entry) => {
        
          if (entry.isIntersecting) {
            if (animationsWereTurnedOff === true && entry.target.classList.contains ('square') && switchState === true){
              entry.target.style.opacity =  '0.8';
              entry.target.style.filter= 'blur(0px)';
              entry.target.style.transform = 'translate(0, 0)' ;
              entry.target.style.transition= '1.5s';}
              entry.target.classList.add('show');

          } else {
            entry.target.classList.remove('show');            
            if (animationsWereTurnedOff === true && entry.target.classList.contains ('square') && switchState === true){ 
              entry.target.style.opacity =  '0';
              entry.target.style.filter= 'blur(3px)';
              entry.target.style.transform = 'translate(-100%, -75%)' ;
              entry.target.style.transition= '1.5s';}
              
          }
      });
  
  });


  




  hiddenElements.forEach((el) => observerHiddenElements.observe(el));





}



function handlemouseover(square){console.log('hmm')
 square.classList.add('highlight');}

function handlemouseout(square){square.classList.remove('highlight');}

// Function to stop observing
function stopObservingHiddenElements() {


  
  squares.forEach(square => {

    
    square.style.opacity = '0.8'; square.style.filter = 'blur(0)'; square.style.transform = 'translate(0,0)';
    animationsWereTurnedOff = true
  
  });


  
}

// Start observing initially
startObservingHiddenElements();

// Event listener for animationsOff event
document.getElementById('para').addEventListener('animationsOff', () => {
 
  stopObservingHiddenElements();
});

// Event listener for animationsOn event
document.getElementById('para').addEventListener('animationsOn', () => {
  startObservingHiddenElements();
});






window.addEventListener('load', () => {
    const headingg = document.querySelectorAll('.heading');
    headingg.forEach(element => {
        element.classList.remove('showHeading');
        element.classList.remove('heading');
        setTimeout(() => {
        element.classList.add('showHeading');
        element.classList.add('heading');
        }, 20);
    });
});


const observerHiddenElements1 = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {

        if (entry.isIntersecting && switchState === true) {
            entry.target.classList.add('showHeading');
            entry.target.classList.add('heading');
            
        } else if (entry.isIntersecting && switchState === false){entry.target.classList.add('heading')}
        else {
            entry.target.classList.remove('showHeading');
            entry.target.classList.remove('heading');
        }
    });
});

// Observe hiddenElements1
const hiddenElements1 = document.querySelectorAll('.heading');
hiddenElements1.forEach((el) => observerHiddenElements1.observe(el));




function hovering(){
  console.log("called")
const isHover = e => e.parentElement.querySelector(':hover') === e;   



squares.forEach(square => {

    document.addEventListener('mousemove', function checkHover() {
        const hovered = isHover(square);
        if (hovered !== checkHover.hovered) {
            if (hovered) {
                square.classList.add('highlight')
            } else(square.classList.remove('highlight'))
          
          checkHover.hovered = hovered;
        }
      });

});

}



