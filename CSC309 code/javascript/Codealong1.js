function square(number){
	return number * number
}

var squareofTwo = square(2)

var cubeOf = function(number){
	var squareOf = square  // only availabe within that function- function variable
	return number * sqaureOf(number)
}

// var squareOf = "Whatever"

// var cubeOf = function(number){
// 	squareOf = square  // only availabe within that function- function variable-without var- bad pracitce. can override the value outside
// 	//if we did var on the inside and no var outside for this variable, that should be okay because then there is no confusion
// 	return number * sqaureOf(number)
// }

function print(something){
	console.log(something)
}

function doThis(todo){//recieves a function as a parameter
	todo()
}

//doThis(4) -- error

// doThis(function(){
// 	console.log("This function would be called up in the doThis function")
// })

//alternative syntax

var myCallBack = function(){
	console.log(Running the myCallBack)
}

doThis(myCallBack)


console.log(squareofTwo)

console.log(squareOf)

console.log(cubeOf)

console.log(cubeOf(3))

print("Boss")
print(12345)
print([1,2,3,4,5])
print(cubeOf)//treats function like any other datatype
print(cubeOf(3))
print([cubeOf,square,print])//no problem what type is put in
var fancyArray = [cubeOf,square,print]
print (fancyArray)
console.log(fancyArray[0](4)) // call the cubeOf function by passing 4

//use of a callback function
   //useful for running code after a function call
   //useful because you do not depend on another server to do you code.
   //waits for the response from the server in case it is a request
//using let to declare variables
//let newVar = 34