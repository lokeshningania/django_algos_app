

const data = [34  ,32  ,56  ,45  ,36  ,90  ,23  ,12  ,98  ,27  ,75  ,16,  19  ,31 , 11  ,18  ,14  ,29  ,63]
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

  for (i = 0; i < data.length; i++){
    var para = document.createElement("p");
    para.id = `p${i}`
    para.innerHTML = `${i}`
    para.style.fontSize = "20px"
    document.getElementById(`arr${i}`).appendChild(para);
  }

  var index = parseInt(document.getElementById('index').innerHTML)
  

  for (i = 0; i < index+1; i++){
    task(i);
  }

  var pos = document.getElementById('elementpositionmsg');
  pos.style.visibility = 'hidden'
  function task(i) {
    setTimeout(function() {
      var indexcolor = document.getElementById(`arr${i}`)
      indexcolor.style.backgroundColor = 'red'
      var previndex = document.getElementById(`arr${i-1}`)
      previndex.style.backgroundColor = 'rgba(253,187,45,1)'
      

      if(i == index){
        indexcolor.style.backgroundColor = 'green'
        
        pos.style.visibility = 'visible'

      }
      

    }, 500 * i+1);
  }


