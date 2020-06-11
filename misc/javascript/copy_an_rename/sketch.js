import {hello} from "./modules/somefunc.js";

console.log(hello())



var i = 0;
new p5(function(p5){
	p5.setup = function(){
		p5.createCanvas(250,250);
		p5.frameRate(10); // determines the loop rate
	}


// Do note that the draw function is looped 
	p5.draw = function(){

		p5.background(50);		
		p5.ellipse(50,50,i+50,20);
		i++;
	}
	console.log(i)
});

