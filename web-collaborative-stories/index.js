
let div1 = document.createElement('div');
div1.className = 'container';
div1.id = 'container'


for (let i = 0; i < 60; i++) {
// Your existing code unmodified...

let div = document.createElement('div');
div.id = 'square';
div.className = 'square';


document.getElementsByTagName('body')[0].appendChild(div1);
div1.appendChild(div)
}



function helpfunction() {alert("this site is for writing collaborative stories together with other people.\n \n each user can write 1 para in any particular story and then must wait till 2 other users write 2 paras to write in the same story \n \n to contribute to a story you must sign up and register first \n \n  signing up is not mandatory and you can still read the stories \n \n click on the text in floating widgets to open their respective stories and read them")}

window.addEventListener('load', () => {
  const squares = document.querySelectorAll('.square');
  squares.forEach(square => {

    var link = document.createElement('a');

    link.href = 'content.html';
    link.style = 'text-decoration: none;'
    link.textContent = 'Visit Example';

    square.appendChild(link);


      const randomColor = getRandomColor();
      const randomColor2 = getRandomColor2();
      const randomColor3 = getRandomColor3();

      square.style.backgroundImage = `linear-gradient(to bottom,${randomColor3}  ,  ${randomColor2}, ${randomColor})`;
    
    });
});

function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
function getRandomColor2() {
  const letters2 = '0123456789ABCDEF';
  let color2 = '#';
  for (let i = 0; i < 6; i++) {
      color2 += letters2[Math.floor(Math.random() * 16)];
  }
  return color2;
}

function getRandomColor3() {
  const letters3 = '0123456789ABCDEF';
  let color3 = '#';
  for (let i = 0; i < 6; i++) {
      color3 += letters3[Math.floor(Math.random() * 16)];
  }
  return color3;
}



