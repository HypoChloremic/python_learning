// so there are multiple options to do this. 
// What arrow functions would like to do is to 
// make the syntax of function definitions much easier. 

// For instance, say we would like to pass a function as a
// parameter through a different method. One way of doing
// that is to actually just define the function with names and
// everything (the one we would like to pass):

function the_function_to_pass1(par){
	par();
}

function function_name1() {
 	return 10;
 } 

the_function_to_pass(function_name);

// instead we can write: 
the_function_to_pass(() => {return 10;});
// tadaa, very eazy.