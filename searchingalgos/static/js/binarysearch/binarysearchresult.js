
/* Array to perform search on */
const data = [1 , 4, 8 , 9 , 14 , 19 , 23 , 26 ,28 , 34 , 40 , 44 , 47 , 56 , 62 , 65 , 89 , 96 , 101 ]

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
  
/* to get the value of index number and searched element and list of index iterated */
var searchval = parseInt(document.getElementById('binarysearchval').innerHTML)

var array = JSON.parse(document.getElementById('list').innerHTML)

var binindex = parseInt(document.getElementById('index').innerHTML)

document.getElementById('searchval').innerHTML = `${searchval}`
/* ~~~~~~~~~~~~~~~~~~~~~~~~~loop for colour changing~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

for (i=0 ; i< array.length; i++){

    task(i);
  
}



/* ~~~~~~~~~~~~~~~~~~~~~~~~~COLOUR VISUALS ANIMATION FUNCTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

 
  function task(i) {
    setTimeout(function() {
      /* ~~~~~~~~~~~~~~~~~~~~~~~~~Colours of prev positions changed to normal~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
      if(i>0){

        var pleftcolor = document.getElementById(`arr${array[i-1][0]}`)
        pleftcolor.style.backgroundColor = "rgba(253,187,45,1)"
        pleftcolor.style.height = '90px'
        var pmidcolor = document.getElementById(`arr${array[i-1][1]}`)
        pmidcolor.style.backgroundColor = "rgba(253,187,45,1)"
        pmidcolor.style.height = '90px'
        var prightcolor = document.getElementById(`arr${array[i-1][2]}`)
        prightcolor.style.backgroundColor = "rgba(253,187,45,1)"
        prightcolor.style.height = '90px'
     }
     /* ~~~~~~~~~~~~~~~~~~~~~~~~~change color according to mid left and right~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

      var leftcolor = document.getElementById(`arr${array[i][0]}`)
      leftcolor.style.backgroundColor = 'white'
      var midcolor = document.getElementById(`arr${array[i][1]}`)
      midcolor.style.backgroundColor = 'red'
      document.getElementById('midvalp').innerHTML = `${data[array[i][1]]}`
      
      if(data[array[i][1]] > searchval){
        document.getElementById('midvsign').innerHTML = ' > '
        
      }
      if(data[array[i][1]] < searchval){
        document.getElementById('midvsign').innerHTML = ' < '
      }

      
      
      var rightcolor = document.getElementById(`arr${array[i][2]}`)
      rightcolor.style.backgroundColor = 'black'
      rightcolor.style.color = 'white'
    /* ~~~~~~~~~~~~~~~~~~~~~~~~~if value found color change to green~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
      if(array[i][1] == binindex){
        midcolor.style.backgroundColor = 'green'
        midcolor.style.height = '90px'
        document.getElementById('midvsign').innerHTML = ' = '
        

      }
      
    }, 5000 * i+1);
  }

  


