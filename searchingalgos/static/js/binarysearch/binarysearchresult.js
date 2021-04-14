
/* Array to perform search on */
const data = [1 , 4, 8 , 9 , 14 , 19 , 23 , 26 ,28 , 34 , 40 , 44 , 47 , 56 , 62 , 65 , 89 , 96 ]

/* for loop to create div element for each element of array */
for (i = 0; i < data.length; i++) { 
    var div = document.createElement("div");
    div.id = `arr${i}`
    div.innerHTML = data[i]
    div.style.width = "60px";
    div.style.height = "90px"
    div.style.background ="rgba(253,187,45,1)";
    div.style.color = "black";
    div.style.display = "inline-block";
    div.style.border = "solid 4px white"
    div.style.fontSize = "40px"
    div.style.textAlign = "center"
    document.getElementById("main").appendChild(div);
    
  }

  /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
/* for loop to create paragraph element for each div of element of array  to show index number*/
  for (i = 0; i < data.length; i++){
    var para = document.createElement("p");
    para.id = `p${i}`
    para.innerHTML = `${i}`
    para.style.fontSize = "20px"
    document.getElementById(`arr${i}`).appendChild(para);
  }
/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
  
/* to get the value of index number of the searched element */
var searchval = parseInt(document.getElementById('binarysearchval').innerHTML)

var array = JSON.parse(document.getElementById('list').innerHTML)

var binindex = parseInt(document.getElementById('index').innerHTML)
/* ~~~~~~~~~~~~~~~~~~~~~~~~~loop for colour changing~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

for (i=0 ; i< array.length; i++){

    task(i);
  
}



/* ~~~~~~~~~~~~~~~~~~~~~~~~~COLOUR VISUALS ANIMATION FUNCTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

 
  function task(i) {
    setTimeout(function() {
     


      var leftcolor = document.getElementById(`arr${array[i][0]}`)
      leftcolor.style.backgroundColor = 'teal'
      leftcolor.style.height = '120px'
      var midcolor = document.getElementById(`arr${array[i][1]}`)
      midcolor.style.backgroundColor = 'red'
      
      var rightcolor = document.getElementById(`arr${array[i][2]}`)
      rightcolor.style.backgroundColor = 'brown'
      rightcolor.style.height = '120px'

      if(array[i][1] == binindex){
        midcolor.style.backgroundColor = 'green'
        midcolor.style.height = '90px'

      }
      
    }, 2000 * i+1);
  }

  


